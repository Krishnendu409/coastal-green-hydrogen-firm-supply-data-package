# Authorship, AI-Assistance Declaration & Submission Memorandum

---

## 1. Authorship Details & Affiliations

| Author | Role | Affiliation | Contact Email |
| :--- | :--- | :--- | :--- |
| **Krishnendu** | **Lead Author** (Process systems modeling, surrogate formulation, NSGA-II optimization, fault monitoring algorithms, manuscript drafting) | Department of Computer Science & Engineering, Manipal Institute of Technology, Manipal Academy of Higher Education, Manipal, Karnataka 576104, India | `krishnendu.official409@gmail.com` |
| **Arav Aggarwal** | **Co-Author** (Renewable resource siting, GIS coastal hydrology, environmental lifecycle metrics, techno-economic model verification) | Department of Civil Engineering, Manipal Institute of Technology, Manipal Academy of Higher Education, Manipal, Karnataka 576104, India | `arav.aggarwal@learner.manipal.edu` |

### Institutional Context & Evaluator Alignment
This research is developed for presentation at **CHEMIGNITE 2026 (ASPIRE 2026)**, hosted by the Department of Chemical Engineering and the IIChE Student Chapter at MIT Manipal. The methodological foundation directly aligns with the research domains of the distinguished session evaluators:
- **Prof. Kishalay Mitra** (Head of GOKUL Lab, IIT Hyderabad) — *Pioneering green surrogate modeling, multi-objective Pareto optimization under uncertainty, and high-current-density PEM electrolysis.*
- **Dr. Muddu Madakyaru** (Professor of Chemical Engineering, MIT Manipal) — *Pioneering multivariate statistical process monitoring (PCA $T^2$ and $Q$/SPE) and nonlinear process control.*

---

## 2. Declaration of Generative AI and AI-Assisted Technologies

The authors provide the following disclosure, formatted in full alignment with the **Elsevier Publishing Ethics** and **IEEE Author Center Generative AI Guidelines**:

> **Declaration of Generative AI and AI-Assisted Technologies:**  
> *"During the development of this research, the authors utilized Google Antigravity (DeepMind Advanced Agentic Coding) as an AI pair-programming assistant. The AI tool assisted extensively with numerical code scaffolding, simulation pipeline optimization (Numba DAE compilation), surrogate neural network ablation routines, multivariate PCA/EWMA benchmark scripting, literature cross-referencing, and draft text polishing. The human authors formulated the research problem, established the engineering constraints and baseline trade-offs, directed all computational sweeps, reviewed the mathematical consistency of the underlying physical equations, and take full responsibility for the manuscript's findings, interpretations, and integrity."*

---

## 3. Public Open-Science Repositories & Zenodo Archiving Protocol

To ensure $100\%$ scientific transparency, full reproducibility, and FAIR data compliance, the project is structured across two dedicated public repositories:

1. **Simulation Code & Model Pipeline Repository:**  
   - URL: [`https://github.com/Krishnendu409/coastal-wind-solar-pem-h2-optimization`](https://github.com/Krishnendu409/coastal-wind-solar-pem-h2-optimization)
   - License: MIT License
   - Contents: First-principles DAE model, LLVM-compiled Numba simulator, Green-MLP surrogate training and ablation scripts, constrained NSGA-II optimizer, and load-compensated PCA/EWMA fault monitoring suite.
2. **Micro-Meteorological & Empirical Benchmark Data Package:**  
   - URL: [`https://github.com/Krishnendu409/coastal-green-hydrogen-firm-supply-data-package`](https://github.com/Krishnendu409/coastal-green-hydrogen-firm-supply-data-package)
   - License: Creative Commons Attribution 4.0 International (CC-BY-4.0)
   - Contents: 20-year hourly weather datasets (ECMWF ERA5 & NASA POWER MERRA-2), primary experimental literature polarization benchmarks, and Indian tender-grounded techno-economic parameters.
3. **Zenodo DOI Protocol (No Pre-Emptive Citations):**  
   - Both repositories contain `.zenodo.json` files pre-configured for automated GitHub-Zenodo release archiving.
   - **Important Scientific Protocol:** No placeholder or synthetic DOI shall be cited in the manuscript text. Until the author activates the repository webhook on `zenodo.org` to mint a live resolving DOI, the codebase and data package must be cited directly via their persistent GitHub repository URLs and tagged release references (`v1.0.1`).

---

## 4. Target Venue, Length & Submission Strategy

1. **Immediate Presentation & Competition Target (October 2026):**
   - **Venue:** **CHEMIGNITE 2026 (ASPIRE 2026)** — National Symposium on Clean Energy, Process Systems Engineering & Sustainability.
   - **Dates:** Idea/Paper submission by October 25, 2026; Oral Presentation on October 29, 2026 at Sir M. Vishveshwaraiah Seminar Hall, Academic Block 2, MIT Manipal.
   - **Deliverables:** Submission Abstract (concise 300 words + 1-page technical summary), Presentation Slides (`PRESENTATION_SLIDES.html`), and Full Reference Manuscript.
2. **Target Publication Journal (Post-Conference Archival):**
   - **Primary Journal Target:** **Elsevier *Computers & Chemical Engineering*** (or *Applied Energy* / *International Journal of Hydrogen Energy*).
   - **Format & Length:** Standard IEEE / Elsevier double-column research article (currently 13 pages, ~9,800 words), fully self-contained with 6 publication-grade figures, 4 structured tables, and 3 step-by-step calculation walkthrough boxes.
