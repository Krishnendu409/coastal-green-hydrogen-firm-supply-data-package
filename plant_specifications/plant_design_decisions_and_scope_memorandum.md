# Formal Engineering Specification & Plant Boundary Memorandum (Revision 3 - Post-Audit)

**Document ID:** MEMO-ENG-2026-H2-01-REV3  
**Project:** Coastal Hybrid Wind–Solar–PEMWE Firm Green Hydrogen Production Plant  
**Site Location:** Coastal Karnataka Corridor ($13.3525^\circ\text{N}, 74.7928^\circ\text{E}$), Udupi–Manipal–Mangalore belt  
**Authors:** Krishnendu & Arav Aggarwal, Manipal Institute of Technology (MIT), MAHE  

---

## 1. Production Demand & Sizing Basis Decisions

### 1.1 Firm Demand Rate: **500.0 kg/h Continuous (CONFIRMED)**
- **Baseline Off-Take:** Continuous, un-curtailed supply of **$500.0\text{ kg H}_2/\text{h}$** ($138.89\text{ g/s}$).
- **Annual Production:** $4,380\text{ metric tonnes/year}$ ($4.38\text{ KTA}$).
- **Industrial Off-Taker Alignment:** Sized to match a dedicated slipstream at the **Mangalore Refinery and Petrochemicals Limited (MRPL)** hydrodesulfurization block or the **Mangalore Chemicals & Fertilizers (MCF)** ammonia loop.

### 1.2 Decision on Sizing Reliability Basis: **Worst-Year Strict Constraint (CONFIRMED)**
**Decision:** The plant sizing MUST satisfy **$\text{LPSP} \le 1.0\%$ in EVERY individual year** across the multi-year meteorological record, rather than merely meeting $\le 1.0\%$ on a multi-year average.

#### Clarification on Meteorological Risk Years:
- **Year 2023 (Wind Drought):** 2023 was the weakest wind year in the 20-year record (wind CF $0.079$ vs $0.094 - 0.138$ in normal years), resulting in $\text{LPSP} = 0.93\%$ in the baseline simulation.
- **Year 2024 (Solar Monsoon Collapse & Max Deficit Breach):** **Year 2024 is the worst-case supply breach year**, with annual solar GHI collapsing to **$1,796.0\text{ kWh/m}^2/\text{yr}$** (the lowest in the 20-year record) due to an extended Southwest Monsoon. Under a 20-year mean sizing, **2024 experiences a supply deficit of $1.73\%$** ($151\text{ hours}$ of unserved hydrogen).
- **20-Year Mean Sizing Basis:** $\text{LCOH} \approx \text{INR } 465/\text{kg H}_2$. However, **7 out of 20 years breach the 1% loss of supply target**, reaching deficits up to $1.73\%$ in 2024.
- **Worst-Year Sizing Basis ($\text{LPSP} \le 1.0\%$ in all 20 years):** $\text{LCOH} \approx \text{INR } 489/\text{kg H}_2$ ($+\text{INR } 24/\text{kg}$, $+5.16\%$).
- **Physical Driver of Cost Delta:** The $+5.16\%$ cost premium is driven almost entirely by expanding hydrogen buffer storage from **$19.5\text{ tonnes}$** to **$28.8\text{ tonnes}$** ($57.6\text{ hours}$ of continuous $500\text{ kg/h}$ demand). Installed generation and electrolyzer capacities remain largely stable.

---

## 2. Plant Scope & Battery Dispatch Strategy

### 2.1 Islanded Boundary (Zero Grid Connection)
- Confirmed 100% off-grid islanded facility.
- Avoids Karnataka Open Access cross-subsidy surcharges (CSS) and additional surcharges (AS) which add INR $2.20 - 3.40/\text{kWh}$ to wheeling power.
- Guarantees strict zero-emission green hydrogen certification under European RED II/III and Indian National Green Hydrogen Mission rules without fossil grid blending.

### 2.2 Balance of Plant (BoP) Inclusions
1. **Electrolyzer Core:** High-pressure PEMWE operating at **$30.0\text{ bar}$** cathode pressure and $1.0\text{ bar}$ anode pressure, bypassing first-stage mechanical compression.
2. **Buffer Hydrogen Storage:** Cascade pressurized steel cylinders/tube trailers operating at **$200\text{ bar}$** with **$28.8\text{ tonnes}$ capacity** ($57.6\text{ hours}$ firm buffer).
3. **Booster Compression:** Diaphragm compressor elevating hydrogen from $30\text{ bar}$ to $200\text{ bar}$ ($1.28\text{ kWh/kg H}_2$).
4. **Water Treatment:** Seawater Reverse Osmosis (SWRO) intake followed by two-pass Electrodeionization (EDI). Specific consumption: $10.0\text{ L H}_2\text{O} / \text{kg H}_2$. Cost contribution: $\sim\text{INR } 0.45/\text{kg H}_2$.

---

## 3. Dissemination Plan & Recalibration of Paper Claims

To ensure scientific rigor and peer-review integrity, all claims have been recalibrated:

| Manuscript Section | Original Draft Claim (Dropped) | Recalibrated & Defensible Claim (Adopted) |
| :--- | :--- | :--- |
| **Computational Footprint** | "Reduces computational carbon/energy footprint by 99.38%" | "Replaces iterative DAE evaluations during evolutionary search with a compact 4,900-parameter neural network surrogate, accelerating 8,760-hour annual evaluations by over $10^3\times$." |
| **Surrogate Architecture** | "Green-MLP eliminates need for rigorous physical modeling" | "Green-MLP serves as an exploratory screening surrogate, with all Pareto-optimal knee-point designs verified against exact physical differential-algebraic equations (DAEs)." |
| **Electrochemical Validation** | "Direct experimental validation against proprietary test stacks" | "Physics-based semi-empirical DAE model parametrized from published literature constants, accompanied by parametric sensitivity sweeps across stack resistance ($R_{\text{elec}}$) and exchange current density ($i_0$)." |
| **Process Monitoring** | "Early-warning detection 52 hours in advance with 100% accuracy" | "Multivariate statistical process monitoring (Hotelling's $T^2$ and Squared Prediction Error $Q$) identifies cross-variable correlation breakdowns during simulated membrane dehydration and flooding faults, outperforming static univariate voltage thresholds." |
| **Wind Resource Siting** | "Empirical 1.28x / 1.58x coastal speed-up multiplier" | "Dual-height shear extrapolation validated against IMD Mangalore/Bajpe anemometry, with coastal speed-up analyzed as an explicit parametric sensitivity range ($1.00\times - 1.25\times$) derived via IEC 61400-1 Annex B." |
