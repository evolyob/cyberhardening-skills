---
name: aissm
description: Universal AI security governance framework, cross-standard control harmonization, operational risk taxonomies, and audit intelligence workflows.
dependencies: []
metadata:
  task_type: compliance-mapping
---

# AI Security & Safety Management (AISSM) Framework

## Objective
Provide unified AI governance crosswalks, control harmonization frameworks, threat taxonomies, and multi-standard audit intelligence across enterprise AI lifecycles.

## Execution Workflow

1. **Pre-flight & Registry Query**:
   - Query crosswalk tables: `python3 scripts/query.py --filter <control_id|keyword> --format markdown`.
   - Batch query target controls: `python3 scripts/query.py --batch data/index.json`.

2. **Governance & Architecture Frameworks (Level 2 References)**:
   - **Cross-Framework Harmonization**: Consult `references/cns_iso_harmonization.md` for management structure and control domain mappings.
   - **AI Impact Assessment (AIA) & Risk Tiers**: Consult `references/ai_impact_assessment_guide.md` for 4-tier risk classification and evaluation matrices.
   - **Unified Statement of Applicability (SoA)**: Consult `references/soa_generation_rules.md` for control merging and justification matrices.
   - **AI Threat Defense & Engineering SOPs**: Consult `references/ai_threat_defense_playbook.md` for vulnerability categories and multi-system boundaries.

3. **Domain Knowledge Payloads (Level 3 Chapters - On Demand)**:
   - **Core Governance & Technical Controls**: Reference `chapters/chapter_01_clauses_and_annex_a_mapping.md` through `chapters/chapter_04_data_governance_and_transparency.md`.
   - **Operational Guidance & Supply Chain**: Reference `chapters/chapter_05_annex_b_part1_governance_and_lifecycle.md` and `chapters/chapter_06_annex_b_part2_data_supply_chain_and_ops.md`.
   - **Risk Catalog & Framework Interoperability**: Reference `chapters/chapter_07_annex_c_risks_and_annex_d_integration.md`.
