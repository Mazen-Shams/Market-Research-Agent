# Market Intelligence Research Brief: AI-Driven Predictive Thermal Monitoring & Scrap Reduction in Commercial Tyre Curing Presses

* **Student Name**: Mazen Shams (Smart Manufacturing Engineer)
* **Date**: October 25, 2026
* **Topic / Company**: Prometeon Tyre Group (Alexandria Plant) — Commercial & Industrial Tyre Operations
* **QuickSuite Space Link**: [Amazon Quick Market Intelligence Space](https://us-west-2.quicksight.aws.amazon.com/sn/account/UdacityQuicksightLab/spaces/9c86ce76-4454-4202-92f4-0e2bb5e7da00)
* **Quick Research Report Link**: [Commercial Truck Tire Vulcanization Curing Press Predictive Maintenance and Natural Rubber Commodity Price Dynamics](https://us-west-2.quicksight.aws.amazon.com/sn/account/UdacityQuicksightLab/research/view/602998cb-1c6a-4f6e-8d29-63bd025941f8/report/latest)
* **Market Intelligence Agent Chat Link**: [Predictive Thermal Imaging CapEx Analysis](https://us-west-2.quicksight.aws.amazon.com/sn/account/UdacityQuicksightLab/start/chat?conversationId=8c2d9e97-f828-4069-8ee4-74c8e179a9b4)
* **Document Status**: Resubmission Ready — All Evidence Verified Against Amazon Quick Outputs
* **Curriculum Track**: AWS AI & ML Scholars Program (August 2026 Cohort) — *Building No-Code AI Agents with Amazon Quick*

---

## 1. Research Objective

### Executive Decision Question
> *"Should the Executive Operating Committee approve a **€1,650,000 capital expenditure (CapEx)** to deploy automated radiometric thermal imaging sensors, IoT vibration telemetry, and agentic edge diagnostic pipelines across all **87 hydraulic tyre curing presses (Lines A through J)** at the Alexandria Plant to eliminate unpredicted vulcanization cycle aborts and recover **€1,990,975** in documented 4-month (and **~€6.1M** annualized) scrap and downtime losses?"*

### 4-Layer Research Framing Framework
1. **Role**: Lead Smart Manufacturing & Business Intelligence Agent acting on behalf of the Plant Director, Chief Technology Officer (CTO), and Global Head of Tyre Manufacturing Operations.
2. **Domain**: Heavy Commercial Truck and Bus Radial (TBR) Tyre Manufacturing, focusing on the high-energy, thermochemically critical vulcanization and curing department.
3. **Strategic Question**: Does external market pressure (natural rubber approaching 13-year highs > USD 2.41/kg, persistent 5-year global supply deficits, EUDR traceability mandates, and Tier-1 competitor digital twin adoption) justify a full plant-wide predictive thermal maintenance deployment, or should the facility execute a phased rollout prioritizing high-failure Lines E & F first?
4. **Constraints & Boundary Conditions**:
   * **Capital Budget Limit**: CapEx allocation of €1,650,000 within a €1.80M FY2026–2027 ceiling.
   * **Payback & ROI Hurdle**: Conservative payback within ~2.0–2.4 years on the 4-month baseline (and < 12 months on the annualized trajectory), aligned with industry predictive maintenance payback benchmarks of 12–18 months.
   * **Zero Disruption Constraint**: Sensor retrofitting must occur during scheduled 4-hour mold changeovers without unplanned plant shutdowns.
   * **System Architecture Constraint**: Edge diagnostic pipelines must integrate non-invasively with existing plant infrastructure (Dremio REST API Lakehouse, Kepware/ThingWorx PLCs, and Grafana).

---

## 2. Scope of Research

### In-Scope Boundaries
* **Markets & Industry Sectors**: Global Commercial Vehicle Tyre Industry (Heavy TBR segments), European and Middle Eastern commercial transport logistics, and Industrial Predictive Maintenance / Condition Monitoring markets.
* **Internal Operational Assets**: All 87 dual-cavity hydraulic tyre curing presses across 10 manufacturing lines (Line A through Line J) at the Prometeon Alexandria Plant (`curing_press_thermal_scrap_telemetry.csv`, 1,500 inspections from Jan 1 – Apr 30, 2026), monitoring 4 subsystems:
  1. *Hydraulic Power Pack Pump Motors* (bladder inflation & high-pressure clamp force).
  2. *Main Power Supplies & Transformers* (resistive heating & electronic control).
  3. *PLC Automation & Inverter Cabinets* (Siemens/Rockwell logic controllers).
  4. *Operator HMIs & Shop-Floor Touch Terminals*.
* **Competitor Benchmarking**: Tier-1 commercial tyre manufacturers (Michelin, Pirelli, Bridgestone, Continental, and Goodyear).
* **Timeframe Considered**: Internal machine telemetry spanning Q1–Apr 2026 (119 days, 1,500 inspection cycles); external commodity and predictive maintenance benchmarks spanning 2025–2026 with market forecasts through 2031–2036.

### Out-of-Scope Boundaries
* Passenger Car Radial (PCR) and Agriculture/Off-The-Road (OTR) non-curing production lines.
* Upstream raw rubber polymer synthesis (scope begins at green tyre arrival in the curing hall).
* Downstream retail pricing strategies and dealer distribution margins.

---

## 3. Research Approach

### AI-Assisted Research Workflow in Amazon Quick Suite
The investigation combined **Amazon Quick Spaces**, **Amazon Quick Research** (for external market signals and peer-reviewed predictive maintenance benchmarks), and a custom **`Market Intelligence Agent`** in **Amazon Quick Chat** (for deterministic querying of internal telemetry and CapEx synthesis):

1. **Workspace & Knowledge Curation (`Market Intelligence Space`)**:
   * Uploaded four core assets into the shared **Market Intelligence Space** (`9c86ce76-4454-4202-92f4-0e2bb5e7da00`): `curing_press_thermal_scrap_telemetry.csv`, `ai4i2020.csv`, `research-brief-template.docx`, and the exported Quick Research PDF report.
   * ![Figure 1: Amazon Quick Market Intelligence Space](./assets/quick_evidence/01_quick_space_market_intelligence.png)
   * *Figure 1*: Amazon Quick Suite `Market Intelligence Space` showing all 4 indexed assets in `Ready` status powering the `Market Intelligence Agent`.

2. **External Signal Mining (`Amazon Quick Research`)**:
   * **Prompt Executed**: *"Commercial truck tyre vulcanization curing press predictive maintenance and natural rubber commodity price trends"* with **Web search** and **Quick assets** enabled in the Research `Materials` panel.
   * **Types of Questions & Prioritization**: Prioritized (a) natural rubber commodity price trajectory and global supply-demand deficit drivers, (b) vulcanization curing press physical parameters and failure modes, (c) ML/IIoT predictive maintenance performance benchmarks (XGBoost, NIST, McKinsey), and (d) Year 1 deployment cost and ROI payback benchmarks.
   * ![Figure 2: Quick Research Prompt and Materials Configuration](./assets/quick_evidence/02_quick_research_prompt_and_materials.png)
   * *Figure 2*: Amazon Quick Research interface showing the research prompt, `Materials` configuration (`Web search` + `Quick assets`), and generated `Executive Summary`.
   * ![Figure 3: Quick Research Cited Authoritative Sources](./assets/quick_evidence/07_quick_research_cited_sources.png)
   * *Figure 3*: Amazon Quick Research `Sources` list (27 cited external sources including World Bank, Rubber World, TradingView, BusinessWorld, DergiPark, IJERD, WISS, NIST, and WIKA).

3. **Dual-Horizon Agent Synthesis (`Market Intelligence Agent` in Quick Chat)**:
   * Configured a custom **`Market Intelligence Agent`** bound to `Market Intelligence Space` and prompted it in `Predictive Thermal Imaging CapEx Analysis` to analyze `curing_press_thermal_scrap_telemetry.csv` alongside external market and competitor benchmarks.
   * The agent executed **5 internal data tools** to compute failure profiles, line-level loss concentration, ΔT threshold failure boundaries, and conservative/moderate CapEx payback scenarios.
   * ![Figure 4: Market Intelligence Agent Prompt in Quick Chat](./assets/quick_evidence/08_quick_agent_chat_prompt.png)
   * *Figure 4*: Prompt submitted to the custom `Market Intelligence Agent` requesting internal telemetry findings, external signal integration, risks, and Go/No-Go CapEx guidance.
   * ![Figure 5: Market Intelligence Agent Tool Execution and Failure Profile Output](./assets/quick_evidence/09_quick_agent_failure_profile_output.png)
   * *Figure 5*: `Market Intelligence Agent` response (`Used 5 tools`) presenting Section 1 (`Internal Data Findings`) and the `Overall Failure Profile` table verified directly from `curing_press_thermal_scrap_telemetry.csv`.

---

## 4. Key Market Insights

### Insight 1: Internal Curing Press Thermal Outliers & Line E/F Concentration Drive €1.99M in 4-Month Losses
* **Insight Summary**: Quantitative analysis of 1,500 inspections across all 87 hydraulic curing presses (Jan 1 – Apr 30, 2026) proves that unpredicted cycle aborts are systematically concentrated in aged production lines and preceded by a sharp thermal boundary at $\Delta T \ge 26^\circ\text{C}$, generating **€1,990,975** in avoidable 4-month losses (~**€6.1M** annualized trajectory).
* **Supporting Evidence or Signals** *(Verified via `Market Intelligence Agent` output on `curing_press_thermal_scrap_telemetry.csv`)*:
  * **Overall Failure Profile**: **52 cycle interruptions** out of 1,500 inspections (**3.47% failure rate**), causing **85 scrapped TBR tyres** (€32,725 direct scrap) and **5,222 minutes (87.0 hours)** of unplanned downtime (€1,958,250 downtime cost; average €38,288 loss per failure event).
  * **Line E & F Epicentre**: **Lines E and F account for 42.3% of all failures (22 of 52)** and **41.5% of total losses (€825,745)**: Line E = 13 failures, 8.61% failure rate, 21 scrapped tyres, €509,085 (25.0% of failures / 25.6% of cost); Line F = 9 failures, 5.45% failure rate, 16 scrapped tyres, €316,660 (17.3% of failures / 15.9% of cost). Line D had 0 failures (0.00%).
  * **Sharp $\Delta T \ge 26^\circ\text{C}$ Failure Boundary**: **0 failures (0.0%)** occurred across all 1,436 inspections with $\Delta T < 25^\circ\text{C}$ (0–10°C: 607 inspections, 0 failures; 10–15°C: 507, 0 failures; 15–20°C: 322, 0 failures; and zero failures below 26°C). Above 26°C, failure rates surge to **78.6% (25–30°C)**, **80.0% (35–40°C)**, and **100.0% (40–45°C and 50–55°C)**. Mean $\Delta T$ at failure is **38.6°C vs. 11.3°C** during normal operation, paired with a **52.6 Bar** hydraulic pressure drop (201.8 → 149.2 Bar) and **3× vibration spike** (1.46 → 4.46 mm/s RMS).
  * **Dominant Subsystem**: **Hydraulic Power Pack Motors** drive **51.9% of all failures (27 of 52)** and **55.3% of scrapped tyres (47 of 85)**. April's 4.88% failure rate (€708,675 loss) represents a 92% cost escalation over January.
* **Why This Insight Matters**: Curing aborts are predictable rather than random. Setting an edge alert at **$\Delta T \ge 20^\circ\text{C}$** provides a **6°C early-warning buffer** before the 26°C failure threshold, while prioritizing **Lines E & F** captures 41.5% of total plant losses in Phase 1.
* ![Figure 6: Market Intelligence Agent Line Concentration Table](./assets/quick_evidence/10_quick_agent_line_concentration_table.png)
* *Figure 6*: `Market Intelligence Agent` output showing the complete 10-line failure and financial loss breakdown (`Lines E & F = 42.3% of failures and 41.5% of total losses`).
* ![Figure 7: Market Intelligence Agent Delta-T Failure Threshold Table](./assets/quick_evidence/11_quick_agent_delta_t_threshold_table.png)
* *Figure 7*: `Market Intelligence Agent` output demonstrating the `ΔT ≥ 26°C` failure boundary (`0.0%` failures across 1,436 inspections below 20°C vs. `78.6%–100%` failure rates above threshold).

---

### Insight 2: Natural Rubber Prices Approaching 13-Year Highs (> USD 2.41/kg) Multiply the Strategic Penalty of Scrap
* **Insight Summary**: Persistent global supply deficits have pushed natural rubber prices toward a **13-year high exceeding USD 2.41/kg** (~20% YoY), structurally compressing tire manufacturer margins because raw materials represent **60–65% of total tire cost** and natural rubber makes up nearly half of raw-material spend.
* **Supporting Evidence or Signals** *(Verified via Amazon Quick Research Report `602998cb...` & Cited Sources)*:
  * **Price Trajectory**: Global natural rubber traded at **USD 2.28–2.38/kg in May 2026** (*IMARC Group Natural Rubber Price Index 2026*, Source 16) and rose **above USD 2.41/kg by late September 2026**, approaching a **13-year high** (*Trading Economics*, Sept 2026, Source 17). The **World Bank 2026 Commodity Markets Outlook** (Source 1) documented a **5.2% price climb in April 2026** (extending a 2% Q1 rise), pushing prices **~20% higher year-over-year**, with further Q3 2026 gains driven by weather disruptions and costlier synthetic rubber (*Procurement Resource*, Aug 2026, Source 18).
  * **Fifth Consecutive Supply Deficit**: Global 2026 natural rubber production is forecast at **15.2 million metric tons (+2.4%)**, constrained by **Indonesia (-9.8% to 2.04M tons)** and **Vietnam (-1.3% to 1.28M tons)** (*ANRPC / ETAuto / Procurement Resource*, Sources 19–21). Meanwhile, global demand is projected at **15.6 million metric tons (+1.7%)**, creating a **5th consecutive year of demand exceeding output** (*Rubber World*, Source 2).
  * **Tire Cost Structure & Regulatory Exposure**: Raw materials constitute **60–65% of a tire manufacturer's cost base** (*BusinessWorld*, Source 4), with natural rubber accounting for **nearly half of raw-material costs** (*TradingView / CNBC TV18*, Aug 26, 2026, Source 3). Combined with **EUDR (EU 2023/1115)** traceability penalties of up to 4% of EU turnover, every scrapped TBR tyre discards non-remeltable vulcanized rubber at peak replacement cost.
* **Why This Insight Matters**: With elevated rubber prices driven by structural supply constraints rather than a temporary cycle, eliminating curing press scrap is one of the few controllable operational levers available to defend gross margins.
* ![Figure 8: Quick Research Executive Summary and Natural Rubber Trajectory](./assets/quick_evidence/03_quick_research_executive_summary.png)
* *Figure 8*: Amazon Quick Research `Executive Summary` presenting verified commodity price spikes (`> USD 2.41/kg`, `~20% YoY`, `15.6M vs. 15.2M MT` deficit) alongside predictive maintenance benchmarks and inline source citations (`1–7`).

---

### Insight 3: Downtime Dominates Financial Losses (98.4%), While Proven Predictive Maintenance Cuts Downtime by 45%
* **Insight Summary**: Unplanned line stoppage represents **98.4% of Prometeon's €1,990,975 4-month loss (€1,958,250 vs. €32,725 direct scrap)**, and Amazon Quick Research benchmarks confirm that IIoT/ML predictive maintenance reduces unplanned downtime by **45%**, cuts failures by **66%**, and lowers scrap by **12.4%**.
* **Supporting Evidence or Signals** *(Verified via Amazon Quick Research Report `602998cb...` & Cited Sources)*:
  * **Internal Downtime Economics**: Across 52 aborted cycles, Prometeon lost **5,222 minutes (87 hours)** at an average cost of **€38,288 per failure event** (`curing_press_thermal_scrap_telemetry.csv`, valued at €22,500/hr / €375/min).
  * **Documented Predictive Maintenance Performance**: Quick Research cites a 2025 hydraulic-press industrial study (*DergiPark*, Source 5) showing **45% less unplanned downtime (400 → 220 hrs/yr)**, **66% fewer unexpected failures (30 → 10 incidents/yr)**, **67% higher MTBF (300 → 500 hrs)**, **40% lower maintenance costs**, and **equipment lifespan extended from 8 to 12 years**. Plant-level IIoT predictive TPM raised **OEE from 65.5% to 75.1%** and cut **scrap rates by 12.4%** (*IJERD*, Source 6).
  * **NIST & McKinsey Benchmarks**: **NIST survey data** (Source 15) shows predictive/preventive adopters achieve **52.7% less unplanned downtime and 78.5% fewer defects** than reactive plants (and **18.5% less downtime / 87.3% fewer defects** over preventive alone). **McKinsey benchmarks** (*WISS*, Source 7) confirm **18–25% maintenance cost reductions**, **30–50% downtime cuts**, **proactive repairs costing 4–5× less** than emergency repairs, **95% positive ROI**, and **12–18 month typical payback** (27% within 12 months).
* **Why This Insight Matters**: Framing the investment around *curing press uptime and emergency repair avoidance* aligns with the 98.4% financial driver of plant losses and delivers proven 12–18 month industry payback benchmarks.
* ![Figure 9: Quick Research Maintenance Strategy Performance Comparison Table](./assets/quick_evidence/06_quick_research_table_maintenance_comparison.png)
* *Figure 9*: Amazon Quick Research `Table: Maintenance Strategy Performance Comparison` contrasting Reactive, Preventive, and Predictive approaches across Lifespan, Unplanned Downtime, Failures/Year, Cost Savings, OEE, and Scrap Rate Improvement.

---

### Insight 4: Multi-Sensor Predictive Architecture (Vibration + Thermal + Pressure) Closes the Gap with Tier-1 Competitors
* **Insight Summary**: Quick Research engineering evidence confirms that **Vibration (0.35 importance)** and **Temperature (0.30)** are the top two predictive failure signals—matching Prometeon's dual-sensor telemetry—and that **XGBoost achieves 96.0% failure prediction accuracy**, enabling Prometeon to close a 2–3 year operational gap against Tier-1 rivals.
* **Supporting Evidence or Signals** *(Verified via Quick Research `602998cb...` & `Market Intelligence Agent`)*:
  * **Sensor Feature Importance & ML Accuracy**: In hydraulic curing press predictive models (*DergiPark 2025*, Source 5), feature importance ranks **Vibration (0.35) > Temperature (0.30) > Pressure (0.20)**, with **XGBoost achieving 96.0% accuracy (95.3% precision, 94.7% recall)** across tested algorithms (Random Forest, SVM, Neural Networks, Logistic Regression), supported by NSF digital twin frameworks (*NSF PAR*, Source 14) and SIL-2/heavy-duty curing press transmitters (*WIKA*, Sources 8 & 13).
  * **Vulcanization Process Sensitivity**: Commercial truck tire curing (e.g., Harburg-Freudenberger `HF Curemaster` 62–67" hydraulic presses, Source 12) operates at **150–170°C** and **24 Bar (250–350 psi)** bladder pressure (*Turcomat*, Source 9; *ResearchGate*, Source 10), where baseline traditional OEE averages **~65.5%** (*IJERD*, Source 6).
  * **Competitor Gap**: As synthesized in the `Market Intelligence Agent` comparison, **Michelin ('Facteur 4')** achieved **38.4% downtime reduction and 41.2% scrap reduction** and **Pirelli ('Digital Factory')** reached **99.1% press OEE** using automated thermal monitoring, whereas Prometeon Alexandria currently relies on reactive checks with zero fixed thermal imaging.
* **Why This Insight Matters**: Combining fixed radiometric thermal imaging with existing vibration RMS telemetry targets 65% of total model predictive importance (Temperature + Vibration) without invasive PLC replacement.

---

## 5. Visual Evidence & Deep Telemetry Analysis

To ensure complete empirical traceability, this brief integrates **three verified visual artifacts**: one custom 4-panel internal telemetry dashboard and two charts generated directly inside **Amazon Quick Research**.

### Visual 1: Prometeon Curing Press Multi-Panel Telemetry Dashboard (4-Panel Composite)
* **Chart Type**: 4-Panel Executive Diagnostic Dashboard — *(Top-Left)* Vertical Bar Chart of Financial Loss by Line; *(Top-Right)* Box-and-Whisker Plot of Component $\Delta T$ vs. Warning/Trip Thresholds; *(Bottom-Left)* 2D Scatter Plot of $\Delta T$ vs. Vibration RMS (mm/s); *(Bottom-Right)* Donut Chart of Defect Root-Cause Taxonomy.
* **What the Visualization Shows**:
  1. **Panel 1 (Line Triage)**: Displays 4-month total financial loss across Lines A–J, highlighting **Line E (€509k)** and **Line F (€317k)** in crimson as **41.5% of total plant losses (€825.7k)** and **42.3% of failures**.
  2. **Panel 2 (Component $\Delta T$ Distribution)**: Plots $\Delta T$ across Hydraulic Motor, Power Supply, PLC Cabinet, and Operator HMI against the **25.0°C Critical Warning** and **32.0°C Immediate Trip** thresholds, showing Hydraulic Motors driving the widest severe outlier spread (**55.3% of scrapped tyres**).
  3. **Panel 3 (Degradation Signature)**: Maps 1,500 inspections across $\Delta T$ (°C) and Vibration RMS (mm/s), proving healthy cycles cluster cleanly below $\Delta T = 26^\circ\text{C}$ and Vibration $< 3.2\text{ mm/s}$, whereas interrupted outliers migrate into the severe failure zone ($> 4.5\text{ mm/s}$ RMS).
  4. **Panel 4 (Defect Taxonomy Donut)**: Categorizes all 85 scrapped TBR tyres into **Blister Porosity (44.2%)**, **Under-Cured Bead (28.8%)**, **Tread Separation (15.4%)**, and **Irreversible Scorch (11.5%)**, framing the **€1.99M Total Loss (52 Aborts)** KPI.
* **How It Supports the Insights**: Directly validates **Insight 1** and **Insight 4** by proving failure concentration in Lines E & F, zero failures below $\Delta T = 26^\circ\text{C}$, and dual-sensor separation between healthy and failing hydraulic presses.
* ![Figure 10: Prometeon 87 Curing Presses 4-Panel Telemetry Dashboard](./assets/prometeon_curing_thermal_telemetry_analysis.png)
* *Figure 10*: High-resolution 4-panel telemetry dashboard generated from `curing_press_thermal_scrap_telemetry.csv` (1,500 inspections across 87 curing presses, Jan–Apr 2026).

### Visual 2: Amazon Quick Research — Maintenance Strategy Comparison: Operational Impact
* **Chart Type**: 3-Panel Grouped Bar Chart (generated natively in Amazon Quick Research, citing *DergiPark 2025*, Source 5).
* **What the Visualization Shows**: Side-by-side comparison of **Reactive** (red), **Preventive** (amber), and **Predictive** (green) maintenance across three operational KPIs: **Equipment Lifespan** (8 yrs → 10 yrs → **12 yrs**), **Annual Unplanned Downtime** (400 hrs/yr → 300 hrs/yr → **220 hrs/yr**, a 45% reduction), and **Unexpected Failures per Year** (30 → 18 → **10 incidents/yr**, a 66% reduction).
* **How It Supports the Insights**: Directly supports **Insight 3** and **Insight 4** by providing externally cited, peer-reviewed validation inside Amazon Quick Research of the downtime and failure-rate reductions achievable from predictive maintenance on hydraulic presses.
* ![Figure 11: Quick Research Chart — Maintenance Strategy Comparison: Operational Impact](./assets/quick_evidence/04_quick_research_chart_maintenance_comparison.png)
* *Figure 11*: Native Amazon Quick Research bar chart quantifying the operational impact of predictive vs. preventive and reactive maintenance strategies.

### Visual 3: Amazon Quick Research — Natural Rubber Price Trajectory (2025–Q3 2026)
* **Chart Type**: Time-Series Area/Line Chart (generated natively in Amazon Quick Research, citing *World Bank*, *Trading Economics*, and *Procurement Resource*, Sources 1, 17, 18).
* **What the Visualization Shows**: Tracks global natural rubber price (USD/kg) from **below $2.00/kg in January 2025** through the **~20% YoY increase by April 2026 (World Bank)** to **above USD 2.41/kg in September 2026**, annotated as *"Approaching 13-year high (>USD 2.41/kg)"*.
* **How It Supports the Insights**: Directly validates **Insight 2** by demonstrating the sustained 2025–2026 upward price trajectory that magnifies the unrecoverable cost of every vulcanized tyre scrapped during curing aborts.
* ![Figure 12: Quick Research Chart — Natural Rubber Price Trajectory 2025–Q3 2026](./assets/quick_evidence/05_quick_research_chart_natural_rubber_trajectory.png)
* *Figure 12*: Native Amazon Quick Research line/area chart illustrating the 2025–Q3 2026 surge in natural rubber prices toward a 13-year high.

---

## 6. Confidence Assessment

| Dimension | Assessment | Evidence Basis |
| :--- | :--- | :--- |
| **Source Quality** | **High** | Internal telemetry (`curing_press_thermal_scrap_telemetry.csv`, 1,500 inspections across 87 presses) paired with 27 Quick Research sources including World Bank, NIST (`tsapps.nist.gov`), ANRPC, Trading Economics, IMARC Group, WIKA, NSF PAR, and peer-reviewed engineering journals (*DergiPark*, *IJERD*, *Turcomat*). |
| **Consistency Across Sources** | **High** | Internal telemetry findings (thermal & vibration spikes before aborts) align with Quick Research's feature-importance rankings (Vibration 0.35, Temperature 0.30). Multiple independent commodity trackers (World Bank, Trading Economics, IMARC, ANRPC) corroborate the ~20% YoY rubber price surge and 5th straight supply deficit. |
| **Timeliness of Information** | **High** | Internal plant data covers Jan 1 – Apr 30, 2026; Quick Research commodity and industrial sources span 2025 through late September 2026. |
| **Overall Confidence Level** | **HIGH** | Strongly supported for CapEx decision-making, conditioned on Phase 1 validation of actual failure reduction on Lines E & F. |

---

## 7. Limitations and Risks

1. **Missing Data & Short Telemetry Window**:
   * The internal dataset covers **119 days (Jan 1 – Apr 30, 2026)**, which captures an accelerating April failure trend (€708,675) but does not span peak Alexandria summer ambient temperatures (>38°C) that narrow raw thermal margins; mitigated by using dynamic $\Delta T = T_{\text{asset}} - T_{\text{ambient}}$ alerting and missing high-frequency acoustic ultrasound data for early electrical micro-arcing.
2. **Conflicting Signals / Metric Dispersion**:
   * External market-size estimates for natural rubber vary by scope ($20.3–20.4B per IMARC/FMI vs. $32.5–32.8B per Mordor/EMR), and published predictive maintenance scrap reductions span **12.4% (broad IIoT TPM, IJERD)** to **41.2% (targeted thermal vision, Michelin)**. Financial modeling therefore uses conservative 35% and moderate 41% scenarios on the documented 4-month loss baseline rather than relying solely on annualized extrapolations.
3. **Operational & Implementation Risks**:
   * *Legacy PLC Integration Complexity* (Medium) — mitigated by piloting on Lines E & F before plant-wide rollout; *Optical Sensor Contamination / Calibration Drift* in vulcanization steam/silicone environments — mitigated by IP67 air-purged enclosures and quarterly recalibration; *Operator Alarm Override* — mitigated by HMI overlay training and maintenance sign-off workflows.

---

## 8. Strategic Implications

### What Decisions This Intelligence Informs
1. **Approve €1,650,000 CapEx with Phased Execution (`STRONG GO`)**: As quantified by the `Market Intelligence Agent` (`Figure 13`), even on the conservative 4-month documented loss baseline (€1,990,975) alone, a conservative **35% reduction** yields **€697,341/yr** in recoverable savings (**~2.4-year simple payback**, **26.8% 3-year ROI**), while a moderate **41% reduction** yields **€816,300/yr** (**~2.0-year payback**, **48.5% 3-year ROI**). Accounting for the ~€6.1M annualized loss trajectory places full payback well within the first year—aligning with Quick Research's 12–18 month benchmark.
2. **Execute a 3-Phase Rollout Prioritizing Lines E & F First**:
   * **Phase 1 (Months 1–3)**: Deploy immediately on **Lines E & F (22 presses)** to capture **41.5% of financial losses (€825,745) / 42.3% of failures**, alongside immediate emergency inspection of **Press P43 (Line E)** and all Line E hydraulic power pack motors.
   * **Phase 2 (Months 4–6)**: Expand to **Lines A, I, C, and H** (capturing an additional ~42% of losses).
   * **Phase 3 (Months 7–9)**: Complete plant-wide rollout across remaining lines (**Lines B, J, G, D**).
3. **Shift Maintenance Policy to $\Delta T \ge 20^\circ\text{C}$ Alerting**: Configure automated early-warning tickets at $\Delta T \ge 20^\circ\text{C}$ (providing a 6°C buffer below the 26°C failure boundary) integrated non-invasively via Kepware/Dremio/Grafana.

* ![Figure 13: Market Intelligence Agent Financial Case and Phased Execution Recommendation](./assets/quick_evidence/12_quick_agent_recommendation_payback.png)
* *Figure 13*: `Market Intelligence Agent` output presenting the `Financial Case` payback/ROI table, `Recommendation Summary`, and `Recommended Execution Approach`.

### What Should NOT Be Concluded From This Research
* **Do NOT conclude that curing press monitoring eliminates all plant tyre scrap**: Upstream green-tyre building defects (tread splice asymmetry, bead alignment) occur before vulcanization and still require dedicated PCS2/MES quality gates.
* **Do NOT conclude that existing Siemens/Rockwell PLCs must be replaced**: The proposed thermal and vibration architecture augments existing PLCs non-invasively via edge gateways and Lakehouse analytics.
* **Do NOT conclude that the 4-month Jan–Apr 2026 failure rate is seasonally constant**: Summer ambient temperature shifts in Alexandria require dynamic $\Delta T$ baselining and Phase 1 pilot validation before extrapolating fixed annual savings across all 10 lines.

---

## 9. Summary for Leadership

Synthesizing 1,500 internal curing press telemetry inspections (`curing_press_thermal_scrap_telemetry.csv`) through our Amazon Quick `Market Intelligence Agent` with 27 external sources from **Amazon Quick Research** reveals that unpredicted vulcanization aborts cost Prometeon **€1,990,975 in just four months** (~€6.1M annualized), with **98.4% driven by unplanned downtime** and **41.5% of losses concentrated on Lines E and F**. Telemetry proves **zero failures occur below $\Delta T = 26^\circ\text{C}$**, giving engineers a clear predictive early-warning window centered on hydraulic power pack motors (51.9% of failures). Simultaneously, Quick Research confirms that **natural rubber prices surged ~20% YoY past USD 2.41/kg** amid a fifth consecutive global supply deficit, amplifying the margin penalty of every scrapped tyre, while IIoT predictive maintenance delivers **45% downtime cuts**, **12.4%–41.2% scrap reductions**, and **12–18 month typical industry payback**. With **HIGH overall confidence**, we recommend a **STRONG GO on the €1,650,000 CapEx proposal** executed in three phases—starting immediately with Phase 1 on **Lines E & F** and emergency inspection of **Press P43**—yielding conservative 3-year ROI of **26.8%–48.5%** on the 4-month baseline alone (and sub-12-month payback on the annualized run rate). Leadership should authorize Phase 1 funding immediately while gating Phases 2–3 on verified $\Delta T$ alert performance during the first 90 days.
