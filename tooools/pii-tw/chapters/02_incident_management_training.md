# Chapter 02: Incident Response, Business Continuity (BCP/DR) & Privacy Awareness

## 1. Statutory Baseline & Operational Resilience
- **PDPA Statutory Article 12**: Mandatory obligation to investigate and notify data subjects in an appropriate manner upon discovery of personal data breach.
- **PDPA Enforcement Rules Art 12 Para 2 Item 4**: Incident prevention, reporting, and emergency response mechanisms.
- **PDPA Enforcement Rules Art 12 Para 2 Item 7**: Structured education and awareness training programs.
- **Privacy & Risk Engineering Framework**: Risk Governance Incident Management, Business Continuity (BIA, RTO, RPO) & Privacy Engineering Awareness Metrics.

### 1.1 Standard 6-Phase Incident Response Lifecycle
```
┌─────────────────┐     ┌─────────────────────┐     ┌────────────────────────┐
│ 1. Preparation  │ ──> │ 2. Detection/Analysis│ ──> │ 3. Containment (FIRST) │
└─────────────────┘     └─────────────────────┘     └───────────┬────────────┘
                                                                │
┌─────────────────┐     ┌─────────────────────┐                 │
│6. LessonsLearned│ <── │   5. Recovery       │ <── 4. Eradication ◄
└─────────────────┘     └─────────────────────┘
```

1. **Preparation**: Stand up the Computer Security Incident Response Team (CSIRT), establish communication channels, deploy forensic toolkits, draft dual-track breach notification templates.
2. **Detection & Analysis**: Correlate SIEM/EDR telemetry to identify indicators of compromise (IoCs), determine blast radius, classify compromised data schema types.
3. **Containment (Absolute Operational Priority)**: Enforce network micro-segmentation, revoke compromised authentication tokens, freeze compromised virtual machines. **Containment precedes all public disclosures, root cause debugging, and system rebuilds**.
4. **Eradication**: Identify and neutralize root-cause vulnerabilities, remove malicious implants, rotate all service credentials.
5. **Recovery**: Restore operations from verified immutable WORM backups, validate data integrity, implement enhanced monitoring.
6. **Lessons Learned (Post-Incident Review)**: Document root cause, re-calibrate KRI/KCI thresholds, update incident runbooks.

### 1.2 Business Impact Analysis (BIA) & Disaster Recovery Targets
When designing disaster recovery and backup resilience for personal data systems:
- **Business Impact Analysis (BIA)**: Quantifies financial, operational, and regulatory impacts resulting from system disruptions or data loss.
- **Recovery Time Objective (RTO)**: The maximum acceptable duration of system downtime before critical operations must be restored.
- **Recovery Point Objective (RPO)**: The maximum acceptable data loss tolerance measured in time (e.g. max 15 minutes of transactional data loss).
- **Privacy Synchronization**: Disaster recovery sites and restored database replicas must strictly maintain identical encryption keys, IAM access restrictions, and crypto-shredding deletion synchronization as primary production clusters.

### 1.3 Dual-Track Notification Timelines & Forensics Chain of Custody
| Dimension | Competent Authority Track | Data Subject Notification Track | Forensic Chain of Custody Standard |
| :--- | :--- | :--- | :--- |
| **Trigger Criteria** | Confirmed compromise of sensitive PII or large-scale customer records. | Confirmed breach impacting rights, privacy, or financial standing of natural persons. | Volatile memory capture, disk bit-stream imaging (E01/DD), cryptographic hash sealing (SHA-256). |
| **Statutory SLA** | Preliminary notification within **72 hours** of breach confirmation. | Notification dispatched without undue delay following technical containment. | Secure evidence locker with timestamped access logging and non-repudiation controls. |
| **Mandatory Content** | Incident timeline, scope of affected PII, technical containment actions, remedial roadmap. | Breach nature, compromised data fields, self-protection steps, official support contact details. | Complete custody transfer ledger verifying that original forensic images remain unaltered. |

