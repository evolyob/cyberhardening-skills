# Statutory Reference: Cyber Security Management Act (CSMA)

> Source: Ministry of Digital Affairs (數位發展部) official English statutory translation.
> Pcode: A0030297 | Amended Date: 2025-09-24

---

## 1. Official Statutory Terminology

- **Information and Communication Systems**: Any system used for collecting, controlling, transmitting, storing, circulating, or deleting information, or for processing, using, or sharing information (Article 3, Item 1).
- **Information and Communication Services**: Any services relating to the collection, control, transmission, storage, circulation, deletion, processing, use, or sharing of information (Article 3, Item 2).
- **Cyber Security**: Prevention of unauthorized access to, use of, control over, disclosure of, damage to, alteration of, or destruction of information or systems, safeguarding confidentiality, integrity, and availability (Article 3, Item 3).
- **Cyber Security Incident**: Any event where a potential violation of cyber security policy or failure of protective measures affects system functionality (Article 3, Item 4).
- **Specific Non-Government Agency**: Critical infrastructure providers, government-owned enterprises, designated foundations, and government-controlled institutions (Article 3, Item 6).
- **Critical Infrastructure Provider**: Entities maintaining or operating critical infrastructure designated by sector competent authorities (Article 3, Item 8).
- **Products Harmful to National Cyber Security**: ICT systems, services, or products posing direct or indirect risk to national security (Article 3, Item 11).

---

## 2. Statutory Obligations for Containerized Environments

### Article 16 (Cyber Security Maintenance Plan & Responsibility Levels)
Specific non-government agencies shall draft, implement, and periodically review a **Cyber Security Maintenance Plan** in accordance with assigned responsibility levels (Levels A/B/C):
- Implement mandatory technical controls mapped to container baselines (P0-P3 tiers).
- Maintain dedicated cyber security personnel and certified auditor oversight.

### Article 17 (Specific Non-Government Agency Audits)
Central competent authorities shall periodically audit the implementation of Cyber Security Maintenance Plans:
- Review CSPM automated compliance logs and CIS benchmark conformance.
- Verify container runtime defense (CWPP) and immutable audit log retention.

### Article 18 (Incident Notification, Containment & Reporting)
Upon discovery of a **Cyber Security Incident**:
- Notify central competent authority within statutory deadlines (e.g. 1 hour for severe classifications).
- Implement containment measures, preserve forensic telemetry, and submit post-incident investigation reports.

---

## 3. Container MCB Technical Mapping Matrix

| Statutory Mandate | CSMA Article | Container MCB Technical Control | Telemetry / Verification |
| :--- | :--- | :--- | :--- |
| **System Integrity & Protection** | Art. 3, 16 | P1: Container Breakout & Privilege Escalation Blocker | eBPF Syscall Runtime Telemetry |
| **Audit Log Retention (>= 1 Year)** | Art. 16, 17 | P0: Kubernetes API Audit & Runtime Event Streaming | Centralized Immutable SIEM Sink |
| **Incident Response & Traceability** | Art. 18 | T1036-T1613: 36 MITRE ATT&CK for Containers TTPs | Sigma Rules & Automated Containment |
| **Supply Chain & Harmful Products** | Art. 3(11) | P2: Image Admission Control & Signature Verification | Cosign / Notary / Registry Whitelist |
