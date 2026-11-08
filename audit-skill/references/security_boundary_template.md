# Security Policy: [skill-name]

## Scope
This skill is a [local tool / network egress tool]. It [reads/writes target files] provided via arguments. It does not upload files, phone home, collect telemetry, or run network services [adjust if egress is explicitly declared].

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[pkg1, pkg2]` (zero unapproved external packages).
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 2s) with zero background daemons.

| Command / Flag | Purpose & Boundary |
|---|---|
| `scripts/<main>.py <arg>` | [Primary action summary; memory/disk boundary] |
| `--<flag> <val>` | [Purpose explanation; path perimeter, safe defaults, no root/env access] |
| `--format [md\|json]` | [Serialization boundary; structured output without filesystem writes] |
