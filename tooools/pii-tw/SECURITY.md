# Security Policy: pii-tw

## Scope
This skill provides Taiwan Personal Data Protection Act (PDPA) and CDPSE engineering compliance analysis. It operates exclusively on local reference files and JSON datasets without network access, telemetry, or file system modifications.

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[]`.
- Zero external package installations.

## Execution
Single-shot ephemeral CLI (< 1s). Read-only in-memory queries with structured outputs.
- Validated execution flags: `--article`, `--cdpse`, `--check`, `--format`, `--list`, `--measure`.
