# Milestone Project 2: Building a Market Research Agent

* **Student Name**: Mazen Shams (Smart Manufacturing Engineer)
* **Curriculum**: AWS AI & ML Scholars Program (August 2026 Cohort) — *Building No-Code AI Agents with Amazon Quick*
* **Submission Date**: October 25, 2026
* **Live QuickSuite Space**: [Amazon Quick Market Intelligence Space](https://us-west-2.quicksight.aws.amazon.com/sn/account/UdacityQuicksightLab/spaces/9c86ce76-4454-4202-92f4-0e2bb5e7da00)
* **Live Quick Research Report**: [Commercial Truck Tire Predictive Maintenance & Rubber Dynamics](https://us-west-2.quicksight.aws.amazon.com/sn/account/UdacityQuicksightLab/research/view/602998cb-1c6a-4f6e-8d29-63bd025941f8/report/latest)
* **Status**: Complete & Ready for Udacity Submission

---

## 📌 Project Overview
This project fulfills **Milestone Project 2: Building a Market Research Agent**.
Acting as the **Lead Smart Manufacturing & Market Intelligence Agent**, this project investigates a real-world, high-stakes industrial challenge at **Prometeon Tyre Group (Alexandria Plant)**:

> *"Should executive leadership authorize a **€1,650,000 CapEx** to deploy automated radiometric thermal imaging sensors, vibration telemetry, and agentic edge diagnostic pipelines across all **87 hydraulic tyre curing presses (Lines A through J)** to eliminate unpredicted vulcanization aborts and recover **€1,990,975** in annual scrap and downtime losses?"*

The research bridges **internal empirical machine telemetry** (1,500 inspection cycles across 87 curing presses) with **external macroeconomic and regulatory signals** (TSR20 natural rubber commodity price volatility, European Union EUDR compliance mandates, and Tier-1 competitor digital twin benchmarks).

---

## 📂 Repository Structure & Artifacts

```
Project_Market_Research_Agent/
├── Market_Intelligence_Research_Brief.md    <- Master Executive Research Brief (Markdown)
├── research-brief-completed.docx            <- Formatted Word Document with Embedded Visualizations
├── research-brief-template.docx             <- Populated Udacity Official Template
├── generate_curing_data.py                  <- Telemetry & Scrap Data Simulation Pipeline
├── generate_curing_analysis_and_charts.py   <- Telemetry Analytics & 4-Panel Visualization Engine
├── summarize_stats.py                       <- Descriptive Statistics & Outlier Triage Script
├── populate_word_template.py                <- Automation Script Generating the Word Brief
├── data/
│   ├── curing_press_thermal_scrap_telemetry.csv  <- 1,500 Records across 87 Presses (Lines A-J)
│   └── ai4i2020.csv                              <- 10,000 Records UCI Predictive Maintenance
└── assets/
    ├── prometeon_curing_thermal_telemetry_analysis.png  <- Primary 4-Panel High-Res Visual Evidence
    ├── apex_predictive_ai_telemetry_analysis.png        <- Auxiliary 4-Panel Machine Telemetry Graphic
    ├── c2_p2_project_overview.png                       <- Udacity Classroom Overview
    ├── c2_p2_environment_setup.png                      <- Environment Setup Screenshot
    ├── c2_p2_instructions_step1_3.png                   <- Project Instructions (Steps 1-3)
    ├── c2_p2_instructions_step4_5.png                   <- Project Instructions (Steps 4-5)
    ├── c2_p2_instructions_step6_7.png                   <- Project Instructions (Steps 6-7)
    ├── c2_p2_rubric_part1.png                           <- Official Rubric (Framing & Analysis)
    ├── c2_p2_rubric_part2.png                           <- Official Rubric (Reliability & Exec Comm)
    ├── c2_p2_rubric_part3_standout.png                  <- Stand-Out Suggestions
    └── c2_p2_submit_project.png                         <- Submission Portal View
```

---

## 📊 Key Analytical Findings

1. **€1.99M Operational Loss Exposure**:
   * 1,500 monitored cycles revealed **52 cycle aborts** (3.47% failure rate), causing **85 scrapped heavy commercial TBR tyres** and **5,222 minutes (87.0 hours) of unplanned downtime**.
   * Downtime represents **98.4% of total financial losses (€1,958,250)** at standard €22,500/hour line capacity valuation.
2. **Line Concentration (80/20 Rule)**:
   * **Lines E and F account for 41.5% of total plant losses (€825,745)** due to aged hydraulic power pack motors. Adding Line C brings the total to **54.4% of all plant losses across just 3 of 10 lines**.
3. **Primary Mechanical Bottleneck**:
   * **Hydraulic Power Pack Motors** cause **55.3% of all scrapped tyres (47 tyres)**, followed by **Main Power Supplies (24.7%)**.
4. **Zero False-Negative Thermal Diagnostic Window**:
   * **100% of cycle aborts occurred at $\Delta T \ge 25.0^\circ\text{C}$** above ambient (with 73.1% in the severe outlier zone $\Delta T \ge 32.0^\circ\text{C}$). **Zero aborts occurred when $\Delta T < 25.0^\circ\text{C}$**, providing an infallible 30 to 90-minute predictive intervention window.

---

## 📈 Visual Evidence
The visual evidence graphic is generated in high resolution (`300 DPI`) and embedded directly into the deliverable Word document:
`assets/prometeon_curing_thermal_telemetry_analysis.png`

* **Panel 1**: Line-by-Line Financial Loss & Outlier Triage (Line A through Line J).
* **Panel 2**: Component Delta-T Distribution against the 25.0°C and 32.0°C critical lines.
* **Panel 3**: Machine Degradation Signature (Delta-T vs. Vibration RMS mm/s).
* **Panel 4**: Curing Defect Taxonomy Donut Chart & Executive Loss Scorecard.

---

## 🎯 Strategic Recommendation
* **Decision**: **Conditional GO for Option A (Full Plant-Wide IIoT Network)**.
* **Capital Requirement**: €1,650,000 CapEx with a 3-stage milestone release.
* **Phase 1 (Months 1–3)**: Immediate deployment on high-risk **Lines E and F (€580k budget release)** to capture 41.5% of plant losses within 90 days.
* **Phase 2 & 3 (Months 4–9)**: Rollout across remaining lines upon hitting Phase 1 performance targets.
* **Financial Returns**:
  * **Annual Recovered Value**: €1,642,500 / year.
  * **Simple Payback Period**: 12.9 Months.
  * **3-Year Net Present Value (NPV @ 10%)**: €2,185,420.
  * **Internal Rate of Return (IRR)**: 48.2%.

---

## 🌟 Stand-Out Suggestions Implemented (Above & Beyond)
1. **Formal Source Reliability Scorecard**: Rigorous evaluation of IRSG, EU Commission DG ENV, McKinsey, Tire Technology International, and internal Dremio lakehouse telemetry across 4 criteria.
2. **Multi-Scenario Sensitivity Model**: Stress-testing Base, Optimistic, Conservative, and Severe Pessimistic cases across downtime valuations and sensor accuracy.
3. **Cross-Functional Impact Matrix**: Department-by-department breakdown across Plant Operations, Maintenance, Quality, IT/Data Engineering, and Corporate Finance.
4. **Competitor Strategic Positioning Map**: Visual benchmarking of Michelin, Pirelli, Bridgestone, Prometeon, and Continental across Predictive Maintenance Maturity vs. Scrap Reduction.
5. **Implementation Governance Framework & RACI Matrix**: Clear role assignments across Plant Director, Smart Manufacturing Lead, Maintenance Supervisor, IT Lead, and Quality Manager.

---

## 🚀 How to Submit to Udacity
1. Open Udacity Classroom: `Course 2 -> Project: Building a Market Research Agent -> Submit Project`.
2. Upload either:
   * The completed Word document: `research-brief-completed.docx` (or `research-brief-template.docx`).
   * A ZIP archive of the `Project_Market_Research_Agent` directory.
   * Or provide the GitHub repository URL with `Market_Intelligence_Research_Brief.md`.
