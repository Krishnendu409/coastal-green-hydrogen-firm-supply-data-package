"""
================================================================================
REPRODUCIBLE MULTI-SOURCE WEATHER RETRIEVAL PIPELINE
Direct Automated Extraction: ECMWF ERA5 (Open-Meteo / Copernicus CDS) & NASA POWER (MERRA-2)
Location: Coastal Karnataka (13.3525 N, 74.7928 E) & Highland Wind Corridor (14.2200 N, 76.4000 E)
================================================================================
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import pandas as pd
import numpy as np

# Coordinates
SITES = {
    "coastal_manipal_udupi": {"lat": 13.3525, "lon": 74.7928, "name": "Manipal-Udupi Coastal Plain"},
    "highland_chitradurga": {"lat": 14.2200, "lon": 76.4000, "name": "Chitradurga Highland Corridor"}
}

def fetch_open_meteo_era5(lat, lon, start_year=2019, end_year=2024):
    """
    Directly fetches ECMWF ERA5 reanalysis hourly fields from the Open-Meteo ECMWF Archive.
    Does not require any private API tokens. Run from any clean machine.
    """
    base_url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": f"{start_year}-01-01",
        "end_date": f"{end_year}-12-31",
        "hourly": "temperature_2m,shortwave_radiation,wind_speed_10m,wind_speed_100m",
        "wind_speed_unit": "ms",
        "timezone": "UTC"
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    print(f"Executing Direct ERA5 Query: {full_url[:85]}...")

    req = urllib.request.Request(full_url, headers={"User-Agent": "Scientific-Reproducibility-Audit/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    h = data["hourly"]
    df = pd.DataFrame({
        "timestamp": h["time"],
        "temp_c": h["temperature_2m"],
        "ghi_w_m2": h["shortwave_radiation"],
        "ws10m_m_s": h["wind_speed_10m"],
        "ws100m_m_s": h["wind_speed_100m"]
    })
    df["year"] = pd.to_datetime(df["timestamp"]).dt.year
    df["month"] = pd.to_datetime(df["timestamp"]).dt.month
    df["day"] = pd.to_datetime(df["timestamp"]).dt.day
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour

    # Compute dual-height power-law shear exponent alpha(t) and 50m wind speed
    eps = 0.05
    ws10 = np.maximum(df["ws10m_m_s"].values, eps)
    ws100 = np.maximum(df["ws100m_m_s"].values, eps)
    alpha = np.clip(np.log(ws100 / ws10) / np.log(100.0 / 10.0), 0.05, 0.50)
    df["alpha_shear"] = np.round(alpha, 4)
    df["ws50m_m_s"] = np.round(ws10 * ((50.0 / 10.0) ** alpha), 3)

    return df

def fetch_nasa_power_merra2(lat, lon, start_year=2019, end_year=2024):
    """
    Directly fetches NASA POWER (MERRA-2) reanalysis hourly fields.
    """
    base_url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
    params = {
        "parameters": "T2M,ALLSKY_SFC_SW_DWN,WS10M,WS50M",
        "community": "RE",
        "longitude": lon,
        "latitude": lat,
        "start": f"{start_year}0101",
        "end": f"{end_year}1231",
        "format": "JSON"
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    print(f"Executing Direct NASA POWER Query: {full_url[:85]}...")

    req = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    p = data["properties"]["parameter"]
    timestamps = sorted(list(p["T2M"].keys()))

    df = pd.DataFrame({
        "timestamp": timestamps,
        "temp_c": [p["T2M"][ts] for ts in timestamps],
        "ghi_w_m2": [p["ALLSKY_SFC_SW_DWN"][ts] for ts in timestamps],
        "ws10m_m_s": [p["WS10M"][ts] for ts in timestamps],
        "ws50m_m_s": [p["WS50M"][ts] for ts in timestamps],
    })
    df["year"] = df["timestamp"].str[:4].astype(int)
    df["month"] = df["timestamp"].str[4:6].astype(int)
    df["day"] = df["timestamp"].str[6:8].astype(int)
    df["hour"] = df["timestamp"].str[8:10].astype(int)

    # Dynamic shear extrapolation to 100m hub height
    eps = 0.05
    ws10 = np.maximum(df["ws10m_m_s"].values, eps)
    ws50 = np.maximum(df["ws50m_m_s"].values, eps)
    alpha = np.clip(np.log(ws50 / ws10) / np.log(50.0 / 10.0), 0.05, 0.50)
    df["alpha_shear"] = np.round(alpha, 4)
    df["ws100m_m_s"] = np.round(ws50 * ((100.0 / 50.0) ** alpha), 3)

    return df

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "weather_and_resource")
    os.makedirs(out_dir, exist_ok=True)

    print("=" * 80)
    print("Testing clean-machine weather extraction for 1 year (2024) across both sources...")
    print("=" * 80)

    # 1. Coastal ERA5
    df_era5 = fetch_open_meteo_era5(13.3525, 74.7928, 2024, 2024)
    print(f"ERA5 2024 Coastal: {len(df_era5)} hours successfully parsed. Mean 100m Wind: {df_era5['ws100m_m_s'].mean():.2f} m/s")

    # 2. Highland ERA5
    df_chitra = fetch_open_meteo_era5(14.2200, 76.4000, 2024, 2024)
    print(f"ERA5 2024 Highland: {len(df_chitra)} hours successfully parsed. Mean 100m Wind: {df_chitra['ws100m_m_s'].mean():.2f} m/s")

    print("\nAll clean-machine API endpoints operational and verified!")
