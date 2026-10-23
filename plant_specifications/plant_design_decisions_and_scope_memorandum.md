# Formal Engineering Specification & Plant Boundary Memorandum (Revision 2 - Post-Audit)

**Document ID:** MEMO-ENG-2026-H2-01-REV2  
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

#### Engineering & Contractual Rationale:
1. **Refinery Process Safety & Continuity:** Chemical refineries cannot tolerate a 1.73% supply deficit (~151 hours of unmet hydrogen demand) in poor renewable years (such as 2023). Unplanned hydrogen starvation triggers severe plant upsets, emergency flaring, catalyst coking in hydrotreaters, or requires firing expensive backup grey hydrogen units.
2. **Techno-Economic Trade-Off Analysis:**
   - **20-Year Mean Sizing Basis:** $\text{LCOH} \approx \text{INR } 465/\text{kg H}_2$. However, **7 out of 20 years breach the 1% loss of supply target**, reaching deficits as high as $1.73\%$.
   - **Worst-Year Sizing Basis ($\text{LPSP} \le 1.0\%$ in all 20 years):** $\text{LCOH} \approx \text{INR } 489/\text{kg H}_2$ ($+\text{INR } 24/\text{kg}$, $+5.16\%$).
   - **Physical Driver of Cost Delta:** The cost premium is almost entirely driven by increasing hydrogen buffer storage from **$19.5\text{ tonnes}$** to **$28.8\text{ tonnes}$** ($57.6\text{ hours}$ of continuous $500\text{ kg/h}$ demand). Installed generation and electrolyzer capacities remain largely stable.
   - **Conclusion:** A $5.16\%$ levelized cost premium to guarantee $99\%$ firm supply even in the worst historical weather year is economically compelling and essential for bankable industrial take-or-pay supply contracts.

---

## 2. Plant Scope & Battery Dispatch Strategy

### 2.1 Islanded Boundary (Zero Grid Connection)
- Confirmed 100% off-grid islanded facility.
- **Regulatory Rationale:** Avoids Karnataka Open Access cross-subsidy surcharges (CSS) and additional surcharges (AS) which add INR $2.20 - 3.40/\text{kWh}$ to wheeling power.
- **Environmental Additionality:** Guarantees strict zero-emission green hydrogen certification under European RED II/III and Indian National Green Hydrogen Mission rules without fossil grid blending.

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
| **Process Monitoring** | "Early-warning detection 52 hours in advance with 100% accuracy" | "Multivariate statistical process monitoring (Hotelling's $T^2$ and Squared Prediction Error $Q$) identifies cross-variable correlation breakdowns during simulated membrane dehydration and flooding faults, outperforming static univariate voltage thresholds." |
| **Wind Resource Siting** | "Empirical 1.28x / 1.58x coastal speed-up multiplier" | "Dual-height shear extrapolation validated against IMD Mangalore/Bajpe anemometry and KERC commercial wind farm capacity factors (28.2%), with terrain escarpment acceleration derived via IEC 61400-1 Annex B." |
