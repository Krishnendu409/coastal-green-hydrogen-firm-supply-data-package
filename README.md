# Coastal Green Hydrogen Firm-Supply Data Package (2005–2025)
### Micro-Meteorological, Electrochemical & Techno-Economic Data Repository for Islanded Wind–Solar–PEMWE Sizing and Process Resiliency

[![Data Verification](https://img.shields.io/badge/Data%20Audit-Verified%20100%25-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Coordinates](https://img.shields.io/badge/Location-13.3525%C2%B0N%20%7C%2074.7928%C2%B0E-orange.svg)]()

This open-access repository provides the complete, multi-domain empirical dataset compiled for the techno-economic optimization, dynamic electrochemical validation, and multivariate process monitoring of an islanded **$500\text{ kg H}_2/\text{h}$** ($4,380\text{ t/yr}$) hybrid coastal Wind–Solar–Battery–PEM Electrolyzer facility located in the **Manipal–Udupi–Mangalore coastal industrial corridor, Karnataka, India** ($13.3525^\circ\text{N}, 74.7928^\circ\text{E}$).

---

## 📁 Repository Directory Structure

```text
├── weather_and_resource/
│   ├── hourly_weather_karnataka_2005_2024_20yr.csv       # 20-Year Hourly Weather (175,320 rows: GHI, WS10, WS50, WS100, Temp)
│   ├── hourly_weather_karnataka_2019_2024_6yr.csv        # 6-Year High-Resolution Subset (52,608 rows)
│   ├── annual_variability_summary_2005_2024.csv          # Year-by-year P10/P50/P90 interannual metrics
│   ├── measured_wind_niwe_and_coastal_stations.csv       # NIWE 100m masts, IMD observatories & commercial wind CFs
│   ├── measured_solar_srra_ground_validation.csv         # MNRE SRRA ground pyranometer vs reanalysis bias table
│   └── wind_shear_and_terrain_speedup_justification.md    # Boundary layer log-law & WAsP plateau speed-up physics
│
├── electrochemistry_validation/
│   ├── pem_polarization_experimental_curves.csv          # Multi-T, multi-P experimental V-i curves (0.05 - 3.5 A/cm2)
│   ├── pem_degradation_and_stack_lifetime_benchmarks.csv # Degradation rates (uV/h) vs load + OEM datasheets (Nel, Plug, ITM, Siemens)
│   ├── pem_membrane_physical_specifications.csv          # Nafion 115 vs 212 parameters, HFR, H2 crossover flux
│   └── pem_model_calibration_and_validation_notes.md     # First-principles DAE model equations & calibration fit (R2 > 0.999)
│
├── cost_data_and_tenders/
│   ├── indian_green_hydrogen_capex_opex_benchmarks_2024_2026.csv # Current Indian quotes (WACC, PEM stack, solar, wind, BESS)
│   ├── seci_and_iocl_tender_benchmarks.csv               # SECI SIGHT Tranche I/II awards & IOCL 10 KTA Panipat tender
│   └── cost_parameters_and_sobol_sensitivity_guide.md   # WACC derivation (10.05%) & Sobol global variance decomposition
│
├── plant_specifications/
│   └── plant_design_decisions_and_scope_memorandum.md    # Confirmed 500 kg/h demand, LPSP <= 1%, off-grid boundary & BoP scope
│
├── scripts/
│   ├── fetch_nasa_power_weather.py                       # Automated NASA POWER API pipeline for 20-year weather data
│   ├── verify_data_package.py                            # Automated integrity and bounds test suite
│   └── battery_first_vs_electrolyzer_first_dispatch.py   # 6-year comparative dispatch simulation script
│
├── LICENSE                                               # Open MIT License
└── README.md                                             # This comprehensive guide
```

---

## ⚡ Itemized Data Summary

### A. Weather & Renewable Resource Data (`weather_and_resource/`)
1. **20-Year Hourly Meteorological Dataset (`hourly_weather_karnataka_2005_2024_20yr.csv`):**
   - **Coverage:** January 1, 2005 to December 31, 2024 ($175,320\text{ consecutive hours}$).
   - **Variables:** Global Horizontal Irradiance (`ghi_w_m2`), Wind Speed at 10m (`ws10m_m_s`), Wind Speed at 50m (`ws50m_m_s`), Wind Speed at 100m hub height (`ws100m_m_s`), 2m Ambient Temperature (`temp_c`), Dynamic Shear Exponent (`alpha_shear`).
   - **Interannual Variability:** Annual solar radiation fluctuates between $1,796.0\text{ kWh/m}^2/\text{yr}$ (2024) and $1,980.9\text{ kWh/m}^2/\text{yr}$ (2006). Mean 100m wind speed varies between $3.90\text{ m/s}$ (2023) and $4.64\text{ m/s}$ (2013).
2. **Measured Ground Wind Stations (`measured_wind_niwe_and_coastal_stations.csv`):**
   - Ground truth from NIWE dedicated 100m met mast at Kapu/Malpe ($13.226^\circ\text{N}$, 12 km from site), showing annual mean 100m wind speed of **$6.24\text{ m/s}$** ($9.45\text{ m/s}$ during Southwest Monsoon) with Weibull $k = 2.28, c = 7.04\text{ m/s}$ and audited commercial wind farm capacity factors of **$25.6\% - 28.2\%$**.
3. **Terrain Speed-Up Justification (`wind_shear_and_terrain_speedup_justification.md`):**
   - Replaces empirical speed-up multipliers with the physical Monin-Obukhov internal boundary layer transition from the Arabian Sea ($z_{0,\text{marine}} \approx 0.005\text{ m}$) to terrestrial surfaces, and WAsP / IEC 61400-1 Annex B escarpment acceleration for 40m laterite coastal tablelands ($S = 2 H / L_h \approx 1.27\times$).
4. **Measured Solar Ground Pyranometer Data (`measured_solar_srra_ground_validation.csv`):**
   - MNRE SRRA Station 28003 (NITK Surathkal, 35 km south of site) ground pyranometer records compared against reanalysis GHI. Shows a mean positive reanalysis bias of **$+4.31\%$** ($+0.22\text{ kWh/m}^2/\text{day}$), primarily during pre-monsoon sea haze. Recommended solar bias correction multiplier: **$0.958$**.

---

### B. Electrochemistry & PEM Model Validation (`electrochemistry_validation/`)
1. **Measured PEM Polarization Curves (`pem_polarization_experimental_curves.csv`):**
   - 39 experimental coordinate sets digitized from peer-reviewed literature across current densities from $0.05$ to $3.50\text{ A/cm}^2$.
   - **Conditions:** $60^\circ\text{C}, 75^\circ\text{C}, 80^\circ\text{C}$; pressures $1\text{ bar}, 10\text{ bar}, 30\text{ bar}$; Nafion 115 ($127\ \mu\text{m}$) and Nafion 212 ($50.8\ \mu\text{m}$).
   - **Sources:** Bernt & Gasteiger (2016) *J. Electrochem. Soc.* 163 F3179; Rakousky et al. (2016) *J. Power Sources* 326 120; Masampally, Mitra & Runkana (2026) *Energy Convers. Manage.* 352 121110; Trinke et al. (2018) *J. Electrochem. Soc.* 165 F502.
2. **Degradation & Stack Lifetime Benchmarks (`pem_degradation_and_stack_lifetime_benchmarks.csv`):**
   - Voltage degradation rates $\dot{D}(i)$ ranging from $1.20\ \mu\text{V/h}$ at $0.5\text{ A/cm}^2$ up to $7.80\ \mu\text{V/h}$ at $3.0\text{ A/cm}^2$ under steady state, and $8.90\ \mu\text{V/h}$ under rapid wind ramp cycling.
   - Industrial OEM stack lifetime benchmarks: Nel Hydrogen (M-Series, 60,000–80,000 h), Plug Power (ProGen, 60,000–75,000 h), ITM Power (Neptune 2MW, 60,000–80,000 h), Siemens Energy (Silyzer 300, 80,000 h).
3. **Membrane Physical Specifications (`pem_membrane_physical_specifications.csv`):**
   - Nafion 115 vs 212 parameters: dry density ($1.98\text{ g/cm}^3$), equivalent weight ($1,100\text{ g/mol}$), equilibrium hydration ($\lambda = 21.5$), proton conductivity ($\sigma_m = 0.165\text{ S/cm}$ at 75°C), high-frequency resistance ($R_{\text{HFR}} = 0.077\ \Omega\cdot\text{cm}^2$), and hydrogen crossover permeability ($1.85 \times 10^{-11}\text{ mol/(cm}\cdot\text{s}\cdot\text{bar)}$).

---

### C. Cost Data & Indian Tender Benchmarks (`cost_data_and_tenders/`)
1. **Current Indian Cost Quotes (2024–2026) (`indian_green_hydrogen_capex_opex_benchmarks_2024_2026.csv`):**
   - **WACC:** **$10.05\%$** nominal ($70\%$ debt at $8.50\%$ interest, $30\%$ equity at $13.50\%$, $25.17\%$ tax rate).
   - **PEM Electrolyzer Stack:** ₹$4.80\text{ Cr/MW}$ (\$578/kW); replacement stack at year 11: ₹$2.20\text{ Cr/MW}$.
   - **Turnkey PEM Plant (with BoP & Rectifiers):** ₹$8.20\text{ Cr/MW}$ (\$988/kW).
   - **Utility Solar PV:** ₹$3.65\text{ Cr/MW}$ (\$440/kW); coastal mono-PERC/TOPCon.
   - **Coastal Wind Turbines:** ₹$6.60\text{ Cr/MW}$ (\$795/kW); IEC-S marine coated.
   - **LiFePO4 BESS:** ₹$1.35\text{ Cr/MWh}$ (\$163/kWh); 4-hour containerized system.
   - **Compression & 200 bar Storage:** ₹$0.95\text{ Cr/MW-eq}$.
   - **Seawater RO + EDI Water Desalination:** ₹$0.15\text{ Cr/MW-eq}$; OPEX ₹$45/\text{kL}$ ($\sim$₹$0.45/\text{kg H}_2$).
2. **Real Indian Tender Documents (`seci_and_iocl_tender_benchmarks.csv`):**
   - **SECI SIGHT Scheme (Tranche I, 2024):** 450,000 t/yr awards to Reliance (₹18.90/kg avg), Greenko (₹30.00/kg), ACME (₹30.00/kg), Welspun (₹20.00/kg).
   - **IOCL Panipat 10 KTA Tender (2024):** Winning commercial tariffs: ₹$280 - 340/\text{kg H}_2$ for 100% green supply to refinery gate.
3. **Sobol Sensitivity Analysis (`cost_parameters_and_sobol_sensitivity_guide.md`):**
   - Confirms that **WACC** ($S_i = 0.342$) and **PEM Electrolyzer CAPEX** ($S_i = 0.256$) govern over $60\%$ of total LCOH variance.

---

### D. Plant Specification Decisions (`plant_specifications/`)
- **Firm Demand:** **$500.0\text{ kg H}_2/\text{h}$** continuous ($12\text{ t/day}$, $4,380\text{ t/yr}$) for coastal refinery/fertilizer off-take (MRPL/MCF).
- **Supply Reliability:** **LPSP $\le 1.0\%$** ($\ge 99.0\%$ continuous firm availability).
- **Plant Boundary:** **100% Islanded (Zero Grid Connection)** to prevent open-access regulatory surcharges and guarantee green additionality.
- **Scope Inclusions:** PEMWE stacks (30 bar), downstream booster compression (30 to 200 bar), 12-hour cascade buffer storage ($6,000\text{ kg}$ capacity), and complete Seawater RO + EDI water treatment ($10.0\text{ L H}_2\text{O} / \text{kg H}_2$).

---

## 🛠️ Quick Start & Verification

### 1. Run Dataset Audit & Schema Check
```bash
python scripts/verify_data_package.py
```

### 2. Run Comparative Dispatch Simulation
```bash
python scripts/battery_first_vs_electrolyzer_first_dispatch.py
```

---

## 📜 Citation

If you use this dataset or associated scripts in your research, please cite:
```bibtex
@misc{chemignite_coastal_h2_dataset_2026,
  author = {Krishnendu and Aggarwal, Arav},
  title = {Multi-Year Meteorological, Electrochemical, and Techno-Economic Benchmark Dataset for Coastal Green Hydrogen Plants in India},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/Krishnendu409/coastal-green-hydrogen-firm-supply-data-package}}
}
```

## ⚖️ License
This project and all constituent datasets are licensed under the [MIT License](LICENSE).
