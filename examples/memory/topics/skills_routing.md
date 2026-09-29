# Skills & CLI Flag Routing Protocol (`skills_routing.md`)

> **Role**: Authoritative semantic routing matrix mapping single-action user intents to direct, single-flag CLI commands for data ingestion, text sanitization, and anti-AI verification.

---

## 1. Single-Flag Execution Specification

When user request matches a tactical intent, invoke ONLY the exact target command & flag via `run_command`. Never load full multi-step skills or run unnecessary pipeline stages.

### 1. Ingest Engine (`plugins/core-guardrails/scripts/ingest.py`)
- **py Script Path**: `plugins/core-guardrails/scripts/ingest.py`
- **Flag 1 (`--list-only`)**:
  - **Single CLI Command & Flags**: `python3 plugins/core-guardrails/scripts/ingest.py <target> --list-only`
  - **User Semantic Intent**: Probe size, token count, chapter TOC, structure inspection.
  - **Key Benefit & Safety Boundary**: Zero-I/O structural probe; extracts catalog and token estimates without reading full text into context.
- **Flag 2 (`--format stream`)**:
  - **Single CLI Command & Flags**: `python3 plugins/core-guardrails/scripts/ingest.py <target> --format stream`
  - **User Semantic Intent**: Clean web URL / PDF / Docx / XLSX to raw sanitized text stream.
  - **Key Benefit & Safety Boundary**: Strips HTML/layout clutter, normalizes NFKC, and rejoins hyphenated words into a clean stream.
- **Flag 3 (`--split-dir`)**:
  - **Single CLI Command & Flags**: `python3 plugins/core-guardrails/scripts/ingest.py <target> --split-dir <dir>`
  - **User Semantic Intent**: Split large document / logs / books into chapters on disk.
  - **Key Benefit & Safety Boundary**: Physically chunks text into `01_xxx.md` ($\le 800$ lines) and generates `data/index.json` to prevent memory/context overflow.

### 2. Anti-AI Gate (`deep-mod/scripts/noai_gate.py`)
- **py Script Path**: `deep-mod/scripts/noai_gate.py`
- **Flag 1 (`--text`)**:
  - **Single CLI Command & Flags**: `python3 deep-mod/scripts/noai_gate.py --text "<snippet>"`
  - **User Semantic Intent**: Verify single paragraph, sentence, or snippet for AI tells.
  - **Key Benefit & Safety Boundary**: Ephemeral inline scan; checks prohibited buzzwords and formulaic AI patterns without file creation.
- **Flag 2 (`<file_or_dir>`)**:
  - **Single CLI Command & Flags**: `python3 deep-mod/scripts/noai_gate.py <file_or_dir>`
  - **User Semantic Intent**: Verify Markdown file or entire directory before delivery.
  - **Key Benefit & Safety Boundary**: Pre-delivery gate; recursively scans `.md` files and outputs exact line numbers of violations.

---

## 2. Ingest & Dual-Firewall Protocol (6,500 Token Gate)

1. **Pre-flight Probe**: Run `ingest.py <target> --list-only`.
2. **Threshold Gate**:
   - `est_tokens <= 6,500`: Stream clean text directly into main context via `--format stream`.
   - `est_tokens > 6,500`: PROHIBIT full context streaming. Either:
     - Partition on disk via `--split-dir <dir>` and read specific chapter slices.
     - Dispatch a background `research` Subagent to absorb raw chunks in an isolated sandbox.

---

## 3. Subagent vs. Single-Shot Direct Execution

- **Direct Single-Shot Tool Call**: Single-file edits, quick CLI inspections, exact flag queries (< 2s).
- **Subagent Offloading (`invoke_subagent`)**: Multi-file repository audits (> 10 files), external web scraping, iterative test-and-repair tasks, or heavy ingestion where intermediate logs must be isolated from the main context.
