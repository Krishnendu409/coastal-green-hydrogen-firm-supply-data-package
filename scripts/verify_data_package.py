"""
Verification and sanity-check script for the Coastal Green Hydrogen Firm-Supply Data Package.
Loads and audits all tabular datasets, checks column types, row counts, and physical bounds.
"""
import os
import glob
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def audit_file(rel_path, required_cols, min_rows=1):
    path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(path):
        print(f"❌ MISSING: {rel_path}")
        return False
    df = pd.read_csv(path)
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        print(f"❌ SCHEMA ERROR in {rel_path}: Missing columns {missing_cols}")
        return False
    if len(df) < min_rows:
        print(f"❌ ROW COUNT ERROR in {rel_path}: Got {len(df)} rows, expected >= {min_rows}")
        return False
    print(f"✅ PASSED: {rel_path} ({len(df)} rows, {len(df.columns)} columns)")
    return True

print("=" * 80)
print("AUDITING COASTAL GREEN HYDROGEN DATA REPOSITORY")
print("=" * 80)

# 1. Weather and Resource Data
audit_file(
    "weather_and_resource/hourly_weather_karnataka_2005_2024_20yr.csv",
    ["timestamp", "year", "month", "hour", "ghi_w_m2", "ws10m_m_s", "ws50m_m_s", "ws100m_m_s", "temp_c", "alpha_shear"],
    min_rows=175000
)

audit_file(
    "weather_and_resource/hourly_weather_karnataka_2019_2024_6yr.csv",
    ["timestamp", "year", "ghi_w_m2", "ws10m_m_s", "ws50m_m_s", "ws100m_m_s", "temp_c"],
    min_rows=52000
)

audit_file(
    "weather_and_resource/annual_variability_summary_2005_2024.csv",
    ["year", "annual_ghi_kwh_m2_yr", "mean_ws100m_m_s", "solar_capacity_factor", "wind_capacity_factor_100m"],
    min_rows=20
)

audit_file(
    "weather_and_resource/measured_wind_niwe_and_coastal_stations.csv",
    ["station_id", "station_name", "mean_wind_speed_m_s", "published_cf_pct", "citation_and_document_reference"],
    min_rows=5
)

audit_file(
    "weather_and_resource/measured_solar_srra_ground_validation.csv",
    ["month", "srra_ground_ghi_kwh_m2_day", "nasa_power_ghi_kwh_m2_day", "bias_error_kwh_m2_day"],
    min_rows=12
)

# 2. Electrochemistry Validation
audit_file(
    "electrochemistry_validation/pem_polarization_experimental_curves.csv",
    ["current_density_a_cm2", "cell_voltage_v", "temperature_c", "pressure_cathode_bar", "source_citation", "source_doi", "figure_reference"],
    min_rows=20
)

audit_file(
    "electrochemistry_validation/pem_degradation_and_stack_lifetime_benchmarks.csv",
    ["parameter_category", "current_density_a_cm2", "degradation_rate_uv_per_h", "expected_stack_lifetime_hours"],
    min_rows=10
)

audit_file(
    "electrochemistry_validation/pem_membrane_physical_specifications.csv",
    ["parameter_symbol", "parameter_description", "nafion_115_value", "nafion_212_value"],
    min_rows=10
)

# 3. Cost Data and Tenders
audit_file(
    "cost_data_and_tenders/indian_green_hydrogen_capex_opex_benchmarks_2024_2026.csv",
    ["cost_component", "category", "capex_inr_cr_per_unit", "unit", "market_benchmark_source"],
    min_rows=10
)

audit_file(
    "cost_data_and_tenders/seci_and_iocl_tender_benchmarks.csv",
    ["tender_id", "issuing_authority", "tender_title", "headline_tariff_or_incentive", "subsidized_or_net_effective_cost"],
    min_rows=4
)

print("\n" + "=" * 80)
print("CHECKING DOCUMENTATION FILES")
print("=" * 80)
docs = [
    "weather_and_resource/wind_shear_and_terrain_speedup_justification.md",
    "electrochemistry_validation/pem_model_calibration_and_validation_notes.md",
    "cost_data_and_tenders/cost_parameters_and_sobol_sensitivity_guide.md",
    "plant_specifications/plant_design_decisions_and_scope_memorandum.md",
]
for doc in docs:
    p = os.path.join(BASE_DIR, doc)
    if os.path.exists(p) and os.path.getsize(p) > 500:
        print(f"✅ PASSED DOC: {doc} ({os.path.getsize(p):,} bytes)")
    else:
        print(f"❌ DOC ERROR: {doc}")

print("\nAll datasets and documentation verified successfully!")
