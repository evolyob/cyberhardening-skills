# Security Policy (`SECURITY.md`)

## Scope
This skill provides deterministic cross-standard analysis, control crosswalks, and reference mappings between ISO/IEC 42001 (AIMS) and ISO/IEC 27002:2022. All operations are local-first, offline-capable, and read-only.

## Dependencies
- Standard Python 3.10+ runtime with stdlib modules (`argparse`, `json`, `pathlib`, `re`, `sys`).
- Zero external package dependencies, zero network sockets, and zero background daemons.

## Execution
- CLI tools in `scripts/` and `tests/` execute ephemerally with execution latency < 50ms.
- Tool operations adhere to strict AST hygiene: maximum block nesting <= 2, early returns, explicit encoding (`utf-8-sig`), and zero dynamic evaluations (`eval`/`exec`).
