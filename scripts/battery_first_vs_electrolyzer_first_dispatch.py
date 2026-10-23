"""
Comparative Dispatch Simulation: Battery-First vs Electrolyzer-First
Evaluates firm supply reliability (LPSP) and stack degradation under 20-year coastal weather.
"""
import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WEATHER_FILE = os.path.join(BASE_DIR, "weather_and_resource", "hourly_weather_karnataka_2019_2024_6yr.csv")

if not os.path.exists(WEATHER_FILE):
    raise FileNotFoundError(f"Missing {WEATHER_FILE}")

df = pd.read_csv(WEATHER_FILE)

# Baseline plant configuration from Pareto knee point
P_WIND_MW = 51.13
P_SOLAR_MW = 94.73
P_PEM_NOM_MW = 38.98
P_PEM_MAX_MW = 48.72  # Operating dynamically up to i_max = 2.84 A/cm2
BATT_CAP_MWH = 20.07
BATT_POWER_MW = 10.0
DEMAND_H2_KG_H = 500.0  # 500 kg/h firm demand
SPEC_ENERGY_KWH_KG = 52.5  # Nominal specific energy consumption (kWh/kg H2)
P_DEMAND_MW = (DEMAND_H2_KG_H * SPEC_ENERGY_KWH_KG) / 1000.0  # ~26.25 MW electrical equivalent

print(f"Loaded {len(df)} hourly steps ({len(df)//8760} years).")
print(f"Plant Configuration: Wind={P_WIND_MW:.2f} MW, Solar={P_SOLAR_MW:.2f} MW, PEM={P_PEM_NOM_MW:.2f} MW, BESS={BATT_CAP_MWH:.2f} MWh")
print(f"Firm Demand: {DEMAND_H2_KG_H} kg/h ({P_DEMAND_MW:.2f} MW eq.)\n")

# Calculate generation profiles
# Solar capacity factor
cell_temp = df["temp_c"].values + (df["ghi_w_m2"].values / 800.0) * 25.0
pv_derate = 1.0 - 0.0038 * np.maximum(0.0, cell_temp - 25.0)
cf_solar = np.clip((df["ghi_w_m2"].values / 1000.0) * pv_derate * 0.96, 0.0, 1.0)
p_solar = cf_solar * P_SOLAR_MW

# Wind capacity factor
v = df["ws100m_m_s"].values
cf_wind = np.zeros_like(v)
m = (v >= 3.0) & (v < 10.5)
cf_wind[m] = (v[m]**3 - 3.0**3) / (10.5**3 - 3.0**3)
cf_wind[(v >= 10.5) & (v <= 25.0)] = 1.0
cf_wind *= 0.95
p_wind = cf_wind * P_WIND_MW

p_total = p_solar + p_wind

def simulate_dispatch(mode="battery_first"):
    soc = 0.50 * BATT_CAP_MWH  # Initial 50% SoC
    soc_min = 0.15 * BATT_CAP_MWH
    soc_max = 0.90 * BATT_CAP_MWH
    
    unserved_h2_kg = 0.0
    total_demand_kg = DEMAND_H2_KG_H * len(df)
    curtailed_mwh = 0.0
    batt_throughput_mwh = 0.0
    stack_ramp_events = 0
    prev_pem_power = P_DEMAND_MW
    
    for t in range(len(df)):
        p_gen = p_total[t]
        
        if mode == "battery_first":
            # Priority 1: Satisfy firm hydrogen demand
            if p_gen >= P_DEMAND_MW:
                pem_power = min(P_PEM_MAX_MW, p_gen)
                surplus = p_gen - pem_power
                # Send remaining surplus to battery
                charge_space = soc_max - soc
                p_charge = min(BATT_POWER_MW, surplus, charge_space)
                soc += p_charge * 0.95
                curtailed_mwh += (surplus - p_charge)
                delivered_h2 = (pem_power * 1000.0) / SPEC_ENERGY_KWH_KG
            else:
                # Deficit below firm demand: discharge battery to bridge gap
                deficit = P_DEMAND_MW - p_gen
                avail_discharge = max(0.0, soc - soc_min)
                p_discharge = min(BATT_POWER_MW, deficit, avail_discharge * 0.95)
                soc -= (p_discharge / 0.95)
                batt_throughput_mwh += p_discharge
                pem_power = p_gen + p_discharge
                delivered_h2 = (pem_power * 1000.0) / SPEC_ENERGY_KWH_KG
                
        elif mode == "electrolyzer_first":
            # Electrolyzer takes maximum possible variable power up to P_PEM_MAX
            pem_power = min(P_PEM_MAX_MW, p_gen)
            delivered_h2 = (pem_power * 1000.0) / SPEC_ENERGY_KWH_KG
            surplus = max(0.0, p_gen - pem_power)
            
            # Battery only absorbs what electrolyzer cannot take
            charge_space = soc_max - soc
            p_charge = min(BATT_POWER_MW, surplus, charge_space)
            soc += p_charge * 0.95
            curtailed_mwh += (surplus - p_charge)
            
            # If delivered H2 < firm demand, discharge battery
            if delivered_h2 < DEMAND_H2_KG_H:
                deficit_mw = (DEMAND_H2_KG_H - delivered_h2) * SPEC_ENERGY_KWH_KG / 1000.0
                avail_discharge = max(0.0, soc - soc_min)
                p_discharge = min(BATT_POWER_MW, deficit_mw, avail_discharge * 0.95)
                soc -= (p_discharge / 0.95)
                batt_throughput_mwh += p_discharge
                delivered_h2 += (p_discharge * 1000.0) / SPEC_ENERGY_KWH_KG

        # Check shortfall
        shortfall = max(0.0, DEMAND_H2_KG_H - delivered_h2)
        unserved_h2_kg += shortfall
        
        # Track dynamic ramp rate
        if abs(pem_power - prev_pem_power) > 0.20 * P_PEM_NOM_MW:
            stack_ramp_events += 1
        prev_pem_power = pem_power
        
    lpsp = (unserved_h2_kg / total_demand_kg) * 100.0
    annual_cycles = batt_throughput_mwh / BATT_CAP_MWH / (len(df)/8760.0)
    
    return {
        "mode": mode,
        "lpsp_pct": round(lpsp, 3),
        "firm_availability_pct": round(100.0 - lpsp, 3),
        "unserved_h2_t_yr": round((unserved_h2_kg / 1000.0) / (len(df)/8760.0), 2),
        "annual_bess_cycles": round(annual_cycles, 1),
        "curtailed_energy_gwh_yr": round((curtailed_mwh / 1000.0) / (len(df)/8760.0), 2),
        "stack_ramp_stress_events_yr": int(stack_ramp_events / (len(df)/8760.0)),
    }

res_bf = simulate_dispatch("battery_first")
res_ef = simulate_dispatch("electrolyzer_first")

df_res = pd.DataFrame([res_bf, res_ef])
print("=" * 80)
print("DISPATCH COMPARISON SUMMARY")
print("=" * 80)
print(df_res.to_string(index=False))
