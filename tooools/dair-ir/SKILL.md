---
name: dair-ir
description: Guide dynamic cybersecurity incident response across 8 operational stages and specialized playbooks (ransomware, cloud exfiltration, OT/ICS).
dependencies: []
metadata:
  task_type: open-ended
---

# Dynamic Incident Response Engine (DAIR)

## Objective
Provide fast, evidence-grounded incident response guidance across the 8-stage DAIR lifecycle and domain-specific playbooks.

---

## Execution Workflow

### Step 1: Work Shape & Explicit Skill Lock
- **Explicit Skill Lock**: If the user targets specific IR activities (e.g. ransomware isolation, OT DMZ severed), lock `dair-ir` as the authoritative Primary.
- **Work Shape**:
  - **Single**: Query single stage exit criteria or specific playbook steps.
  - **Phased**: Multi-step triage flow (Detect -> Contain -> Eradicate -> Recover).

### Step 2: Query Stage or Playbook
Run the target command with a single tool call:
- **Full Lifecycle Overview**: `python3 <skill_root>/scripts/dair_flow.py`
- **Specific Stage**: `python3 <skill_root>/scripts/dair_flow.py --stage <stage_id>`
- **Specialized Playbook**: `python3 <skill_root>/scripts/dair_flow.py --playbook <ransomware|cloud_exfiltration|ot_ics>`
- **Chapter Index & Content**: `python3 <skill_root>/scripts/dair_flow.py --list-chapters` or `--chapter <id>`
- **Readiness Check**: `python3 <skill_root>/scripts/dair_flow.py --check`

### Step 3: Structured Reporting & Exit Gate Verification
- Format results into concise tables with explicit Exit Gate conditions.
- Reference [references/dair_lifecycle.md](references/dair_lifecycle.md) and [references/playbooks.md](references/playbooks.md) for deep protocols.

---

## Chapter & Playbook Reference Index
- **Chapter 1-16**: Core DAIR Lifecycle & Foundations
- **Chapter 17**: [Ransomware & Double Extortion](chapters/chapter_17_ransomware.md)
- **Chapter 18**: [Cloud Systems IR](chapters/chapter_18_cloud_ir.md)
- **Chapter 19**: [OT/ICS Operational Technology IR](chapters/chapter_19_ot_ics.md)
- **Chapter 19-2**: [IEC 62443-3-1 Technical Security & Conduit Telemetry](chapters/chapter_19-2_ot_62443_3_1_tech.md) (Zone/Conduit isolation, passive telemetry, DPI, containment runbooks)
- **Chapter 19-3**: [IEC 62443-4-1 Secure Development & Defect Remediation](chapters/chapter_19-3_ot_62443_4_1_sdlc.md) (Supply chain defect notifications, CSAF ingestion, staging regression validation, recovery exit gates)
- **Chapter 20**: [NIST CSF 2.0 Integration](chapters/chapter_20_nist_csf.md)
