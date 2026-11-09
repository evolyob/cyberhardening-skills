# Security Policy: audit-skill

## Scope
This skill is a local-first code auditing tool. It performs read-only static analysis on paths provided via arguments. It does not upload files, phone home, collect telemetry, or run network services.

## Dependencies
- Standard library prioritized (Python >= 3.14).
- Declared dependencies: `[]` (zero unapproved external packages).
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 50ms) with zero background daemons.

| Command / Flag | Purpose & Boundary |
|---|---|
| `scripts/audit.py <path>` | Full 23-Gate audit (Read-only, default mode) |
| `--security` | Restrict execution to Category 1 (Text & Security Gate only) |
| `--ast` | Restrict execution to Category 3 (Python AST & quality checks only) |
