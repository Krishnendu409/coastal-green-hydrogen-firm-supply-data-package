"""
Fetch 20 years of hourly meteorological data (2005-2024) from NASA POWER API
for coastal Karnataka (13.3525°N, 74.7928°E).
Parameters: ALLSKY_SFC_SW_DWN (GHI, W/m2), WS10M (m/s), WS50M (m/s), T2M (Air Temp at 2m, C).
Derived:
  - alpha_shear: Monin-Obukhov power-law shear exponent alpha = ln(WS50/WS10) / ln(50/10)
  - ws100m_m_s: Wind speed at 100m hub height = WS50 * (100/50)^alpha
"""
import urllib.request
import json
import time
import os
import pandas as pd
import numpy as np

LAT = 13.3525
LON = 74.7928
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "weather_and_resource")
os.makedirs(OUT_DIR, exist_ok=True)

CHUNKS = [
    ("20050101", "20091231"),
    ("20100101", "20141231"),
    ("20150101", "20191231"),
    ("20200101", "20241231"),
]

all_records = []

print(f"Fetching 20-year hourly weather for Lat={LAT}, Lon={LON} (2005-2024)...")

for start_date, end_date in CHUNKS:
    url = (
        "https://power.larc.nasa.gov/api/temporal/hourly/point"
        f"?parameters=ALLSKY_SFC_SW_DWN,WS10M,WS50M,T2M"
        f"&community=RE&longitude={LON}&latitude={LAT}"
        f"&start={start_date}&end={end_date}&format=JSON"
    )
    print(f"  Fetching chunk {start_date} to {end_date}...")
    success = False
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            params = data["properties"]["parameter"]
            ghi_dict = params["ALLSKY_SFC_SW_DWN"]
            ws10_dict = params["WS10M"]
            ws50_dict = params["WS50M"]
            t2m_dict = params["T2M"]
            
            timestamps = sorted(ghi_dict.keys())
            print(f"    Retrieved {len(timestamps)} hours for {start_date[:4]}-{end_date[:4]}")
            
            for ts in timestamps:
                year = int(ts[0:4])
                month = int(ts[4:6])
                day = int(ts[6:8])
                hour = int(ts[8:10])
                
                ghi = float(ghi_dict.get(ts, 0.0))
                ws10 = float(ws10_dict.get(ts, 3.0))
                ws50 = float(ws50_dict.get(ts, 4.5))
                t2m = float(t2m_dict.get(ts, 27.0))
                
                # NASA missing data sentinels (-999)
                if ghi < 0 or ghi > 1400:
                    ghi = 0.0
                if ws10 < 0 or ws10 > 50:
                    ws10 = 3.2
                if ws50 < 0 or ws50 > 60:
                    ws50 = 4.8
                if t2m < -10 or t2m > 55:
                    t2m = 27.5
                
                # Atmospheric shear exponent alpha bounded between 0.08 and 0.35
                safe_ws10 = max(0.1, ws10)
                safe_ws50 = max(safe_ws10 + 0.05, ws50)
                alpha = np.clip(np.log(safe_ws50 / safe_ws10) / np.log(50.0 / 10.0), 0.08, 0.35)
                ws100 = safe_ws50 * ((100.0 / 50.0) ** alpha)
                
                all_records.append({
                    "timestamp": ts,
                    "year": year,
                    "month": month,
                    "day": day,
                    "hour": hour,
                    "ghi_w_m2": round(ghi, 2),
                    "ws10m_m_s": round(ws10, 2),
                    "ws50m_m_s": round(ws50, 2),
                    "ws100m_m_s": round(ws100, 2),
                    "temp_c": round(t2m, 2),
                    "alpha_shear": round(float(alpha), 4),
                })
            success = True
            time.sleep(1.5)  # respectful delay between API calls
            break
        except Exception as e:
            print(f"    Attempt {attempt+1} failed: {e}. Retrying in 3s...")
            time.sleep(3)
    if not success:
        raise RuntimeError(f"Failed to fetch chunk {start_date} to {end_date}")

df_20yr = pd.DataFrame(all_records)
csv_20yr_path = os.path.join(OUT_DIR, "hourly_weather_karnataka_2005_2024_20yr.csv")
df_20yr.to_csv(csv_20yr_path, index=False)
print(f"\n[DONE] Saved 20-year dataset ({len(df_20yr)} hours) to {csv_20yr_path}")

# Also save 2019-2024 subset for quick local runs
df_6yr = df_20yr[df_20yr["year"] >= 2019].copy()
csv_6yr_path = os.path.join(OUT_DIR, "hourly_weather_karnataka_2019_2024_6yr.csv")
df_6yr.to_csv(csv_6yr_path, index=False)
print(f"[DONE] Saved 6-year benchmark subset ({len(df_6yr)} hours) to {csv_6yr_path}")

# Compute Interannual Variability Summary (Annual metrics)
summary = []
for yr, grp in df_20yr.groupby("year"):
    ann_solar_kwh_m2 = grp["ghi_w_m2"].sum() / 1000.0
    mean_ghi = grp["ghi_w_m2"].mean()
    mean_ws10 = grp["ws10m_m_s"].mean()
    mean_ws50 = grp["ws50m_m_s"].mean()
    mean_ws100 = grp["ws100m_m_s"].mean()
    mean_temp = grp["temp_c"].mean()
    
    # Wind CF estimate (IEC Class III turbine, v_in=3, v_rated=10.5, v_out=25 m/s)
    v = grp["ws100m_m_s"].values
    cf_w = np.zeros_like(v)
    m = (v >= 3.0) & (v < 10.5)
    cf_w[m] = (v[m]**3 - 3.0**3) / (10.5**3 - 3.0**3)
    cf_w[(v >= 10.5) & (v <= 25.0)] = 1.0
    cf_w *= 0.95
    mean_wind_cf = np.mean(cf_w)
    
    # Solar CF estimate
    cf_s = np.clip((grp["ghi_w_m2"].values / 1000.0) * 0.96 * (1.0 - 0.0038 * np.maximum(0, grp["temp_c"].values - 25)), 0, 1)
    mean_solar_cf = np.mean(cf_s)
    
    summary.append({
        "year": yr,
        "hours_recorded": len(grp),
        "mean_ghi_w_m2": round(mean_ghi, 2),
        "annual_ghi_kwh_m2_yr": round(ann_solar_kwh_m2, 1),
        "mean_ws10m_m_s": round(mean_ws10, 2),
        "mean_ws50m_m_s": round(mean_ws50, 2),
        "mean_ws100m_m_s": round(mean_ws100, 2),
        "mean_temp_c": round(mean_temp, 2),
        "solar_capacity_factor": round(float(mean_solar_cf), 4),
        "wind_capacity_factor_100m": round(float(mean_wind_cf), 4),
    })

df_sum = pd.DataFrame(summary)
csv_sum_path = os.path.join(OUT_DIR, "annual_variability_summary_2005_2024.csv")
df_sum.to_csv(csv_sum_path, index=False)
print(f"[DONE] Saved annual summary table to {csv_sum_path}")
print("\nAnnual variability highlights:")
print(df_sum[["year", "annual_ghi_kwh_m2_yr", "mean_ws100m_m_s", "solar_capacity_factor", "wind_capacity_factor_100m"]].to_string(index=False))
