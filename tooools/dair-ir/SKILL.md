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
- **Readiness Check**: `python3 <skill_root>/scripts/dair_flow.py --check`

### Step 3: Structured Reporting & Exit Gate Verification
- Format results into concise tables with explicit Exit Gate conditions.
- Reference [references/dair_lifecycle.md](references/dair_lifecycle.md) and [references/playbooks.md](references/playbooks.md) for deep protocols.
