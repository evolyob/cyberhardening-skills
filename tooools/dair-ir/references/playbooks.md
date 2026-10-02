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
- **Domain**: Purdue Model L0-L3 (SCADA, PLC, RTU, Safety Instrumented Systems) & Industrial Conduits
- **Standards Alignment**: IEC 62443-3-1 (Technical Security & Conduit Isolation) / IEC 62443-4-1 (Supply Chain Defect & Patch Remediation)
- **Key Focus**: Maintaining physical process safety margins, enforcing zone/conduit boundaries, deploying passive-first telemetry, and verifying supply chain firmware integrity.
- **Immediate Steps**:
  1. **Zone & Conduit Isolation (IEC 62443-3-1)**: Sever IT-OT DMZ (Level 3.5) jump host connections and non-essential conduits between Level 3 and Level 2.
  2. **Passive-First Telemetry**: Deploy passive network taps and deep packet inspection (DPI) for industrial protocols (Modbus, S7comm, DNP3, EtherNet/IP); strictly prohibit active port scanning on live controller subnets.
  3. **SIS & Physical Safety Lock**: Switch Safety Instrumented Systems (SIS) key switches to physical lock mode and prepare operators for manual fallback (Cyber Safe Position).
  4. **Engineering Workstation (EWS) Isolation**: Disconnect EWS from external networks and use offline verified maintenance tools.
  5. **Supply Chain Defect Handling (IEC 62443-4-1)**: Coordinate vendor CSAF/Advisories against the component SBOM; test and validate all firmware patches in an isolated staging sandbox prior to field deployment.
- **Exit Gates**:
  1. Zone & conduit isolation confirmed with passive telemetry showing zero unauthorized industrial control commands.
  2. PLC/RTU ladder logic and configuration hashes match offline gold baselines 100%.
  3. Safety Instrumented Systems (SIS) and physical interlocking mechanisms verified functional by certified site engineers.
  4. Firmware and security patches verified in staging environment with authentic digital signatures.
  5. Formal tripartite sign-off completed by Plant Operations, Process Control Engineering, and Security Leadership before returning to automated control mode.
