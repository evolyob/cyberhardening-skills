# Security Policy: audit-skill

## Scope
This skill is a local-first code auditing tool. It performs read-only static analysis on paths provided via arguments. It does not upload files, phone home, collect telemetry, or run network services.

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[]` (zero unapproved external packages).
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 50ms). Read-only in-memory analysis with zero filesystem mutations and zero background daemons.
- Validated execution flags:
  - `--security`: Text security, credential leak, and payload scan only.
  - `--ast`: Python AST syntax, shallow nesting (<= 2), and dependency boundary scan only.
