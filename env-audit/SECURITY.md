# Security Policy: env-audit

## Scope
This skill provides audit os binaries, cves, eol risks, upstream versions, and generate upgrade commands. It operates on local files or declared network targets provided via arguments. It does not collect telemetry, run silent daemons, or mutate unauthorized paths.

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[]`.
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 2s). In-memory execution with explicit outputs directed to designated targets.
- Validated execution flags:
  - `--json`: Execution option.
  - `--quiet`: Execution option.
  - `--upgradable`: Execution option.
  - `--version`: Execution option.
