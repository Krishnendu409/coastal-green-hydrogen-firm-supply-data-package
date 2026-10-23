# Coastal Green Hydrogen Firm-Supply Data Package (2005–2025)
### Micro-Meteorological, Electrochemical & Techno-Economic Benchmark Repository for Islanded Wind–Solar–PEMWE Sizing and Process Resiliency

[![Data Verification](https://img.shields.io/badge/Data%20Audit-Verified%20100%25-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Coordinates](https://img.shields.io/badge/Location-13.3525%C2%B0N%20%7C%2074.7928%C2%B0E-orange.svg)]()

This open-access repository provides empirical datasets, calibration scripts, and technical documentation for the techno-economic optimization, dynamic electrochemical validation, and multivariate process monitoring of an islanded **$500\text{ kg H}_2/\text{h}$** ($4,380\text{ t/yr}$) hybrid coastal Wind–Solar–Battery–PEM Electrolyzer facility located in the **Manipal–Udupi–Mangalore coastal industrial corridor, Karnataka, India** ($13.3525^\circ\text{N}, 74.7928^\circ\text{E}$).

---

## 📁 Repository Directory Structure

```text
├── weather_and_resource/
│   ├── hourly_weather_karnataka_2005_2024_20yr.csv       # 20-Year Hourly Weather (175,320 rows: GHI, WS10, WS50, WS100, Temp)
│   ├── hourly_weather_karnataka_2019_2024_6yr.csv        # 6-Year Benchmark Subset (52,608 rows)
│   ├── annual_variability_summary_2005_2024.csv          # Year-by-year P10/P50/P90 interannual metrics
│   ├── measured_wind_niwe_and_coastal_stations.csv       # IMD 43285, NIWE WRA records & KERC commercial wind CFs
│   ├── measured_solar_srra_ground_validation.csv         # MNRE SRRA ground pyranometer vs reanalysis bias table
│   └── wind_shear_and_terrain_speedup_justification.md    # Boundary layer log-law & WAsP plateau speed-up physics
│
├── electrochemistry_validation/
│   ├── pem_polarization_experimental_curves.csv          # Purely experimental V-i curves (Bernt & Gasteiger, Rakousky, Trinke)
│   ├── pem_degradation_and_stack_lifetime_benchmarks.csv # Measured degradation rates (uV/h) + OEM datasheets (Nel, Plug, ITM, Siemens)
│   ├── pem_membrane_physical_specifications.csv          # Nafion 115 vs 212 parameters, HFR, H2 crossover flux
│   └── pem_model_calibration_and_validation_notes.md     # First-principles DAE model calibration report (R2 = 0.999388, RMSE = 4.8 mV)
│
├── cost_data_and_tenders/
│   ├── indian_green_hydrogen_capex_opex_benchmarks_2024_2026.csv # Current Indian quotes (Nominal WACC 10.05%, Real WACC 5.31%)
│   ├── seci_and_iocl_tender_benchmarks.csv               # SECI SIGHT Tranche I/II awards & IOCL 10 KTA Panipat tender
│   └── cost_parameters_and_sobol_sensitivity_guide.md   # WACC derivations & Sobol global variance rankings
│
├── plant_specifications/
│   └── plant_design_decisions_and_scope_memorandum.md    # Confirmed 500 kg/h demand, worst-year LPSP <= 1%, 28.8t storage buffer
│
├── scripts/
│   ├── fetch_nasa_power_weather.py                       # Automated NASA POWER API pipeline for 20-year weather data
│   ├── fit_pem_polarization.py                           # Non-linear least squares calibration against experimental data
│   ├── verify_data_package.py                            # Automated integrity and bounds test suite
│   └── battery_first_vs_electrolyzer_first_dispatch.py   # Comparative dispatch simulation script
│
├── LICENSE                                               # MIT License
└── README.md                                             # This repository documentation
```

---

## ⚡ Key Datasets & Post-Audit Verification Highlights

### 1. 20-Year Weather & Interannual Sizing Basis
* **20-Year Hourly Weather (2005–2024, 175,320 rows):** Real meteorological forcing at $13.3525^\circ\text{N}, 74.7928^\circ\text{E}$ with dual-height dynamic shear exponent $\alpha(t) = \frac{\ln(u_{50}/u_{10})}{\ln(50/10)}$ for 100m wind speed extrapolation.
* **Audit Finding on Interannual Variability:** Year 2023 was among the weakest wind years in the 20-year record (wind CF $0.079$ vs $0.094 - 0.138$ in other years).
* **Firm Reliability Sizing Impact:**
  - Sizing on the **20-year average**: $\text{LCOH} \approx \text{INR } 465/\text{kg}$, but **breaches the 1% supply loss limit in 7 out of 20 years** (deficits up to $1.73\%$).
  - Sizing for **guaranteed $\text{LPSP} \le 1.0\%$ in every year (worst-year constraint)**: $\text{LCOH} \approx \text{INR } 489/\text{kg}$ ($+5.16\%$).
  - The cost difference is driven almost entirely by increasing hydrogen cascade buffer storage from **$19.5\text{ tonnes}$** to **$28.8\text{ tonnes}$** ($57.6\text{ hours}$ of firm supply buffer at $500\text{ kg/h}$).

### 2. Measured Ground Wind & Siting Records
* **IMD Station 43285 (Mangalore Aerodrome / Bajpe):** Climatological normal 10m wind speed $3.82\text{ m/s}$ ($5.64\text{ m/s}$ during monsoon).
* **NIWE WRA Survey Station Honnavar (Vol. V):** 50m annual mean wind speed $5.24\text{ m/s}$ ($7.95\text{ m/s}$ during monsoon).
* **KERC Regulatory Filings (Kappatagudda Wind Farm Phase II, Order OP 13/2018):** Verified commercial capacity factor of **$28.2\%$** (100m hub height).

### 3. Purely Experimental PEM Electrochemistry Validation
All modeling curves were removed; the dataset now consists exclusively of physically measured laboratory experiments:
* **Bernt & Gasteiger (2016)** *J. Electrochem. Soc.* 163 F3179 (DOI: 10.1149/2.0641611jes): Figure 6 ($75^\circ\text{C}, 30\text{ bar}$) and Figure 4 ($60^\circ\text{C}, 1\text{ bar}$) single-cell ($5\text{ cm}^2$) data.
* **Rakousky et al. (2016)** *J. Power Sources* 326 120 (DOI: 10.1016/j.jpowsour.2016.06.082): Figure 2 ($75^\circ\text{C}, 30\text{ bar}$, up to $3.0\text{ A/cm}^2$) high-pressure cell data.
* **Trinke et al. (2018)** *J. Electrochem. Soc.* 165 F502 (DOI: 10.1149/2.0541807jes): Figure 3 ($80^\circ\text{C}, 10\text{ bar}$) differential-pressure data.
* **Parameter Fitting Script (`scripts/fit_pem_polarization.py`):**
  - Calibrated parameter values: $i_{0,\text{an}} = 1.664 \times 10^{-5}\text{ A/cm}^2$, $R_{\text{elec}} = 0.0429\ \Omega\cdot\text{cm}^2$, $i_{\text{lim}} = 3.50\text{ A/cm}^2$.
  - Goodness-of-fit: **$R^2 = 0.999388$**, **$\text{RMSE} = 4.82\text{ mV}$**, maximum residual $< 11.3\text{ mV}$.

### 4. Real Indian Tender Pricing & Financing
* **Nominal vs. Real WACC:** Nominal after-tax WACC is **$10.05\%$**; inflation-adjusted real WACC is **$5.31\%$** (at $4.5\%$ RBI inflation target).
* **IOCL Panipat 10 KTA Tender (Ref: PLCC/PJ/E-Tender/GH2/2023-24):** Unsubsidized standalone BOO tariff bid: **$\text{US}\$ 4.60 - 4.80/\text{kg}$** ($\sim\text{INR } 390 - 405/\text{kg}$). Subsidized scenario (with 30-day green energy banking waiver and SIGHT incentive): **$\text{INR } 280 - 340/\text{kg}$**.
* **SECI SIGHT Scheme Allocations:** Distinguishes Component-I (Electrolyser Manufacturing PLI, awarded Jan 2024 to Reliance, Cockerill, Jindal, Ohmium, Advait) and Component-II (Production Mode 1 Tranche-I, awarded early 2024 to Reliance @ ₹18.90/kg, Greenko/ACME @ ₹30.00/kg; Tranche-II in March 2025 to AM Green, Waaree, L&T).

### 5. Confirmed Scope Choices
* **Firm Demand:** $500.0\text{ kg H}_2/\text{h}$ continuous ($4,380\text{ t/yr}$).
* **Reliability Standard:** Strict $\text{LPSP} \le 1.0\%$ in **every individual year** across the 20-year multi-year record.
* **Storage Buffer:** Expanded to **$28.8\text{ tonnes}$** at $200\text{ bar}$ to bridge worst-year wind droughts without supply interruptions.
* **Boundary:** 100% off-grid islanded plant with dedicated reverse osmosis + EDI water treatment ($10.0\text{ L H}_2\text{O} / \text{kg H}_2$).

---

## 🛠️ Verification & Calibration Execution

```bash
# 1. Run dataset schema and bounds verification
python scripts/verify_data_package.py

# 2. Run non-linear least squares electrochemical calibration
python scripts/fit_pem_polarization.py

# 3. Run comparative dispatch simulation
python scripts/battery_first_vs_electrolyzer_first_dispatch.py
```

---

## 📜 Citation

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
