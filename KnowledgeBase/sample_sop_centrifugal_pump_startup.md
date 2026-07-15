# Standard Operating Procedure
## SOP-U100-002: Startup of Feed Transfer Pump (P-101A/B)

**Unit:** 100 — Feed Transfer & Heat Exchange Loop
**Equipment:** P-101A (Duty), P-101B (Standby) — Centrifugal Pumps
**Revision:** 3 | **Effective Date:** 2026-01-01
**Regulatory Reference:** Factories Act, 1948 — Section 21 (Fencing of Machinery); OISD-STD-105 (Safety requirements in petroleum refineries)

---

### 1. Purpose
This procedure defines the safe startup sequence for the feed transfer pump P-101A (or standby P-101B) supplying process feed from Tank TK-101 to Heat Exchanger E-101.

### 2. Scope
Applies to all shift operators and maintenance personnel authorized to start/stop feed transfer pumps in Unit 100.

### 3. Safety Precautions
- PPE required: safety helmet, safety glasses, chemical-resistant gloves, steel-toe boots.
- Confirm Lock-Out Tag-Out (LOTO) has been fully removed and permit closed before startup.
- Do not start the pump if TK-101 level (LT-102) reads below 15% — risk of cavitation.
- Ensure area around pump is clear of personnel before energizing.

### 4. Pre-Startup Checks
1. Verify TK-101 level (LT-102) is above 15% and below LAH-102 high alarm setpoint.
2. Confirm suction and discharge valves are aligned per line-up sheet.
3. Check pump coupling guard is in place.
4. Verify lubrication oil level at sight glass is within normal band.
5. Confirm FIC-101 controller is in MANUAL mode with output at 0% prior to start.

### 5. Startup Sequence
1. Open suction valve fully.
2. Crack open discharge valve approximately 10%.
3. Start pump motor from DCS or local panel.
4. Confirm discharge pressure builds within 10 seconds; if not, stop pump immediately and investigate.
5. Gradually open discharge valve to 100% over 30 seconds while monitoring FT-101.
6. Switch FIC-101 to AUTO once flow stabilizes near setpoint.
7. Monitor pump for abnormal noise or vibration for the first 5 minutes of operation.

### 6. Normal Operating Parameters
| Parameter | Normal Range |
|---|---|
| Discharge Flow (FT-101) | 40–50 m3/hr |
| Discharge Pressure | 6.5–7.5 barg |
| Bearing Temperature | < 70 degC |
| Motor Current | < 85% of rated FLA |

### 7. Abnormal Condition Response
- **High vibration or unusual noise:** Stop pump, switch to standby (P-101B), raise a maintenance work order, do not restart until inspected.
- **Loss of suction / cavitation noise:** Check TK-101 level, close discharge valve, stop pump if level below 10%.
- **Bearing temperature > 85 degC:** Trip pump immediately, notify shift supervisor, raise high-priority work order referencing bearing wear history.

### 8. References
- P&ID: Unit 100 Feed Transfer & Heat Exchange Loop, Rev 2
- OISD-STD-105: Safety Requirements in Petroleum Refineries
- Factories Act, 1948, Chapter III (Safety)
- Pump vendor O&M manual (not included in this kit)

---
*This is a synthetic training document created for knowledge base testing purposes.*
