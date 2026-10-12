# Core Memory & Template Index

> **Primary Directive**: Read `core.md` and `TASK_STATE.md` at conversation start. Load topic files and templates on-demand. Never dump unprompted.

---

## 0. Session State & Handoff
- **Path**: `TASK_STATE.md`
- **Role**: Active task handoff state, confirmed facts, and pending items (< 30 lines).

---

## 1. Reference Templates (`templates/` - Implementation Contracts & Scaffolds)

### 1. Specification Contract (No-Spec-No-Code)
- **Path**: `templates/spec_template.md`
- **Role**: Phase 0 boundary freezing (Goal/Non-Goals firewalls, Whitelist paths, Zero-EOL deps, Verification command).

### 2. Senior Clean Code Radar (Architecture & Craft)
- **Path**: `templates/senior_coding_laws.md`
- **Role**: 5-step implementation hygiene (Boundary isolation, Pure functional core, Flattened flow <= 2, Useful errors, Subtractive delivery). Reference cases in `templates/senior_coding_examples.md`.

### 3. Senior Clean Code Examples (Practical Cases)
- **Path**: `templates/senior_coding_examples.md`
- **Role**: Empirical Before/After case studies for `senior_coding_laws.md` (Path traversal prevention, pure core, guard clauses, error chaining, subtractive engineering).

### 4. Security Boundary Policy Scaffold
- **Path**: `templates/security_boundary.template.md`
- **Role**: Standard policy scaffold declaring skill execution boundaries (Scope, Dependencies, Execution) for `SECURITY.md`.

### 5. Reverse Reconstruction Contract
- **Path**: `templates/recon_spec.template.md`
- **Role**: Clean-room reverse engineering & behavioral parity verification matrix.

---

## 2. Active Domain Topics (`topics/`)

### 1. Agent Skill & Security Architecture Guide
- **Domain**: 5-Step Skill Build Flow, Progressive Disclosure & Data Indexing, Cryptographic Primitives, CIS/OWASP Compliance, Zero-EOL Runtimes
- **Topic Path**: `topics/agent_skill_architecture.md`
- **Keywords / Triggers**: Skill Build, Spec First, Progressive Disclosure, Data Indexing, Test Anchors, Security Compliance, Cryptography, OWASP, ASVS, CIS Benchmarks, PEP 594

### 2. Threat Intelligence Reporting Checklist
- **Domain**: Security Intelligence, CYFIRMA DeTCT Analysis
- **Topic Path**: `topics/cyfirma_detct_checklist.md`
- **Keywords / Triggers**: CYFIRMA, DeTCT, Threat Report, Phishing, Dark Web Leaks, Domain Reputation

### 3. Teams Automation & Archiving Playbook
- **Domain**: Teams Graph API, Unstructured Data Extraction, Excel Archiving
- **Topic Path**: `topics/teams_power_automate_scan.md`
- **Keywords / Triggers**: Teams Scan, 更版掃描統計表, Graph API Beta, Manual Confirmation, Thread Replies

### 4. Visual Layout Skeletons
- **Domain**: High-Density Markdown Layouts, Bento Cards, Comparison Tables, Mermaid Topologies
- **Topic Path**: `topics/visual_layout.md`
- **Keywords / Triggers**: Layout Skeletons, Bento Grid, Visual Skeletons, Architecture Topology, Strategy Cards

### 5. Engineering & System Governance Protocol
- **Domain**: Pre-Delivery Machine Verification, Anti-Whack-a-Mole Structural Gates, Deterministic Large-Input Probing, Data Quarantine
- **Topic Path**: `topics/system_governance.md`
- **Keywords / Triggers**: System Governance, Machine Verification, Measure-Not-Assert, REPL Probing, Large File Handling, Quarantine

### 6. Skills & CLI Flag Routing Protocol
- **Domain**: Semantic-to-Flag Routing, Ingest Token Gates (6,500), AST Code Audit, Anti-AI Verification, Subagent Offloading, Deep Grill Spec Alignment
- **Topic Path**: `topics/skills_routing.md`
- **Keywords / Triggers**: Skills Routing, Flag Lookup, Ingest Probe, AST Audit, Frontend Audit, Anti-AI Gate, Subagent Dispatch, Ingest Token Gate, Deep Grill, Spec Alignment, Tracer-Bullet DAG
