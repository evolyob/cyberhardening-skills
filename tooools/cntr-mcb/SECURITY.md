# Security Policy: cntr-mcb

## Scope
This skill provides automated queries, technical baseline mappings, and compliance checklists for the Financial Container Security Monitoring Baseline (MCB). It operates as a local static analysis and reference tool without network telemetry or destructive capabilities.

## Dependencies
- Standard library prioritized (Python >= 3.10).
- Declared dependencies: `[]` (zero unapproved external packages).
- Zero background daemons or socket listeners.

## Execution
Single-shot ephemeral CLI tool (< 15ms). Read-only in-memory analysis against canonical JSON specifications in `data/`.
- Supported execution flags:
  - `--product`: Filter container security baselines across AWS, Azure, GCP, IBM, Red Hat, and VMware.
  - `--level`: Filter controls by P0 (Critical), P1 (High), P2 (Medium), and P3 (Low) tiers.
  - `--ttp`: Query MITRE ATT&CK for Containers detection logic.
  - `--siem`: Query enterprise SIEM rule queries (Splunk, Sentinel, QRadar, ArcSight).
  - `--format`: Render structured output in `markdown` or `json`.