### 1.4 Security Awareness Training Engineering
- **KPI vs KCI**: Course attendance completion rate (KPI) reflects administrative compliance; simulated phishing click rate reduction and immediate report rates (KCI) prove behavioral resilience.
- **Role-Based Curriculum**: Tailored modules for software developers (secure coding, synthetic test data), system admins (privileged credential hygiene, WORM logs), and business operators (social engineering recognition).

---

## 2. Production Scenario: Ransomware Outage & BCP/DR Synchronization
- **Incident Overview**: Attackers compromised an internal developer jump box, exfiltrated 500,000 patient records, encrypted production database clusters, and corrupted local transaction logs.
- **Operational Failure**: Infrastructure engineers attempted to reboot database nodes and contacted external PR before isolating infected network segments, allowing ransomware to spread across additional subnets.
- **Remediation Architecture**:
  1. CSIRT executed immediate containment: segmented core VLANs, isolated infected virtual clusters, revoked all Active Directory service accounts.
  2. Activated Business Continuity Plan (BCP): failed over to an isolated disaster recovery cluster with pre-validated RTO <= 2 hours and RPO <= 15 minutes.
  3. Submitted preliminary breach filings to regulatory authorities within 48 hours, and issued authenticated SMS notifications with one-time verification links to affected patients.

---

## 3. Scenario Practice & Decision Forensics (Q&A) & Distractor Forensics

### Q1 `[Privacy Engineering - FIRST]`
Monitoring systems detect that an internal database host is actively streaming unencrypted personal data to an unknown external IP address. What is the Incident Response Team's FIRST action?
- A. Transmit a formal breach notification to the supervisory regulatory authority
- B. Isolate the affected host from the network to contain data exfiltration
- C. Convene an executive press conference to brief external media outlets
- D. Trigger an immediate full restore of database clusters from tape backups

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In incident response engineering standards, containment is the absolute first action (FIRST) to halt active data loss and restrict blast radius.
> - **Why A, C, D are Incorrect**: External reporting and system restoration cannot proceed before achieving verified technical containment.

### Q2 `[Privacy Engineering - PRIMARY]`
When establishing Disaster Recovery (DR) requirements for a database holding critical customer personal data, what is the PRIMARY purpose of defining a Recovery Point Objective (RPO)?
- A. Determine the maximum allowable duration of system downtime following a disaster
- B. Determine the maximum acceptable amount of data loss measured in time between the last backup and the disruptive event
- C. Establish the total financial budget allocated for purchasing backup storage hardware
- D. Specify the physical travel distance between the primary data center and secondary recovery facility

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: RPO defines data loss tolerance measured in elapsed time.
> - **Why A is Incorrect**: Maximum allowable downtime is defined by the Recovery Time Objective (RTO).
> - **Why C and D are Incorrect**: Budget allocation and physical distance are implementation constraints, not the definition of RPO.

### Q3 `[Privacy Engineering - MOST]`
When evaluating the effectiveness of enterprise anti-phishing and privacy training programs, which metric serves as the MOST reliable Key Control Indicator (KCI)?
- A. Annual training course attendance completion percentage exceeding 95%
- B. Statistically significant reduction in simulated phishing click rates coupled with increased reporting rates
- C. Percentage of allocated annual training budget expended
- D. Overall employee satisfaction survey scores post-training

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: KCIs measure control effectiveness. Simulated phishing behavior directly demonstrates operational risk reduction.
> - **Why A, C, D are Incorrect**: Attendance, budget tracking, and satisfaction scores measure administrative volume or sentiment, not defensive resilience.

### Q4 `[Privacy Engineering - NEXT]`
Following the technical containment of a confirmed ransomware infection and verification of system eradication, what is the NEXT operational phase?
- A. Decommission and physically shred all server motherboards
- B. Restore systems from verified clean backups and perform integrity validation before returning to service
- C. Terminate the employment contracts of all users who clicked phishing links
- D. Delete all incident-related SIEM logs to conserve storage space

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: After containment and eradication, the recovery phase follows, restoring operations from clean backups and validating data integrity.
> - **Why A, C, D are Incorrect**: Physical destruction is unnecessary; punitive terminations do not advance recovery; deleting logs destroys evidence.
