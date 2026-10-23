# Electrochemical Model Calibration & Validation Notes (Revision 3 - Post-Audit)

## 1. Decision on Paper Framing: Unvalidated Semi-Empirical Model (Option 2)

**Decision for Manuscript:** In accordance with rigorous peer-review standards, the manuscript will **formally describe the electrochemical stack model as a physics-based, semi-empirical DAE model parametrized from published literature constants, rather than claiming empirical validation against experimental stack hardware.**

### Recommended Sensitivity Sweeps for the Paper:
To demonstrate model robustness without overstating experimental validation, the paper will present sensitivity sweeps across the core electrochemical uncertainty envelope:
1. **Interfacial Electronic/Contact Resistance:** $R_{\text{elec}} \in [0.020, 0.060]\ \Omega\cdot\text{cm}^2$ (representing titanium PTL passivation and contact degradation over time).
2. **Anode Exchange Current Density:** $i_{0,\text{an}} \in [1.5 \times 10^{-5}, 4.0 \times 10^{-5}]\text{ A/cm}^2$ (representing catalyst surface roughness and dissolution).
3. **Impact on Plant Sizing & LCOH:** Shows how LCOH shifts by $\pm \text{INR } 12 - 18/\text{kg H}_2$ across this range without changing the Pareto knee-point architecture.

---

## 2. Corrected Thermodynamic Saturation Vapor Pressure Formulation

In earlier code drafts, an atmospheric approximation with an empirical prefactor (`0.0312`) was erroneously used, yielding an unphysical saturation vapor pressure of $1.974\text{ bar}$ at $75^\circ\text{C}$ (which exceeds atmospheric pressure below water's boiling point). 

This has been corrected to the **exact NIST Antoine Thermodynamic Equation** for liquid water ($273.15 - 373.15\text{ K}$):

$$\log_{10}(P_{\text{sat}} / \text{bar}) = A - \frac{B}{T - C}$$
Where $A = 5.40221$, $B = 1838.675$, and $C = 31.737$ (temperature $T$ in Kelvin).

### Physical Activities at $75^\circ\text{C}$ ($348.15\text{ K}$):
- Water Saturation Vapor Pressure: $P_{\text{sat}} = 10^{-0.40878} = \mathbf{0.3901\text{ bar}}$ ($39.01\text{ kPa}$).
- Effective Cathode Hydrogen Activity: $a_{\text{H}_2} = P_{\text{cat}} - P_{\text{sat}} = 30.0 - 0.3901 = \mathbf{29.6099\text{ bar}}$.
- Effective Anode Oxygen Activity: $a_{\text{O}_2} = P_{\text{an}} - P_{\text{sat}} = 1.0 - 0.3901 = \mathbf{0.6099\text{ bar}}$ (un-clamped).
- Reversible Nernst Potential ($E_{\text{rev}}$):
  $$E_{\text{rev}} = E_0(T) + \frac{R T}{2 F} \ln\left[ a_{\text{H}_2} \cdot a_{\text{O}_2}^{0.5} \right] = 1.1840\text{ V} + 0.0471\text{ V} = \mathbf{1.2311\text{ V}}$$

---

## 3. Direct Primary Literature Sources & Open-Access Links

For researchers wishing to digitize raw curves directly from source publications:

1. **Bernt & Gasteiger (2016)**  
   *Title:* "Influence of Operating Conditions and MEA Design on the Performance of a Proton Exchange Membrane Water Electrolyzer"  
   *Journal:* *Journal of The Electrochemical Society*, 163(11) F3179–F3189 (2016)  
   *DOI:* [10.1149/2.0641611jes](https://doi.org/10.1149/2.0641611jes)  
   *Open-Access PDF:* [https://iopscience.iop.org/article/10.1149/2.0641611jes/pdf](https://iopscience.iop.org/article/10.1149/2.0641611jes/pdf) (Creative Commons CC BY 4.0)  
   *Figures:*  
   - **Figure 6:** Influence of cathode pressure ($1\text{ bar}$ vs $30\text{ bar}$) at $75^\circ\text{C}$ on Nafion 115 ($127\ \mu\text{m}$, $1.5\text{ mg/cm}^2\ \text{IrO}_2$). **Note: Measured experimental points terminate at $2.0\text{ A/cm}^2$.**  
   - **Figure 4:** Atmospheric baseline curves at $60^\circ\text{C}, 70^\circ\text{C}, 80^\circ\text{C}$.

2. **Rakousky et al. (2016)**  
   *Title:* "Analysis of degradation mechanisms in polymer electrolyte membrane water electrolyzers"  
   *Journal:* *Journal of Power Sources*, 326, 120–128 (2016)  
   *DOI:* [10.1016/j.jpowsour.2016.06.082](https://doi.org/10.1016/j.jpowsour.2016.06.082)  
   *Figures:*  
   - **Figure 2 & Figure 3:** DLR test bench ($25\text{ cm}^2$), $75^\circ\text{C}$, $30\text{ bar}$ cathode, measured up to $2.0\text{ A/cm}^2$ with $1,000\text{ h}$ durability cycling.

3. **Trinke, Hanke, Bensmann & Hanke-Rauschenbach (2018)**  
   *Title:* "Hydrogen Permeation in Proton Exchange Membrane Water Electrolysis"  
   *Journal:* *Journal of The Electrochemical Society*, 165(7) F502–F513 (2018)  
   *DOI:* [10.1149/2.0541807jes](https://doi.org/10.1149/2.0541807jes)  
   *Open-Access PDF:* [https://iopscience.iop.org/article/10.1149/2.0541807jes/pdf](https://iopscience.iop.org/article/10.1149/2.0541807jes/pdf)  
   *Figures:*  
   - **Figure 3:** Differential-pressure polarization and hydrogen-in-oxygen crossover flux at $80^\circ\text{C}$, $10\text{ bar}$ and $30\text{ bar}$.

---

## 4. Honest Holdout Cross-Validation Results

Using [`scripts/fit_pem_polarization.py`](../scripts/fit_pem_polarization.py) with an honest **70% Train / 30% Holdout Test split** on the 12 physically measured points from Bernt & Gasteiger Fig. 6 ($0.05$ to $2.00\text{ A/cm}^2$):

- **Fitted Anode Exchange Current Density ($i_{0,\text{an}}$):** $2.805 \times 10^{-5}\text{ A/cm}^2$ ($\log_{10} i_0 = -4.552$)
- **Fitted Interfacial Resistance ($R_{\text{elec}}$):** $0.0624\ \Omega\cdot\text{cm}^2$
- **Total Area-Specific Resistance ($R_{\text{tot}} = R_{\text{mem}} + R_{\text{elec}}$):** $0.1314\ \Omega\cdot\text{cm}^2$
- **Holdout Test $R^2$ (Unseen points):** **$0.975602$**
- **Holdout Test RMSE:** **$9.98\text{ mV}$**
- **Full Dataset $R^2$:** **$0.997113$**
- **Full Dataset RMSE:** **$7.45\text{ mV}$**
