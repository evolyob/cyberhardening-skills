# Security & Boundary Contract: `dair-ir`

## Scope
- Look up local IR playbooks and query stage gates.
- No network communication, telemetry transmission, or privilege escalation.
- Operates entirely offline using local JSON data definitions.

## CLI Flags
- `--stage`: Query specific DAIR lifecycle stage (1-8 or stage ID).
- `--playbook`: Query specific incident response playbook (ransomware, cloud_exfiltration, supply_chain, ot_ics).
- `--list-chapters`: List all 20 book chapters with metadata.
- `--chapter`: Read specific chapter text by index or keyword.
- `--format`: Structured output format (`markdown`, `json`).
- `--check`: Perform environment and data readiness check.

## Dependencies
- Standard Library: Python 3.10+ (`argparse`, `json`, `pathlib`, `sys`).
- Zero external package dependencies.

## Execution
- Channel: Single-shot ephemeral CLI (< 20ms).
- Max Memory: < 15MB.
- File Access: Read-only access to `<skill_root>/data/` and `<skill_root>/chapters/`.
