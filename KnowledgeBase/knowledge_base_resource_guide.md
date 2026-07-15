# AI for Industrial Knowledge Intelligence — Data & Resource Guide
*Mapped directly to Problem Statement #8: "Unified Asset & Operations Brain"*

All links below were checked live (July 2026). Nothing here is paywalled or requires special access unless noted.

---

## 1. Engineering Drawings & P&IDs
*For: Universal Document Ingestion & Knowledge Graph Agent (P&ID parsing, computer vision, OCR)*

| Resource | What it gives you | Link |
|---|---|---|
| EPA public-domain sample P&ID | A real, full P&ID from a government engineering document (usable for CV/OCR testing without licensing issues) | https://www.epa.gov/sites/default/files/2019-07/documents/wbs-ixclo4-documentation-june-2019.pdf |
| PDHAcademy P&ID course (30+ worked P&ID figures, tag/legend tables) | Multiple annotated example P&IDs + instrument tag numbering conventions (ISA S5.1) | https://pdhacademy.com/wp-content/uploads/2023/08/462-Piping-and-Instrumentation-Diagrams.pdf |
| AIChE P&ID webinar deck | Equipment/instrument symbol reference, tag numbering logic | https://www.aiche.org/sites/default/files/docs/webinars/BarkelB-PIDs.pdf |
| Wikimedia Commons P&ID symbol diagrams (CC-BY-SA, machine-readable SVG) | Clean vector P&ID you can rasterize at multiple resolutions to stress-test your CV pipeline | https://commons.wikimedia.org/wiki/File:Pump_with_tank_pid_en.svg |

**Included in this kit:** `sample_pid_diagram.svg` + `sample_pid_tag_register.csv` — an original simple P&ID with ground-truth tag extraction, so you can test ingestion accuracy on day one without waiting to source real drawings.

---

## 2. Maintenance Records, Sensor Data & Equipment Failure History
*For: Maintenance Intelligence & RCA Agent*

| Resource | What it gives you | Link |
|---|---|---|
| NASA Prognostics Data Repository (PCoE) | Umbrella repo — turbofan, bearing, battery, and 20+ other run-to-failure datasets | https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/ |
| NASA C-MAPSS Turbofan Degradation Dataset | Time-series sensor data to failure — great for RUL/predictive-maintenance demo | https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip |
| PHM Society mirror of NASA repository | Same datasets, alternate host if NASA links are slow | https://data.phmsociety.org/nasa/ |
| AI4I 2020 Predictive Maintenance Dataset (UCI, CC BY 4.0) | 10,000 labeled machine records, 5 real failure modes (tool wear, heat dissipation, power, overstrain, random) | https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset |
| ↳ Raw CSV direct download | | https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv |
| ↳ Kaggle mirror | | https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020 |
| Case Western Reserve University (CWRU) Bearing Dataset | Vibration signals for inner-race/outer-race/ball bearing faults — classic RCA/failure-pattern source | Kaggle mirror: https://www.kaggle.com/datasets/astrollama/cwru-case-western-reserve-university-dataset |
| MIMII Sound Dataset (Hitachi, Zenodo, CC BY-SA) | 26,000+ real factory machine sound clips (pumps, valves, fans, slide rails), normal + anomalous | https://zenodo.org/records/3384388 |

---

## 3. Maintenance Logbook Text / Free-Text NLP Corpora
*For: RAG copilot + entity extraction on messy technician language (exactly what the PS calls "recreating documents that already exist")*

| Resource | What it gives you | Link |
|---|---|---|
| MaintNet (ACL/COLING 2020) | Real free-text maintenance logbooks from aviation, automotive, and facilities domains, plus abbreviation lists and NLP preprocessing tools built specifically for this kind of jargon-heavy text | Paper: https://arxiv.org/pdf/2005.12443 · Curated dataset links: https://github.com/TLP-COI/awesome-tlp |
| Auton Lab `pmx_data` | Meta-repository indexing ~20 predictive-maintenance datasets with download scripts, so you don't have to hunt each one individually | https://github.com/autonlab/pmx_data |
| Kaggle Maintenance Work Orders Dataset | Ready-made CMMS-style work order text | https://www.kaggle.com/datasets/tinhban/maintenance-work-orders-dataset |

---

## 4. Visual Inspection / Quality Datasets
*For: Quality & Regulatory Compliance Intelligence, defect/anomaly detection*

| Resource | What it gives you | Link |
|---|---|---|
| MVTec AD | 5,000+ high-res images across 15 object/texture categories, pixel-precise defect annotations — the standard benchmark for industrial visual inspection | https://www.mvtec.com/research-teaching/datasets/mvtec-ad |
| MVTec AD 2 | Newer, harder inspection scenarios (8,000+ images, real lighting variation) | https://www.mvtec.com/research-teaching/datasets/mvtec-ad-2 |
| UCI Steel Plates Faults | 1,941 labeled steel plate defects across 7 fault types — good lightweight quality-domain dataset | https://archive.ics.uci.edu/dataset/198/steel+plates+faults |

