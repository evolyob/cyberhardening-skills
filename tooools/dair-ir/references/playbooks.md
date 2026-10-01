# Specialized Incident Response Playbooks

## 1. Ransomware Response (Double Extortion)
- **Domain**: Windows Active Directory & File Shares
- **Key Focus**: Preventing data exfiltration and destructive mass-encryption.
- **Immediate Steps**:
  1. Cut network interfaces of infected systems to isolate blast radius.
  2. Invalidate active Domain Admin Kerberos tickets.
  3. Validate immutable backup status prior to recovery attempts.

---

## 2. Cloud Storage & Identity Exfiltration
- **Domain**: Cloud Providers (AWS / Azure / GCP)
- **Key Focus**: Neutralizing stolen IAM keys and unauthorized bucket dumping.
- **Immediate Steps**:
  1. Revoke active STS / OAuth sessions and rotate IAM credentials.
  2. Query CloudTrail / Activity Logs for mass GetObject or download bursts.
  3. Enforce VPC endpoint policies on target storage resources.

---

## 3. Operational Technology (OT / ICS) Handling
- **Domain**: Purdue Model L1-L3 (SCADA, PLC, RTU)
- **Key Focus**: Maintaining safety margins and avoiding process disruption.
- **Immediate Steps**:
  1. Sever IT-OT firewall jump host connections immediately.
  2. Prohibit active port scanning against sensitive industrial controllers.
  3. Coordinate directly with site plant operators before initiating shutdowns.
