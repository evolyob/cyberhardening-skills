# Security Policy: asset-risk

## Scope
This skill provides categorize information assets, assign canonical threat-vulnerability pairs from parameters. It operates on local files or declared network targets provided via arguments. It does not collect telemetry, run silent daemons, or mutate unauthorized paths.

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[]`.
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 2s). In-memory execution with explicit outputs directed to designated targets.
- Validated execution flags: `--batch`, `--cat`, `--drill`, `--format`, `--high-risk-file`, `--name`, `--pair-id`, `--param-path`, `--pii`, `--pii-inventory`, `--pii-param-path`, `--threat`, `--type`, `--vuln`.