---

## 5. Regulatory & Safety Documents — India (matches the PS's OISD/PESO/Factory Act references directly)
*For: Quality & Regulatory Compliance Intelligence Agent*

| Resource | What it gives you | Link |
|---|---|---|
| **The Factories Act, 1948** — official full text | Complete Act (India Code, Govt of India) — real regulatory text to ingest for compliance-gap detection | https://www.indiacode.nic.in/bitstream/123456789/15981/1/the_factories_act,_1948.pdf |
| ↳ Mirror (DGMS) | | https://www.dgms.gov.in/writereaddata/UploadFile/The_Factories_Act-1948.pdf |
| **OISD Standards List** — official directory of all 100+ OISD standards | Index page linking to individual standards (10 of them are statutorily mandatory) | https://www.oisd.gov.in/en-in/oisd-standards-list |
| ↳ Example full OISD standard (Fire Protection Facilities, hosted by OISD) | Real 100+ page technical safety standard | https://www.oisd.gov.in/public/assets/filemanager/1742541199_e2b8de065ca3061addb4.pdf |
| ↳ Example OISD-GDN-192 (General safety practices at worksites) | Shorter standard, good for a first ingestion test | https://bcplonline.co.in/Tenderdoc/q8wmjy0oc7_OISD.pdf |
| **PESO** (Petroleum & Explosives Safety Organisation) — official site | Petroleum Rules 2002, Explosives Rules, SMPV(U) Rules — all linked from here | https://www.peso.gov.in/en |

## 5b. Regulatory & Safety Documents — Global (useful cross-reference / benchmark structure)

| Resource | What it gives you | Link |
|---|---|---|
| OSHA Process Safety Management Standard, 29 CFR 1910.119 (official publication) | Full official PSM standard text — 14-element structure is a good template for your compliance ontology | https://www.osha.gov/sites/default/files/publications/OSHA3132.pdf |

---

## 6. Curated Aggregator Repositories (one-stop shopping if you need more)

| Repo | Focus |
|---|---|
| https://github.com/jonathanwvd/awesome-industrial-datasets | Broadest curated list — chemical, mechanical, oil & gas, quality |
| https://github.com/nicolasj92/industrial-ml-datasets | Manufacturing-focused, published with an academic review paper |
| https://github.com/ricardoevvargas/awesome-industry40-datasets | Industry 4.0 specific (control loops, SECOM semiconductor data, etc.) |
| https://github.com/SkyShunsuke/Awesome-Industrial-Vision-Datasets | 50+ industrial computer-vision datasets |

---

## 7. The Gap You Cannot Fill With Public Data — and What To Do About It

There is **no public real-world dataset** for: internal SOPs, incident/near-miss reports, RCA writeups, or project files/email archives — companies don't publish these for obvious reasons. This is exactly why judges say "ideally validated with real industrial document samples": they know most teams can't get real ones, so a credible synthetic set matters.

**Recommended approach:**
1. Use the *real* regulatory PDFs (Section 5) as-is — don't synthesize these, they're authentic and freely available.
2. Use the *real* sensor/failure datasets (Section 2) as-is for the RCA/predictive agent.
3. For SOPs, inspection reports, and incident reports — generate a small, internally consistent synthetic set (20–50 documents) that cross-reference the same equipment tags and the same OISD/Factory Act clauses used in Section 5. This lets you demonstrate the **cross-document knowledge graph linkage** the judges are scoring on (25% Innovation + 20% Technical Excellence combined).

This kit includes five such synthetic documents, deliberately cross-referenced to each other, as a starter set — see below.

---

## 8. What's Included in This Kit (ready to ingest today)

| File | Simulates | Use it to test |
|---|---|---|
| `sample_pid_diagram.svg` | An engineering P&ID | Computer vision / OCR ingestion, tag extraction |
| `sample_pid_tag_register.csv` | Ground-truth extracted tags from the P&ID above | Entity extraction accuracy scoring |
| `sample_maintenance_work_orders.csv` | 15 CMMS work order records, Indian plant context | RAG copilot, RCA agent, failure pattern mining |
| `sample_sop_centrifugal_pump_startup.md` | An operating procedure | RAG copilot answer quality, procedure-following queries |
| `sample_inspection_report.md` | A pressure vessel inspection report (references OISD-STD-130 & SMPV Rules) | Compliance agent, inspection-to-regulation linkage |
| `sample_incident_near_miss_report.md` | A near-miss/RCA report referencing the same pump tag as the work orders | Lessons Learned agent, cross-document KG linkage |

All six files reference the same equipment tags (**P-101A/B**, **TK-101**, **E-101**) on purpose — so your knowledge graph should be able to connect a work order → an inspection finding → an incident → the regulation it violated. That end-to-end trace is the single best demo moment for this problem statement.
