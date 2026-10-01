# Security Policy: sec-intel

## Scope
This skill provides authoritative, evidence-based intelligence lookup for ips, asns, domains, and cves via icann rdap, real dns (dig), and dual-engine euvd/osv. It operates on local files or declared network targets provided via arguments. It does not collect telemetry, run silent daemons, or mutate unauthorized paths.

## Dependencies
- Standard library prioritized (Python >= 3.13).
- Declared dependencies: `[]`.
- Zero silent background installations: package installs require explicit user confirmation.

## Execution
Single-shot ephemeral CLI (< 2s). In-memory execution with explicit outputs directed to designated targets.
- Validated execution flags: `--all`, `--comprehensive`, `--dns`, `--email`, `--json`, `--min-epss`, `--min-score`, `--mxtoolbox`, `--no-tls`, `--selector`, `--size`, `--timeout`, `--vuln`, `--web`.
