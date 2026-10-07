---
name: cntr-mcb
description: Query, audit, and benchmark financial container security baselines across 6 cloud/on-prem platforms (AWS, Azure, GCP, IBM, Red Hat, VMware), MITRE ATT&CK for Containers TTPs, and P0-P3 compliance checklists.
dependencies: []
metadata:
  task_type: cybersecurity-audit
---

# Financial Container Security Monitoring & Configuration Baseline (MCB)

## Objective
Provide authoritative technical baselines, CWPP/CSPM controls, Detection as Code telemetry taxonomies, and P0-P3 compliance checklists for financial institutions deploying containerized workloads.

## Execution Workflow

1. **Intake & Scope Locking**:
   - Determine target platform (`AWS`, `Microsoft`, `GoogleCloud`, `IBM`, `RedHat`, `VMware`) or assessment dimension (`P0`, `P1`, `P2`, `P3`).
   - Query baseline data via deterministic tool:
     ```bash
     python3 scripts/query.py --product <Vendor> --format markdown
     python3 scripts/query.py --level <P0|P1|P2|P3> --format markdown
     ```

2. **Threat & Detection Mapping**:
   - Align runtime anomalies against 36 MITRE ATT&CK for Containers techniques:
     ```bash
     python3 scripts/query.py --ttp <TTP_ID> --format markdown
     python3 scripts/query.py --siem <Platform> --format markdown
     ```

3. **Gap Analysis & Audit Reporting**:
   - Consult canonical synthesis chapters in `chapters/` for deep technical specs and incident remediation architectures.
   - For statutory obligations and official legal terminology, align controls against [Cyber Security Management Act](references/cyber_security_management_act.md).
   - Output structured audit findings and remediation recommendations using active verbs and quantitative criteria.
