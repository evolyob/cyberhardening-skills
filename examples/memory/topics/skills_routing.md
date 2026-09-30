# Cross-Skill Semantic Routing Protocol (`skills_routing.md`)

> **Rule**: Macro-routing only. Maps user scenario intents and trigger keywords to target skill groups. Micro-level CLI flags, parameters, and execution contracts MUST remain encapsulated in each skill's local `SECURITY.md`.

---

## 1. Single-Flag Execution Specification

When user request matches a tactical intent, invoke ONLY the exact target command & flag via `run_command`. Never load full multi-step skills or run unnecessary pipeline stages.

## 1. Cross-Skill Capabilities & Semantic Routing Matrix

| User Scenario | Intent & Trigger Keywords | Target Skill / Plugin | Execution Channel | Local Security Contract |
| :--- | :--- | :--- | :--- | :--- |
| **Code & Skill Quality Audit** | AST audit, line budget, spec compliance, security gates, 4-backtick balance | **`audit-skill`** | Single-shot CLI (< 2s) | `~/.gemini/skills/audit-skill/SECURITY.md` |
| **Anti-AI Detox & Standup Voice** | Anti-AI tone, standup voice, buzzwords, formulaic patterns, meeting chunking | **`noai-note`** | In-memory scan | `~/.gemini/skills/noai-note/SECURITY.md` |
| **Deep Research & Skill Extraction** | Deep research, architecture review, extract skill, pipeline distillation | **`deep-mod`** | Multi-stage pipeline | `~/.gemini/skills/deep-mod/SECURITY.md` |
| **Socratic Interview & Plan Challenge** | Grill me, challenge plan, hidden assumptions, edge case validation | **`deep-grill`** | Interactive 1-by-1 | `~/.gemini/skills/deep-grill/SECURITY.md` |
| **Host Security & Binary EOL Audit** | Host OS, binary EOL, CVE lookup, package manager version check | **`env-audit`** | Host discovery JSON | `~/.gemini/skills/env-audit/SECURITY.md` |
| **PDF Engineering & Manipulation** | PDF extract, OCR, merge, split, ReportLab canvas, A4 layout | **`pdf`** | Tool priority matrix | `~/.gemini/skills/pdf/SECURITY.md` |

---

## 2. Ingest Token Circuit Breaker (6,500 Token Gate)

1. **Pre-flight Probe**: Run ingestion probe on target document/stream.
2. **Threshold Gate**:
   - `est_tokens <= 6,500`: Stream sanitized text directly into primary context.
   - `est_tokens > 6,500`: Prohibit full context streaming. Either:
     - Partition on disk into chapter slices (`01_xxx.md`, $\le 800$ lines).
     - Dispatch background `research` subagent to absorb raw chunks in an isolated sandbox.

---

## 3. Dispatch Channel Strategy

- **Direct Single-Shot Tool Call**: Single-file edits, quick CLI audits, exact flag executions (< 2s).
- **Subagent Offloading (`invoke_subagent`)**: Multi-file repository audits (> 10 files), external web research, iterative test-and-repair tasks, or large ingest processing.
