# Incident / Near-Miss Report with Root Cause Analysis

**Incident ID:** INC-2026-0501-01
**Classification:** Near-Miss (Equipment Damage, No Injury)
**Equipment Involved:** P-101A — Centrifugal Pump, Unit 100 Feed Section
**Date of Incident:** 2026-05-01
**Reported By:** R. Sharma (Shift Operator)
**Investigation Lead:** Unit 100 Maintenance Engineer

---

## 1. Description
During routine round, elevated vibration and abnormal noise were detected from P-101A drive-end bearing. Pump was shut down and switched to standby (P-101B) before catastrophic bearing seizure could occur. This is the **third bearing-related failure on P-101A in a four-month period** (see related work orders WO-2026-0114, WO-2026-0322).

## 2. Immediate Cause
Drive-end bearing (6309 type) showed advanced wear/pitting consistent with the two prior failures.

## 3. Root Cause Analysis (5-Why)
1. **Why did the bearing fail again?** — Bearing was operating under abnormal radial load.
2. **Why was there abnormal radial load?** — Motor-pump coupling alignment was found out of tolerance during teardown.
3. **Why was alignment out of tolerance?** — Laser alignment check confirmed 0.4mm angular misalignment, exceeding the 0.05mm/100mm tolerance specified in the pump vendor manual.
4. **Why was the misalignment not caught earlier?** — Standard practice after bearing replacement (WO-2026-0114, WO-2026-0322) was visual/straightedge alignment only; laser alignment was not part of the standard bearing-replacement work order checklist.
5. **Why was laser alignment not in the checklist?** — SOP-U100-002 and the associated maintenance work instructions did not mandate laser alignment verification after bearing replacement — this was a procedural gap.

**Root Cause:** Procedural gap — bearing replacement work orders did not mandate precision (laser) shaft alignment verification, allowing a pre-existing minor misalignment to progressively damage successive replacement bearings.

## 4. Contributing Factors
- No formal trigger existed to escalate a repeat failure (2 occurrences in 4 months) to an RCA before the 3rd event.
- Vibration trend data across the three events was not reviewed collectively until this investigation.

## 5. Corrective Actions
| # | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| 1 | Update SOP-U100-002 / bearing replacement work instruction to mandate laser alignment check after any bearing replacement | Maintenance Engineer | 2026-05-20 | Open |
| 2 | Add automatic RCA trigger rule: 2+ failures on same equipment/failure-mode within 6 months auto-escalates to RCA | Reliability Engineer | 2026-06-01 | Open |
| 3 | Review vibration trend history for all rotating equipment in Unit 100 for similar undetected misalignment patterns | Reliability Engineer | 2026-06-15 | Open |

## 6. Related Records
- Work Orders: WO-2026-0114, WO-2026-0322, WO-2026-0501
- SOP Referenced: SOP-U100-002 (Startup of Feed Transfer Pump)
- Equipment Tag: P-101A (see P&ID tag register)

## 7. Lessons Learned (for broader distribution)
Repeat failures of the same type on the same equipment are a leading indicator of a root cause not yet addressed, not routine wear-and-tear. Any bearing/rotating-equipment failure recurring within 6 months should trigger a mandatory alignment check and RCA before the next replacement, not after the third.

---
*This is a synthetic training document created for knowledge base testing purposes.*
