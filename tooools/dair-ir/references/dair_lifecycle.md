# DAIR Dynamic Lifecycle Specification

## Overview
The Dynamic Approach to Incident Response (DAIR) replaces rigid linear phases with a responsive 8-stage operational loop.

---

## The 8 Operational Stages

### 1. Prepare
- **Objective**: Baseline visibility, sensor health, and communication rosters.
- **Exit Gate**: `telemetry_and_playbooks_verified`.

### 2. Detect
- **Objective**: Triage raw alerts, sensor triggers, and anomaly indicators.
- **Exit Gate**: `initial_alert_and_raw_iocs_captured`.

### 3. Verify & Triage
- **Objective**: Validate true positives, assess impact score, and establish incident classification.
- **Exit Gate**: `severity_and_scope_hypotheses_locked`.

### 4. Scope
- **Objective**: Trace lateral movement, account compromise, and data staging locations.
- **Exit Gate**: `complete_blast_radius_mapped`.

### 5. Contain
- **Objective**: Segment network perimeters, revoke tokens, and isolate infected nodes.
- **Exit Gate**: `adversary_access_severed`.

### 6. Eradicate
- **Objective**: Clean persistent registry keys, web shells, and compromised services.
- **Exit Gate**: `all_persistence_and_malware_removed`.

### 7. Recover
- **Objective**: Restore services from verified clean backups with continuous canary monitoring.
- **Exit Gate**: `production_restored_with_enhanced_monitoring`.

### 8. Debrief
- **Objective**: Formulate post-incident report, update threat models, and refine detection logic.
- **Exit Gate**: `post_incident_report_and_defenses_updated`.
