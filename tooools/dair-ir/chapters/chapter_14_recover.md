# Chapter 14: Recover Activity: Safe Restoration & Canary Validation

> Source: PDF Pages 401-429 (Total Pages: 29)

◦ Test patches in a non-production environment before broad deployment.

2. Implement patch management during eradication, including:

◦ Track patch status with inventory management tools.

◦ Balance change management procedures with the urgency of eradication.

◦ Consider phased rollout for large environments.

◦ Verify system functionality after patching.

3. Address unpatchable systems, including:

◦ Implement compensating controls (network segmentation, enhanced monitoring).

◦ Document compensating controls as temporary measures requiring review.

◦ Establish a timeline for system replacement or upgrade.

◦ Include unpatchable systems in ongoing vulnerability management tracking.

4. Conduct broader vulnerability assessment, including:

◦ Scan the environment for related vulnerabilities beyond the immediate incident scope using

vulnerability assessment tooling.

◦ Review configuration hardening against CIS Benchmarks or similar standards.

◦ Enumerate accessible services using port scanning or local service enumeration and disable

unnecessary services.

◦ Review network device configurations for overly permissive firewall rules, obsolete entries, and

unnecessary exposure.

◦ Disable unnecessary remote access services such as Telnet, FTP, RDP, and SMB unless explicitly

required.

Step 7. Address Eradication Challenges

1. Investigate living-off-the-land techniques, including:

◦ Review use of legitimate built-in system utilities commonly abused for living-off-the-land

techniques.

◦ Analyze command-line arguments for administrative tools.

◦ Establish baselines for normal administrative tool usage.

◦ Implement enhanced logging for commonly abused utilities.

2. Address fileless malware, including:

◦ Focus memory analysis on identifying injected code and reflective loading.

◦ Review script execution logs (PowerShell Script Block Logging, WMI traces).

◦ Examine registry-resident malware and WMI persistence.

◦ Clear memory-resident threats through controlled system restarts.

3. Investigate legitimate remote access tool abuse, including:

◦ Audit installed remote monitoring and management (RMM) tools.

◦ Identify unauthorized installations of remote access utilities commonly leveraged by attackers.

◦ Review authorized tool configurations for unauthorized access grants.

◦ Implement allowlisting to prevent the unauthorized installation of remote access tools.

4. Address cross-trust boundary persistence, including:

◦ Enumerate forest trusts, external trusts, and federated identity relationships.

◦ Review authentication logs in trusted environments for suspicious cross-boundary activity.

◦ Coordinate eradication with administrators of trusted domains and identity providers.

◦ Verify removal of cross-boundary artifacts in all affected environments.

Eradicate Activity | Chapter 13 | 377

Step 8. Validate Eradication Success

1. Verify persistence mechanism removal, including:

◦ Re-scan systems for indicators of compromise identified during the investigation.

◦ Confirm scheduled tasks, services, and registry entries are removed.

◦ Validate account remediation by monitoring authentication logs.

◦ Test that blocked network indicators generate alerts if accessed.

2. Monitor for signs of continued attacker activity, including:

◦ Watch for authentication attempts using revoked credentials.

◦ Monitor network traffic for connections to known attacker infrastructure.

◦ Review process creation logs for suspicious execution patterns.

◦ Implement canary files or honeypot credentials to detect residual access.

3. Confirm vulnerability remediation, including:

◦ Verify patches are successfully installed on affected systems.

◦ Test compensating controls for unpatchable systems.

◦ Validate that configuration hardening changes are in effect.

◦ Confirm the initial access vector is closed.

Step 9. Document Eradication Actions

1. Record investigation findings, including:

◦ Document identified indicators of compromise and persistence mechanisms.

◦ Record root cause analysis results and contributing factors.

◦ Capture timeline of attacker activity reconstructed from evidence.

◦ Note any gaps in evidence or areas requiring further investigation.

2. Document remediation actions, including:

◦ Record each persistence mechanism removed with a timestamp and method.

◦ Document credential resets, including accounts, timing, and coordination.

◦ Capture system restoration decisions and validation results.

◦ Record vulnerability patches applied and compensating controls implemented.

3. Communicate eradication status to stakeholders, including:

◦ Provide an executive summary of eradication activities and outcomes.

◦ Deliver technical briefings to IT teams responsible for ongoing monitoring.

◦ Coordinate with legal and compliance on documentation requirements.

◦ Prepare handoff documentation for recover activity follow-on work.

4. Capture eradicate-phase feedback for the debrief consolidation, including:

◦ Document detection gaps that allowed initial compromise.

◦ Note investigation challenges and tool limitations encountered during eradication.

◦ Surface security control gaps and playbook gaps revealed during eradication; debrief Step 8

converts these into prioritized organizational improvements rather than each phase implementing

them independently.

[1] Barnhart, Heather, "Inside the Five Most Dangerous New Attack Techniques" RSAC Webcast, 2025, www.youtube.com/watch?

v=JrmYKm0tihk&t=2093s

[2] Fishbone Diagram, Lean Six Sigma Definition, www.leansixsigmadefinition.com/glossary/fishbone-diagram/

[3] The Five Whys technique is attributed to Sakichi Toyoda, founder of what later became Toyota Industries. See en.wikipedia.org/

wiki/Sakichi_Toyoda.

[4] Sigma HQ - Generic Signature Format for SIEM Systems, sigmahq.io/

[5] Hayabusa - Windows Event Log Fast Forensics Timeline Generator, github.com/Yamato-Security/hayabusa

[6] HIPAA Journal, "Rhode Island RIBridges System Hack," www.hipaajournal.com/rhode-island-ri-bridges-system-hack/

[7] State of Rhode Island, "RIBridges Investigation Summary," May 2025, admin.ri.gov/sites/g/files/xkgbur536/files/2025-05/

RIBridges%20Investigation%20Summary%20FINAL%20-%20External%20Release.pdf

[8] HIPAA Journal, "Rhode Island RIBridges System Hack," www.hipaajournal.com/rhode-island-ri-bridges-system-hack/

[9] Rhode Island Current, "Deloitte Reaches $6.3M Deal to Settle Class Action Lawsuit in RIBridges Data Breach," October 17, 2025,

rhodeislandcurrent.com/2025/10/17/deloitte-reaches-6-3m-deal-to-settle-class-action-lawsuit-in-ribridges-data-breach/

[10] Kyocera Document Solutions, "Security Advisory: Vulnerabilities in KfeCoSvc Driver," August 29, 2023,

www.kyoceradocumentsolutions.com/en/our-business/security/information/2023-08-29.html

[11] VPC Flow Log Analysis, github.com/joswr1ght/vpc-flow-log-analysis/tree/master

[12] FBI Internet Crime Complaint Center, "Business Email Compromise: The $55 Billion Scam," September 2024, www.ic3.gov/PSA/

2024/PSA240911

[13] Microsoft, "Detect and Remediate Illicit Consent Grants," learn.microsoft.com/en-us/defender-office-365/detect-and-

remediate-illicit-consent-grants

[14] KnowBe4, "How a North Korean Fake IT Worker Tried to Infiltrate Us," July 2024, blog.knowbe4.com/how-a-north-korean-fake-it-

worker-tried-to-infiltrate-us

[15] GitLab, "GitLab discovers widespread npm supply chain attack," about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-

chain-attack/

[16] Nelson, Nate, "Marquis v. SonicWall Lawsuit Ups the Breach Blame Game," Dark Reading, February 2026, www.darkreading.com/

cloud-security/marquis-sonicwall-lawsuit-breach-blame-game

[17] U.S. Department of Justice, "Leader of Massive Scheme to Traffic in Fraudulent and Counterfeit Cisco Networking Equipment

Sentenced to Prison," May 2024, www.justice.gov/archives/opa/pr/leader-massive-scheme-traffic-fraudulent-and-counterfeit-

cisco-networking-equipment

[18] Janushkevich, Dmitry, "The Fake Cisco: Hunting for backdoors in Counterfeit Cisco devices," F-Secure Labs, July 2020,

labs.withsecure.com/publications/the-fake-cisco

[19] Salesloft, "Drift Integrations," September 2025, help.salesloft.com/s/topic/0TOPD0000002N2C4AU/drift-integrations

[20] Google Threat Intelligence, "Data Theft from Salesforce Instances via Salesloft’s Drift Third-Party Application," August 2025,

cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift

[21] Krebs on Security, "The Ongoing Fallout from a Breach at AI Chatbot Maker Salesloft," September 2025, krebsonsecurity.com/

2025/09/the-ongoing-fallout-from-a-breach-at-ai-chatbot-maker-salesloft/

[22] s3logparse - S3 Access Log Parser, github.com/joswr1ght/s3logparse

[23] Microsoft Security Response Center, "Microsoft Actions Following Attack by Nation State Actor Midnight Blizzard," January 2024,

msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/

[24] Wiz Research, "Midnight Blizzard breach: analysis and best practices," January 2024, www.wiz.io/blog/midnight-blizzard-

microsoft-breach-analysis-and-best-practices

[25] Microsoft, "Tier model for partitioning administrative privileges," learn.microsoft.com/en-us/microsoft-identity-manager/pam/

tier-model-for-partitioning-administrative-privileges

[26] Microsoft, "Planning for compromise," Windows Server AD DS security best practices, learn.microsoft.com/en-us/windows-

server/identity/ad-ds/plan/security-best-practices/planning-for-compromise

[27] Medin, Tim, "Kerberos 101," Red Siege, April 2020, www.redsiege.com/wp-content/uploads/2020/04/20200430-kerb101.pdf

[28] Microsoft, "Security posture assessments - Accounts," Microsoft Defender for Identity, learn.microsoft.com/en-us/defender-for-

identity/security-posture-assessments/accounts

[29] Reddit r/cybersecurity, "Cached credentials and long-lived tokens," www.reddit.com/r/cybersecurity/comments/1gy6ynf/

comment/lyosx5d/

[30] CISA, "Known Exploited Vulnerabilities Catalog," www.cisa.gov/known-exploited-vulnerabilities-catalog

[31] CVE-2025-64446, www.cve.org/CVERecord?id=CVE-2025-64446

[32] Qi, Ryan et al., "WAFFLED: Exploiting Parsing Discrepancies to Bypass Web Application Firewalls," arXiv, March 2025, arxiv.org/

abs/2503.10846

[33] Prajapati, Pranav, "XSS: Bypassing Cloudflare WAF with a Simple Trick," Medium, 2025, medium.com/%40pranavrp77/xss-

bypassing-cloudflare-waf-with-a-simple-trick-12aff8ce87c7

[34] SOCRadar, "Cloudflare Protection Bypass Vulnerability on Threat Actors' Radar," 2023, socradar.io/blog/cloudflare-protection-

bypass-vulnerability-on-threat-actors-radar/

[35] Claroty Team82, "JS-ON Security: Off - Abusing JSON-Based SQL to Bypass WAF," 2022, claroty.com/team82/research/js-on-

security-off-abusing-json-based-sql-to-bypass-waf

[36] CIS Benchmarks - Security Configuration Guides, www.cisecurity.org/cis-benchmarks

Eradicate Activity | Chapter 13 | 379

[37] CISA, "#StopRansomware: Akira Ransomware," April 2024, www.cisa.gov/news-events/cybersecurity-advisories/aa24-109a

[38] ThreatDown, "Akira ransomware drops AnyDesk client on compromised systems," www.threatdown.com/blog/akira-

ransomware-drops-anydesk-client-on-compromised-systems/

14 Recover Activity

The recover activity represents the transition from eliminating threats to restoring normal operations. This

activity leverages insights from detection, scoping, containment, and eradication activities to test and

validate systems before bringing them back into production.

Recovery is not only removing containment measures and reactivating systems. Rather, it is an orchestrated

process that ensures restored systems are secure, functional, and ready to support operations before

returning them to production.

Figure 122 | Recover Activity Waypoint

The recover activity balances competing pressures: the urgency to restore operations against the need for

thorough validation to prevent recompromise. Organizations that rush recovery without proper validation

risk responding to ongoing threats when attackers exploit the same vulnerabilities or persistence

Recover Activity | Chapter 14 | 381

mechanisms that survived eradication. Conversely, organizations that delay recovery excessively compound

the incident’s impact and frustrate stakeholders who depend on affected systems.

This chapter explores the objectives of recovery, strategies for returning systems to production, and the

challenges that complicate the restoration process. It also covers practical techniques for system validation,

enhanced monitoring configuration, and coordinated restoration before looking at activity examples.

RECOVERY OBJECTIVES

The recover activity serves several distinct objectives to ensure that systems return to production in a

controlled, validated manner. These objectives guide incident response teams through the final stages of

active response, setting the stage for the organization to resume normal operations with confidence that

the incident has been resolved.

In this section, we’ll work through the objectives that structure recovery work: pre-restoration verification,

system validation testing, and system owner acceptance. We’ll also cover enhanced monitoring

configuration, coordinated production restoration, containment action removal, and metrics capture to

inform post-incident review.

Pre-Restoration Verification

Before any system returns to production, responders should verify that eradication efforts were successful

and that the conditions enabling the original compromise have been addressed. This verification serves as a

validation during the transition from the eradicate activity, preventing premature restoration that could

lead to rapid recompromise.

Pre-restoration verification allows the organization to confirm that the incident’s root

causes have been remedied before putting systems back into production.

Table 32 provides a reference for pre-restoration verification activities.

Table 32 | Pre-Restoration Verification Checklist

VERIFICATION AREA VERIFICATION ACTIVITIES

Root Cause

Remediation

Confirm vulnerability patched, credentials rotated, or misconfiguration

corrected based on incident root cause analysis

System Patching Apply outstanding operating system, firmware, and application patches

beyond the root-cause remediation so restored systems return to production

with current security updates

Persistence Removal Verify all identified persistence mechanisms have been removed from the

system

Backup Validation For backup restorations, confirm backup predates initial compromise using

incident timeline

VERIFICATION AREA VERIFICATION ACTIVITIES

Rebuild Verification For rebuilt systems, verify rebuild used trusted sources and clean installation

media

Security Control

Status

Confirm EDR agents installed and reporting, host firewall configured, logging

enabled

IOC Scanning Scan restored system for indicators of compromise discovered during

scoping and eradication, performed last so the scan reflects the fully patched

and hardened configuration that will return to production

Start by confirming that the root cause identified during eradication has been remediated. If the attacker

gained access through an unpatched vulnerability, verify that the patch has been applied. If compromised

credentials contributed to the incident, confirm that those credentials have been rotated or that accounts

have been replaced across all systems where they were used. If a misconfiguration provided the initial

foothold, validate that the configuration has been corrected.

Beyond the root-cause remediation, apply any outstanding operating system, firmware, and application

updates before returning the system to production. Systems that have been offline for days or weeks during

the incident are typically behind on routine patching, and returning them with known vulnerabilities

undermines the eradication work.

Next, verify that persistence mechanisms identified during the investigation have been removed from the

system. If the system was rebuilt rather than cleaned, verify that the rebuild process used trusted sources

and did not inadvertently reintroduce compromised components.

For systems restored from backup, validate that the backup data predates the initial compromise. The

incident timeline reconstruction from the scope and eradicate activities serves as the reference point for

this validation. A backup taken after attackers established persistence may reintroduce the very threats the

organization just removed.

Finally, after patching, hardening, and security control validation are complete, scan the restored system for

indicators of compromise discovered during scoping and eradication. Performing the IOC scan last ensures

that the scan reflects the configuration that will actually return to production, rather than an interim state

that may still change.

Recover Activity | Chapter 14 | 383

Figure 123 | Pre-Restoration Verification Process

System Validation Testing

Once pre-restoration verification confirms that a system is ready for recovery, validation testing ensures

the system functions correctly and that security controls are properly configured. This testing catches

problems before they affect production operations and provides documented evidence that systems were

thoroughly validated.

Functional testing confirms applications operate correctly after restoration. Run through standard

operational tests to verify the system performs its intended business functions.  If the organization

maintains test plans or User Acceptance Testing (UAT) documentation for the system, use these resources

to guide validation. Test data access, transaction processing, and other core system capabilities.

During system validation testing, the incident response team should also confirm that security controls are

active and properly configured.  Verify Endpoint Detection and Response (EDR) agents are running and

reporting to the management console. Confirm host-based firewalls are configured according to

organizational policy. Check that logging is enabled and events are flowing to collection systems. Finally,

validate that any patches or hardening applied during eradication remain in place.

Interconnectivity testing verifies communication between the restored system and its dependencies. If the

system connects to databases, test those connections. If it communicates with other application servers,

verify that those communication paths function correctly. Test authentication flows to confirm the system

can properly validate users and service accounts. Verify any other interconnectivity features critical to

operation.

Figure 124 | System Validation Testing Process

System Owner Acceptance

System owners and business units should validate restored systems before returning them to production.

This acceptance testing serves two purposes:

• Confirm the system meets business requirements for functionality.

• Establish clear accountability for the system’s operational status.

Involve system owners early in the validation process. Provide them with the test plans or validation

checklists used during system validation testing, or have the business unit perform the acceptance testing

themselves while incident responders focus on security control validation. Business users often know their

systems intimately and can identify subtle problems that technical testing might miss.

Involving system owners in acceptance testing builds trust and shared responsibility for

the restored system’s readiness. System owners will often understand the full operational

context better than technical teams, enabling them to identify issues that technical testing

might overlook.

Document the acceptance process and obtain sign-off from the system owner. This documentation should

record what testing was performed, who performed it, and the owner’s acknowledgment that the system is

ready for production. The sign-off establishes that the system met operational requirements at the time of

restoration.

This formal acceptance process protects both the incident response team and the organization. After

responders have worked on a system, any subsequent problems may be attributed to the incident response

effort, even when those problems existed before the incident or arose from unrelated causes. Documented

acceptance testing with owner sign-off establishes a baseline and clear transfer of responsibility.

Recover Activity | Chapter 14 | 385

Figure 125 | System Owner Acceptance Process

Enhanced Monitoring Configuration

Recovery does not end when systems return to production. The period immediately following restoration

requires heightened monitoring to detect any signs of recompromise or residual attacker activity that

survived eradication.

Configuring Platform-Specific Logging and Auditing

As part of the recovery action, analysts should configure elevated logging levels on restored systems for

increased visibility. Increase verbosity for authentication events, process creation, network connections, file

system changes, system changes, administrative actions, and other pertinent events. This additional logging

provides greater visibility during the critical post-recovery period for continued monitoring and insight into

system use.

On Windows systems, enable advanced audit policies to capture detailed security events for enhanced

monitoring. Use Group Policy, Microsoft Intune, or the auditpol command to configure comprehensive

auditing for the post-recovery monitoring period, capturing important events such as logon activity,

process creation, account management, and privilege use, as shown in Listing 115. Many organizations have

shifted policy enforcement from Active Directory Group Policy to Intune, so the delivery mechanism differs

even when the underlying audit configuration is equivalent.

Enabling verbose auditing can substantially increase log volume. Windows Event ID 4688

(process creation) and Linux auditd process execution on busy hosts such as container

runtimes can generate lots of event logs. Before enabling enhanced auditing in production,

confirm that log-forwarding infrastructure (Windows Event Forwarding collectors, universal

forwarders, or equivalent agents) is sized for the increase in logging data. Validate that

events arrive at the intended destination rather than being dropped at the host or a

forwarding tier.

Listing 115 | Configuring Enhanced Windows Auditing for Post-Recovery Monitoring

PS C:\> auditpol /set /subcategory:"Logon" /success:enable /failure:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Special Logon" /success:enable /failure:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Process Creation" /success:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Account Lockout" /success:enable /failure:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Security Group Management" /success:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"User Account Management" /success:enable

The command was successfully executed.

Use auditpol /get /category:*  to review current audit policy settings and confirm that

changes have been applied successfully.

For Linux systems, configure auditd rules to monitor critical system activities during the recovery period.

The example rules in Listing 116  provide a starting point for monitoring authentication-related files, SSH

configuration, process execution, and network configuration changes. Note that these rules should be

tailored to the specific environment and adjusted based on the incident context. Depending on the system’s

configuration and use, some logs (such as process execution) may generate high volumes of data.

Listing 116 | Configuring Linux auditd Rules for Post-Recovery Monitoring

$ cat /etc/audit/rules.d/recovery-monitoring.rules

## Monitor authentication-related files

-w /etc/passwd -p wa -k identity

-w /etc/shadow -p wa -k identity

-w /etc/group -p wa -k identity

-w /etc/sudoers -p wa -k sudoers

## Monitor SSH configuration and authorized keys

-w /etc/ssh/sshd_config -p wa -k sshd_config

-w /root/.ssh/authorized_keys -p wa -k ssh_keys

## Monitor process execution

-a always,exit -F arch=b64 -S execve -k exec

## Monitor network configuration changes

-w /etc/hosts -p wa -k hosts

-w /etc/resolv.conf -p wa -k dns

$ sudo augenrules --load

$ sudo systemctl restart auditd

For ARM64 systems, adjust the arch field in the process execution rule to arch=arm64.

Recover Activity | Chapter 14 | 387

Table 33 summarizes important log sources to enable during the post-recovery monitoring period across

different platforms.

Table 33 | Enhanced Monitoring Log Sources by Platform

PLATFORM LOG SOURCE IMPORTANT EVENTS TO MONITOR

Windows Security Event Log Logon and privilege use (4624, 4625, 4672, 4648); account and

group changes (4720, 4722, 4738, 4728, 4732); service and

scheduled task creation (4697, 4698); audit policy changes (4719);

audit log cleared (1102); Kerberos service ticket requests (4769);

sensitive object access (4662)

Windows PowerShell Logging Script block logging (4104) for executed script bodies and

encoded commands; module logging (4103) for cmdlet

invocations and parameters; PowerShell transcription for full

interactive session capture; AMSI detections for obfuscated or

flagged content

Windows Sysmon Process creation with command line and parent process (Event

ID 1); network connections (Event ID 3); DNS queries (Event ID

22); image loads (Event ID 7); process injection and remote

thread creation (Event ID 8); raw disk access (Event ID 9); WMI

activity (Event IDs 19-21); named pipe creation and connection

(Event IDs 17-18); file creation and registry changes

Linux auditd Authentication, sudo usage, file access, process execution

Linux auth.log / secure SSH connections, su/sudo activity, PAM authentication

Cloud

(AWS)

CloudTrail API calls, IAM changes, resource modifications, console logins

Cloud

(Azure)

Activity Log / Sign-in

Logs

Resource operations, authentication events, role assignments

Cloud

(GCP)

Cloud Audit Logs Admin activity, data access, system events

Establishing Custom Detection and Monitoring Duration

Where possible, create custom detection rules targeting the specific indicators of compromise identified

during the incident.  If the investigation identified specific command-and-control domains, file hashes, or

behavioral activity, configure alerts for these indicators. Attackers may return to previously compromised

environments, and custom rules for known IOCs can provide high-value/low-noise early warning alerts.

Establish a monitoring duration appropriate to the incident severity and organizational risk tolerance. A

common practice is to maintain enhanced monitoring for thirty days, but this will be organization-specific.

This duration allows observation through typical operational patterns, including scheduled tasks, batch jobs,

and periodic business processes that might not execute during shorter observation windows.

Work with decision makers to identify the appropriate monitoring duration, balancing the

need for vigilance against resource constraints and added cost to the organization.

Define what constitutes abnormal behavior during this monitoring period and establish response

procedures. Any irregularity on a recently recovered system should trigger a rapid investigation. The

incident response team should remain engaged during this period, ready to respond quickly if monitoring

reveals problems.

Figure 126 | Enhanced Monitoring Configuration Process

Coordinated Production Restoration

Bringing systems back into production requires coordination across technical teams, business units, and

organizational leadership. This coordination ensures that systems return in the proper sequence, at

appropriate times, and with all stakeholders prepared for the transition.

RECOVERY RACI: WHO ACTUALLY DOES THIS WORK?

In mid-to-large organizations, IT operations, system owners, and infrastructure teams own the

mechanics of recovery execution. They plan restoration sequences, schedule change windows,

rebuild systems, and bring services back online. In RACI terms, they are Responsible and Accountable

for the restoration work itself.

The incident response team’s role during recovery is Informed and Consulted. Your contributions

focus on incident-specific concerns: whether the restore point predates attacker access, whether

credential and configuration changes from eradication are consistently deployed, whether rebuilt

systems meet the hardening established during the incident, whether containment measures can

safely be lifted, and whether enhanced monitoring is ready to catch recompromise.

If you lead IR at a smaller organization or work as a consultant in an environment without mature IT

operations, the lines between IR and IT execution blur, and you may personally run the commands

this chapter describes. The rest of this chapter speaks to the IR perspective on recovery, covering

what to validate, what to advise on, and what to document, regardless of where the execution handoff

lands in your organization.

IT operations, in coordination with system owners, identifies system dependencies and establishes a

restoration sequence. Foundational services such as Active Directory, DNS, and core network infrastructure

Recover Activity | Chapter 14 | 389

typically need to be brought up first because other systems depend on them. Application servers often have

external dependencies (such as database servers and load balancing systems) that must be restored before

they can function. The dependency chain and restoration procedure are (ideally) documented so recovery

execution, IR validation, and post-incident review share a common reference.

AWS OUTAGE CASE STUDY: THE CRITICAL ROLE OF DNS IN RECOVERY

DNS is an underlying protocol that enables much of modern networking. When DNS fails, the

cascading effects extend far beyond what most organizations anticipate.

On December 7, 2021, AWS experienced a significant outage in the us-east-1 region. A network device

overload, triggered by routine scaling activity, caused a control-plane failure that disrupted core

services. The impact rippled across many major service providers: Disney+, Netflix, Slack, Robinhood,

Coinbase, Ticketmaster, and even the US government, including the Internal Revenue Service (IRS).

Over 11,000 websites went down, and economic losses were estimated in the billions of dollars. [1]

What made this outage so impactful was the failure of DNS resolution for DynamoDB API services.

When DNS name lookups failed, applications could not connect to their databases, leading to

widespread service disruption and major business impact in a peak shopping season.

During recovery, DNS and name resolution services should be among the first systems restored and

validated. Before bringing application servers back online, verify that DNS is functioning correctly and

that records resolve as expected. Test resolution from multiple locations and for both internal and

external records.

Remember the DNS haiku: when troubleshooting problems, even ones that seem unrelated to DNS,

always check DNS.

IT operations coordinates restoration timing with business stakeholders. The incident response team

consults on timing when IR-specific concerns apply, such as when immediate restoration would disrupt

ongoing monitoring, evidence collection, or active investigation work. Off-hours restoration can have

significant advantages: reduced user impact, easier monitoring, and fewer variables complicating

troubleshooting if problems arise. However, business pressure may push for immediate restoration once

systems are ready. Provide technical recommendations to decision makers, but recognize that timing

decisions ultimately belong to organizational leadership, who understand the business context.

Capture the guidance provided by decision makers regarding restoration timing in the incident

documentation. If leadership chooses immediate restoration despite recommendations for an off-hours

window, record this decision along with the rationale. This documentation provides context for any issues

that arise and informs future incident response planning.

Organizations can often minimize the risk of broad system restoration processes by using phased

restoration. Rather than returning all systems simultaneously, bring them back in groups with validation

between phases. This approach isolates problems to specific restoration phases and provides checkpoints

for course correction if issues emerge.

Phased recovery is generally recommended to manage risk, but may not be the ideal

approach for all incidents or all organizations. See Section 14.2  for additional insight on

recovery strategies and situations when phased recovery may not be the best approach.

Figure 127 | Coordinated Production Restoration Process

Containment Action Removal

During containment, responders implement temporary measures to stop attacker activity: firewall rules,

network segmentation, disabled accounts, blocked services, DNS sinkholes, and more. Recovery includes

the controlled removal of the measures that are no longer needed once systems return to normal operation.

Some measures, however, stay in place well beyond the recovery activity. A DNS sinkhole for a known

command-and-control domain, for example, typically remains in production for months or years as a

durable detection-and-blocking control, even after the systems affected by the incident have fully

recovered.

Review all containment measures currently in place before beginning removal. Ensure that the incident

documentation captures an inventory of all containment measures, including what each measure does,

when it was implemented, who implemented it, and the rationale for its implementation. This inventory

guides prioritization for removal and helps identify measures that should remain in place after the incident.

Recover Activity | Chapter 14 | 391

Evaluate which temporary measures should become permanent improvements. Firewall rules implemented

during containment may represent security improvements worth keeping. Network segmentation that

limits attacker movement may provide long-term benefits. Work with security architecture teams to assess

which containment measures warrant permanent implementation within the organization’s security

posture.

As each system completes validation and returns to production, remove the specific containment measures

affecting that system. Monitor for any adverse effects after each step of the containment removal process.

This incremental approach provides opportunities to detect problems before they cascade across the

environment.

Figure 128 | Containment Action Removal Process

Metrics Capture

The recover activity generates valuable data that informs both the post-incident lessons learned process

and future recovery planning. Capturing this data systematically ensures the organization benefits from the

experience gained during this process.

Record the recovery timeline for each affected system. Document when restoration began, when validation

was completed, when owner acceptance occurred, and when the system returned to production. These

timestamps reveal the actual duration of recovery efforts and highlight any bottlenecks in the process for

subsequent review and analysis.

Also, document issues encountered during restoration and how they were resolved. If a backup restoration

failed and required a different approach, record what happened and how the team adapted. If validation

testing revealed problems requiring additional remediation, capture those details. These records become

institutional knowledge that can be used to improve future recovery efforts.

Where possible, track human resource time investment throughout recovery. Note personnel hours spent

on recovery activities, including any third-party support services engaged. This data is valuable for incident

cost analysis and helps organizations plan appropriate resources for future incidents.

Finally, preserve all recovery documentation. The decisions made, challenges overcome, and adaptations

required during recovery provide rich material for improving incident response capabilities. Comprehensive

documentation, captured when the information is fresh to the analyst, contributes to experience that can

be applied to organizational improvement for recovery processes.

Figure 129 | Metrics Capture Process

RECOVERY STRATEGIES

Organizations can approach recovery through different strategies depending on incident characteristics,

business requirements, and operational constraints. The choice of strategy affects recovery speed, risk

level, and resource requirements, and should be made thoughtfully through coordination with

organizational decision makers.

In this section, we’ll examine two principal recovery strategies: phased recovery for incremental restoration

and coordinated recovery for parallel restoration within a planned window. We’ll also cover scheduling

considerations that shape timing decisions and the unique factors that apply to cloud recovery.

Phased Recovery

Phased recovery restores systems incrementally, validating each system or small groups of systems before

proceeding to the next. This approach is more conservative, providing maximum control over the

restoration process and allowing analysts to isolate problems when they occur.

When problems arise during phased recovery, analysts can isolate any issues to the systems in the current

restoration phase (or the previous restoration phases when system validation is not comprehensive).

Responders can troubleshoot and resolve issues without the complexity of multiple simultaneous

restoration failures. If a restored system exhibits signs of residual compromise, the limited scope allows

rapid re-containment without affecting other recovered systems.

Limiting the scope of restoration in a phased recovery reduces complexity and makes

troubleshooting easier when problems arise. This is an important advantage for many

organizations.

Phased recovery also provides natural validation checkpoints. Each phase completion offers an opportunity

to assess progress, adjust plans, and confirm the approach is working before committing to additional

restoration steps. Teams can incorporate lessons from early phases into later restoration efforts.

The trade-off in phased recovery is the extended timeline for returning all systems to production. Phased

Recover Activity | Chapter 14 | 393

recovery extends the overall restoration timeline because systems will wait for prior phases to complete

before proceeding. For organizations with many affected systems, the sequential nature of phased recovery

may prolong business impact beyond acceptable thresholds.

Phased recovery works best when the organization faces uncertainty about eradication completeness, when

systems have limited dependencies, or when the incident response team has limited capacity for parallel

restoration efforts.

Coordinated Recovery

Coordinated recovery restores multiple systems simultaneously within a planned maintenance window.

This approach accelerates overall restoration but requires extensive preparation and parallel execution

capability.

Speed is the primary advantage in coordinated recovery.  Restoring systems in parallel reduces the total

calendar time from incident to normal operations, significantly reducing the Mean Time to Resolution

(MTTR) metric. For incidents affecting interconnected systems that depend on each other, coordinated

recovery may be the only practical approach, as individual systems cannot function until their dependencies

are restored.

Coordinated recovery demands significant preparation from all involved teams. Teams should pre-validate

all restoration procedures, stage required resources, assign personnel to parallel working groups focused on

a system or a group of systems, and establish communication protocols for the restoration window.

The risk profile for coordinated recovery differs from that for phased recovery, as problems during

coordinated recovery can cascade across multiple systems simultaneously. If the restoration plan is flawed

or encounters unexpected issues, those issues will affect multiple dependent systems rather than becoming

apparent during early phases. Further, troubleshooting becomes more complex when multiple systems

exhibit issues simultaneously.

Coordinated recovery works best when systems have well-documented dependencies, when phased

restoration would unacceptably extend business impact, or when the organization has high confidence in

the completeness of eradication and restoration procedures.

COORDINATED RECOVERY AT MAERSK: AN INCIDENT OF GLOBAL SCALE

On June 27, 2017, the NotPetya malware struck Maersk, the global shipping and logistics company

responsible for approximately 20% of world trade. Within hours, the attack destroyed 49,000 laptops,

wiped 3,500 of 6,200 servers, and rendered 1,200 applications inaccessible. [2]

Port facilities across the globe shut down. The loading systems used to prevent container ships from

capsizing became unavailable. Even phone contacts synchronized with Outlook were wiped from

mobile devices, hampering coordination efforts.

Maersk’s operations relied on tightly coupled systems that could not operate independently, making a

phased restoration impractical.

Maersk assembled an emergency recovery center in the United Kingdom and established its

headquarters in Denmark as the global coordination hub. Hundreds of staff worked tirelessly in

parallel, each focused on specific system groups. As part of the response effort, Maersk confiscated

all computer equipment, procured new hardware, and distributed it to recovery teams.

The incident investigation revealed that Maersk’s 150 domain controllers had all been wiped

simultaneously, and without them, nothing else could be restored. Recovery teams eventually located

one intact domain controller backup in Ghana, a server that had been offline during the attack due to

a power outage. This single backup became the foundation for rebuilding the entire global network.

Within ten days, teams had restored 4,000 servers, 45,000 PCs, and 2,500 applications. Full recovery

of all 49,000 laptops took four weeks. The incident cost Maersk between $250 and $300 million.

Several factors contributed to the successful coordinated recovery. Centralized coordination through

the UK recovery center and Danish headquarters provided a clear command structure. Parallel teams

worked on assigned responsibilities to prevent duplication of effort.

The Maersk recovery demonstrates that coordinated recovery requires more than technical

capability. Organizations facing similar scenarios need established communication channels that do

not depend on the systems being recovered, manual processes documented and ready for activation,

and clear coordination structures that can operate under crisis conditions.

Scheduling Considerations

The timing of recovery activities affects both operational success and business impact. Responders should

provide informed recommendations while recognizing that scheduling decisions are the responsibility of

organizational decision makers.

Off-hours restoration offers several advantages. Fewer users are active, reducing the impact of any

problems that arise. Network traffic is often lower, making it easier to monitor for anomalies. Staff

performing off-hours restoration often face fewer competing demands during the process. Further, if

problems encountered during restoration do require rollback, the lower stakes of off-hours operations

provide more flexibility.

Off-hours restoration is not always feasible for organizations. Many businesses operate

24/7, and off-hours will still involve significant user activity.

Business pressure often favors immediate restoration to minimize downtime and get systems back online

quickly. Stakeholders waiting for systems to return may not appreciate the risk reduction benefits of

delayed restoration. Decision makers may determine that accepting some restoration risk is preferable to

extended downtime.

When providing scheduling recommendations, clearly frame the trade-offs. Explain what risks off-hours

restoration mitigates and what consequences might arise from immediate restoration. If decision makers

choose immediate restoration, response teams should support that decision while documenting the

guidance provided.

Consider system criticality when developing scheduling recommendations for decision makers. High-

criticality systems with significant business impact may warrant more aggressive restoration timelines with

accepted risk levels. Lower-criticality systems may benefit from conservative scheduling that prioritizes

thorough validation over speed.

Recover Activity | Chapter 14 | 395

Cloud Recovery Considerations

Cloud environments present unique recovery considerations related to their architecture, access models,

and available restoration mechanisms. Even organizations with primarily on-premises infrastructure likely

have cloud dependencies through SaaS applications, identity providers, or hybrid connectivity that require

special considerations during recovery.

Cloud snapshots provide powerful restoration capabilities when properly managed. Restoration from a

known-good snapshot can rapidly return instances to a pre-compromise state. However, snapshot selection

requires careful timeline analysis to ensure the chosen snapshot predates the initial compromise. Restoring

from a post-compromise snapshot reintroduces the attacker’s access. The examples in Table 34 illustrate

common commands for restoring instances from snapshots across major cloud providers.

Table 34 | Restoring Cloud Instances from Snapshots

CLOUD

PROVIDER

SNAPSHOT RESTORATION COMMAND

AWS aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-

east-1a

Azure az snapshot create --resource-group RG --source /subscriptions/.../disks/disk1 --name

clean-snapshot

Google gcloud compute disks create restored-disk --source-snapshot=clean-snapshot --zone=us

-central1-a

Before restoring from a snapshot, verify the snapshot creation date against the incident timeline established

during scoping. List available snapshots with creation timestamps to identify candidates that predate the

initial compromise. An example AWS CLI command for listing snapshots with creation timestamps is shown

in Listing 117.

Listing 117 | Listing AWS Snapshots with Creation Timestamps

$ aws ec2 describe-snapshots --owner-ids self --query

'Snapshots[*].[SnapshotId,StartTime,Description]' --output table

------------------------------------------------------------------------------------

|                                 DescribeSnapshots                                |

+-----------------------+--------------------------+-------------------------------+

| snap-0a1b2c3d4e5f6g7h | 2025-11-15T03:00:00.000Z | Weekly backup - web-server-01 |

| snap-1b2c3d4e5f6g7h8i | 2025-11-22T03:00:00.000Z | Weekly backup - web-server-01 |

| snap-2c3d4e5f6g7h8i9j | 2025-11-29T03:00:00.000Z | Weekly backup - web-server-01 |

+-----------------------+--------------------------+-------------------------------+

Identity and Access Management (IAM) warrants particular attention during cloud recovery. Review and

audit all access mechanisms: passwords, API keys, access tokens, service account credentials, role

assignments, policies, groups, and permissions. Validate that multi-factor authentication is enabled for all

users with access to cloud resources. Verify that policies and privileges follow the principle of least

privilege, granting only the necessary privileges to perform required tasks.

Temporarily increase logging verbosity on recovered cloud instances. Cloud platforms offer extensive

logging capabilities that may not be fully enabled during normal operations. Activating additional logging for

API access, network connections, and resource changes provides enhanced visibility during the post-

recovery monitoring period. The additional cost of verbose logging is often justified during the critical

weeks following incident recovery.

Infrastructure-as-code environments require verification that templates and deployment configurations

have not been compromised. If attackers modified infrastructure definitions, newly deployed resources may

contain backdoors or misconfigurations. Review version control history for infrastructure code and validate

template integrity before deploying new resources.

RECOVERY CHALLENGES

Recovery presents distinct challenges that can complicate even well-planned restoration efforts.

Understanding these challenges helps incident response teams anticipate issues and develop mitigation

strategies as they transition back to normal operations.

In this section, we’ll address challenges that complicate recovery: data loss when restoring from clean

backups, business pressure for rapid restoration, and the ever-present uncertainty in eradication

verification. We’ll also examine coordination complexity from parallel teams and dependencies, user

communication during restoration, and the tendency to attribute unrelated post-recovery problems to the

incident response effort.

Data Loss from Clean-Backup Recovery

Choosing a backup that predates the compromise means losing data created or modified between the

backup and the incident. The gap can range from hours to days depending on the compromise timeline and

backup cadence, and it requires strategies to minimize business impact.

Restore user-created files selectively from newer backups after thorough investigation, ensuring they do

not reintroduce a threat to the environment. Recover data from application databases if separate database

backups are available that can be validated as clean.

In many compromise incidents, organizations will need to accept some data loss as the

cost of ensuring systems are free of attacker artifacts. Coordinate with data owners to

manually recreate critical changes from the lost period when automated recovery is not

possible.

Business Pressure for Rapid Restoration

System owners and organizational leadership want affected systems back in production quickly. Every hour

of downtime results in business impact, user frustration, and measurable financial losses. This pressure is at

odds with the careful validation and staged rollout that reduce the chance of recompromise.

The pressure on analysts to quickly restore systems to production increases as the incident duration

continues. Initial patience with deliberate restoration often erodes as days pass and the business impact

accumulates, particularly for stakeholders who do not fully understand the organization’s incident response

policies and priorities. These pressures can push responders toward shortcuts that bypass validation or

monitoring steps.

Thorough eradication can reduce this pressure over time. When the IRT has confidence that the attacker

Recover Activity | Chapter 14 | 397

has been fully evicted and persistence mechanisms have been removed, the organization can take a

deliberate pace through recovery rather than rushing systems back into production. Some organizations,

particularly those with significant technical debt exposed by the incident, run recovery over weeks or

months while addressing underlying hardening, replacement, or upgrade work that the incident has

brought forward.

Recovery teams can best manage this challenge by translating technical work into business language and

involving decision makers to manage expectations among other stakeholders. Analysts should describe

recovery activities in terms of reducing the likelihood of another outage, protecting restored data, and

preventing a return of attacker access. Thorough recovery becomes a way to protect the investment already

made in containment and eradication.

Communication with stakeholders helps manage expectations. Regular updates about recovery progress,

challenges encountered, and next steps keep stakeholders informed and engaged.

Documentation remains important throughout the recovery activity. Recovery teams should record

decisions on restoration timing and scope, who made them, and what information they considered at the

time. If business pressure leads to expedited recovery and later recompromise, this record provides context

for debrief and after-action reviews.

Eradication Verification Uncertainty

Rarely will an organization know with certainty that eradication was completely successful. This uncertainty

underlies much of recovery’s complexity and affects decisions about when and how to bring systems back

online. Sophisticated attackers may have established persistence mechanisms that investigation did not

discover, and those mechanisms can enable rapid recompromise after restoration.

An unpleasant part of incident response is making decisions without complete information.

Responders rely on process and experience to manage uncertainty, accepting that some

risk will always remain.

The uncertainty is irreducible but manageable. Even thorough investigations leave some residual risk that

attacker artifacts persist. Recovery becomes a risk management exercise in which organizations decide

when the residual risk is acceptable for specific systems, users, and business processes.

Recovery planning should treat eradication verification as an activity rather than a single decision. Analysts

define concrete checks for each system before and after restoration: registry and configuration validation,

scheduled task review, startup item inspection, and integrity checks for critical binaries. Results of these

checks feed into go or no-go decisions for each recovery step.

Enhanced monitoring during and after recovery addresses this uncertainty operationally. By closely

watching restored systems for signs of attacker activity, organizations can detect recompromise and

respond before significant additional damage occurs. The monitoring period serves as a practical validation

that eradication was sufficiently complete for the organization’s risk tolerance.

Phased recovery also mitigates eradication uncertainty. Teams restore a small set of systems first, enable

monitoring, and watch for anomalies before scaling up to broader restoration. If recompromise occurs, the

impact is limited, and responders can refine eradication and validation techniques before proceeding.

Coordination Complexity

Recovery involves multiple groups working in parallel: incident responders validating systems, IT operations

performing restorations, network teams adjusting connectivity, business units conducting acceptance

testing, and leadership making timing decisions. Coordinating these efforts challenges even mature

organizations, especially when recovery spans time zones, vendors, and external service providers.

Communication gaps can contribute to problems during recovery. A system restored by IT operations but

not yet validated by security might re-enter production prematurely. Network teams might remove

containment measures before restored systems are ready for full connectivity. Business users might begin

using systems before acceptance testing completes, then experience issues that were already known but

not yet communicated.

Having an incident response coordinator can be valuable during recovery, especially for incidents that scale

across multiple systems and teams. This role focuses on tracking recovery progress, facilitating

communication between teams, and ensuring recovery steps are executed in the proper sequence. The

coordinator helps prevent missteps that arise from parallel activities and keeps recovery moving forward.

For larger incidents, bringing a technical project manager into the recovery effort can substantially reduce

coordination complexity. Project tracking and multi-team coordination are core project management skills

and are not common on incident response teams. A Gantt chart of the recovery effort can help to identify

resource constraints using business language that leadership readily understands. This can make it easier to

decide when to bring in contractors, extend change windows, or reprioritize other work to unblock

recovery.

Having a clear handoff procedure also helps to reduce friction during complex recovery efforts. Recovery

plans define what conditions a system should meet before progressing from restoration to validation, from

validation to acceptance testing, and from acceptance testing to production release. These criteria might

include specific log sources enabled, health checks passing for a defined period, or successful completion of

predefined user acceptance tests. When handoffs are explicit, teams spend less time discussing readiness

and more time executing recovery procedures.

User Communication and Expectations

End users affected by the incident want to know when systems will be available and what actions they

should take when services return. Managing these communications requires balancing transparency with

the uncertainty inherent in recovery timelines.

Overpromising creates recurring problems during recovery. If recovery encounters unexpected delays after

users have been told systems will return by a specific time, credibility suffers. Repeated missed deadlines

erode trust in incident communications and make future guidance less effective.

Technical incident response teams should defer user communications to designated communication leads

or organizational spokespeople. This can be an internally focused effort, or it may involve public relations

teams for incidents with external visibility. The technical team provides accurate status information and

should be prepared to answer questions from the communication leads, but the communication leads

manage the messaging in line with organizational policies and priorities.

Preparing template messages for common scenarios (delays, partial restoration, user

action required) before recovery begins allows communication leads to send timely

Recover Activity | Chapter 14 | 399

updates when situations arise that require prompt announcements.

For large incidents, organizations should establish a communication cadence with stakeholders and affected

users early and stick to it. Provide updates at regular intervals, even when there is no new information to

share. Use multiple communication channels to reach users through their preferred media (keeping in mind

that systems such as chat or email may not be available during the incident).

Post-Recovery Problem Attribution

Systems sometimes exhibit problems after recovery that are unrelated to the incident or the recovery

effort. Hardware failures, latent software bugs, configuration drift, and normal operational issues can all

emerge coincidentally after restoration. When they do, the incident response effort is frequently blamed.

This attribution problem is difficult to avoid entirely. System owners and users naturally associate any post-

recovery problem with the recent incident response work. The incident response team touched the system,

so problems are perceived as connected to those changes even when they are demonstrably unrelated.

Recovery planning can reduce the impact of misplaced attribution. Thorough acceptance testing with

documented owner sign-off provides a clear reference point. When the system owner verifies that the

system functions correctly and agrees that it is ready for production, subsequent problems are harder to

attribute solely to the recovery effort. The documented baseline establishes that the system met the agreed

requirements at a specific point in time.

Relationships matter as much as documentation. When system owners feel involved and informed rather

than having recovery imposed on them, they become partners in restoration rather than critics looking for

faults. Regular check-ins, open discussion of risks and trade-offs, and responsiveness to concerns build

trust that can help reduce the impact of unforeseen complications.

RECOVERY ACTIVITY EXAMPLE

The following example illustrates a case where recovery is an important part of the incident response

process.

Phased Recovery of a Domain Controller Environment

Sarah Park, senior incident responder at Lakewood Health Systems, faced a complex recovery scenario. A

ransomware attack encrypted domain controllers across the organization’s three sites, and the eradicate

activity had just concluded. Clinical systems remained offline, waiting for Active Directory restoration

before they could authenticate users and resume operations.

Sarah’s first task was to correlate the incident timeline with available backups to identify a safe restore

point. The investigation revealed that attackers gained initial access through a vulnerable VPN appliance

eighteen days before the encryption event. Before querying the backup catalog, Sarah reviewed what

remained of the backup infrastructure. During the encryption event, the attackers had targeted the primary

backup repository, encrypting the daily incremental files and the disk-based weekly restore points

alongside the domain controllers. The organization’s longer-retention daily and monthly tiers, held on the

same repository, were lost with them. Only the weekly snapshots that had been synchronized to the offline

archive prior to the attack remained usable for restoration. She queried the backup catalog to review the

recoverable domain controller backups, as shown in Listing 118.

Listing 118 | Reviewing Available Domain Controller Backups

PS C:\> Get-WBBackupTarget | Get-WBBackupSet | Where-Object {$_.VersionId -like "*DC01*"} |

>>     Select-Object VersionId, BackupTime | Sort-Object BackupTime -Descending

VersionId                            BackupTime

---------                            ----------

DC01-2025-12-04                      12/4/2025 2:00:00 AM  1

DC01-2025-11-27                      11/27/2025 2:00:00 AM 2

DC01-2025-11-20                      11/20/2025 2:00:00 AM 3

DC01-2025-11-13                      11/13/2025 2:00:00 AM

1 Most recent backup (7 days old): post-compromise, unsafe.

2 Two weeks old: attacker already had AD access by this date.

3 Three weeks old: predates initial access, safe for restoration.

The most recent backup was tempting, but Sarah’s timeline showed the attacker had accessed Active

Directory within five days of initial compromise. Only the November 20th backup predated all attacker

activity in the environment.

With a safe backup identified, Sarah worked through pre-restoration verification. She performed a test

restore of the November 20th backup NTDS.dit database to an isolated virtual machine to verify backup

integrity before proceeding. She confirmed the VPN vulnerability that provided initial access had been

patched during eradication. The compromised service account credentials had been rotated. An IOC scan of

the restored test environment returned clean results. Sarah documented these verification steps in the

incident record before proceeding to production restoration.

Recovery proceeded in phases, starting with the primary domain controller at headquarters.  Sarah restored

the PDC emulator role holder first, as other domain controllers and AD-dependent systems required it for

authentication and replication. After the restore completed, she verified core AD services were operational

using Get-Service and dcdiag, as shown in Listing 119.

Listing 119 | Verifying Domain Controller Services Post-Restoration

PS C:\> Get-Service NTDS, DNS, Netlogon, DFSR | Select-Object Name, Status

Name     Status

----     ------

NTDS     Running 1

DNS      Running

Netlogon Running

DFSR     Running 2

PS C:\> dcdiag /test:sysvolcheck /test:advertising

[...]

......................... DC01 passed test sysvolcheck

......................... DC01 passed test Advertising 3

1 Active Directory Domain Services is running.

2 DFS Replication is running for SYSVOL.

Recover Activity | Chapter 14 | 401

3 The domain controller is advertising correctly to the network.

Before proceeding to the next phase, Sarah configured enhanced monitoring on the restored domain

controller. She enabled detailed auditing for authentication events, Kerberos ticket operations, and account

management activities using auditpol, as shown in Listing 120.

Listing 120 | Configuring Enhanced Auditing on Restored Domain Controller

PS C:\> auditpol /set /subcategory:"Kerberos Authentication Service" /success:enable

/failure:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Kerberos Service Ticket Operations" /success:enable

/failure:enable

The command was successfully executed.

PS C:\> auditpol /set /subcategory:"Credential Validation" /success:enable /failure:enable

The command was successfully executed.

Phase 2 restored secondary domain controllers at the two satellite clinic sites. Sarah restored each DC

sequentially, verifying replication health with repadmin after each restoration before proceeding to the next,

as shown in Listing 121.

Listing 121 | Verifying AD Replication Health

PS C:\> repadmin /replsummary

Replication Summary Start Time: 2025-12-11 14:23:15

Beginning data collection for replication summary, this may take a while:

[...]

Source DSA          largest delta    fails/total %%   error

DC01                       12m:05s    0 /   5    0

DC02                       08m:32s    0 /   5    0    1

DC03                       15m:47s    0 /   5    0

Destination DSA     largest delta    fails/total %%   error

DC01                       12m:05s    0 /   5    0

DC02                       08m:32s    0 /   5    0

DC03                       15m:47s    0 /   5    0

1 All domain controllers are replicating successfully with no failures.

During Phase 2, Sarah encountered an expected complication. The twenty-one-day-old backup contained

stale computer objects for workstations deployed after the backup date. After communicating with the

incident lead and decision makers, she documented these objects for the IT team to recreate after

workstation recovery, rather than delaying DC restoration to resolve them.

Phase 3 addressed member servers and workstations. Critical AD-dependent systems, including the RADIUS

server for wireless authentication, the certificate authority, and clinical application servers, were restored

first. Sarah coordinated with system owners for acceptance testing on each server before marking it ready

for production.

For workstations, the team made a pragmatic decision: rebuild from gold images rather than restore from

backup. This approach was faster and ensured a clean baseline state. User data was backed up separately to

network shares unaffected by the ransomware. The IT team deployed workstations in phases by

department, prioritizing clinical areas.

Radiology department systems presented an obstacle. A service account password was rotated two weeks

before the incident as part of routine maintenance, after the backup date but before the attacker gained

access. The restored AD contained the old password, breaking authentication to the radiology application.

The enhanced logging on the domain controllers quickly captured the failed authentication attempts from

the application servers, allowing Sarah to identify the issue. Sarah coordinated with the vendor to reset the

service account and update the application configuration, adding a day to the Phase 3 timeline.

After eight days, Lakewood Health Systems completed the full restoration of all systems.

Figure 130 | Lakewood Health Systems Recovery Timeline

Sarah captured important lessons learned for the post-incident review:

• Attackers destroyed the online backup repository during the encryption event, leaving only the four

weekly snapshots that had been synchronized to the offline archive beforehand. Adopting an immutable

or air-gapped backup tier aligned with the 3-2-1-1-0 rule, with ninety days or more of protected weekly

snapshots, would provide a greater margin for recovery.

• The service account inventory was incomplete, causing delays when the radiology system credentials

required coordination. A complete inventory with password rotation dates would accelerate future

recovery efforts.

• Pre-staged gold images significantly accelerated workstation recovery compared to individual system

restores. Maintaining current images should become standard practice.

• AD-dependent systems created a bottleneck that kept clinical systems offline. Future business

continuity planning should address authentication dependencies.

Recover Activity | Chapter 14 | 403

Sarah noted that each of these gaps, once addressed, would shorten recovery timelines and reduce

coordination overhead in future incidents. By documenting them during the recover activity while details

were fresh, she ensured they would carry forward into the formal debrief.

RECOVER: STEP-BY-STEP

The following steps provide a condensed reference for recovery activities. Each step corresponds to topics

covered earlier in this chapter, organized for use when validating, testing, and coordinating the return of

systems to production.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Conduct Pre-Restoration Verification

This step revalidates the eradicate Step 8 exit criteria for each system about to return to production rather

than repeating the eradication work from scratch. Use the evidence and documentation produced during

eradication as the starting point, and focus Step 1 on confirming those findings still hold and on the

verification activities that are specific to recovery, such as backup integrity and rebuild integrity, which are

not part of eradication.

1. Revalidate root cause remediation before restoration, including:

◦ Confirm that the exploited vulnerability remains patched on the system.

◦ Verify compromised credentials are still rotated across all systems where they were used.

◦ Validate the misconfigurations enabling initial access remain corrected.

◦ Review eradication documentation to confirm all identified issues were addressed and no

regressions have been introduced since eradicate Step 8.

2. Revalidate persistence mechanism removal, including:

◦ Treat eradication verification as an ongoing activity rather than a single decision.

◦ Confirm the eradicate Step 8 persistence checks still hold on the system about to be restored.

◦ Spot-check scheduled tasks, services, registry entries, and unauthorized accounts for any

reappearance since the eradicate sign-off.

◦ Perform registry and configuration validation, scheduled task review, startup item inspection, and

integrity checks for critical binaries, feeding the results into go/no-go decisions for each recovery

step.

3. Validate backup integrity for backup-based restorations, including:

◦ Confirm backup date predates the initial compromise based on the incident timeline.

◦ Verify backup integrity through checksum validation or test restoration.

◦ Document backup selection rationale for incident records.

◦ If no clean backup exists, document the rebuild approach and validation steps.

4. Verify rebuild integrity for rebuilt systems, including:

◦ Confirm rebuild used trusted installation media or gold images.

◦ Verify installation sources have not been compromised.

◦ Document the rebuild process and any deviations from standard procedures.

Step 2. Perform System Validation Testing

1. Conduct functional testing, including:

◦ Run standard operational tests to verify core business functions.

◦ Test data access, transaction processing, and application workflows.

◦ Use existing test plans or UAT documentation where available.

◦ Document any functional issues discovered during testing.

2. Verify security control configuration, including:

◦ Confirm the EDR agent is installed, running, and reporting to the management console.

◦ Verify the host-based firewall is enabled and configured per organizational policy.

◦ Check that logging is enabled and events are flowing to collection systems.

◦ Validate patches and hardening applied during eradication remain in place.

3. Perform inter-connectivity testing, including:

◦ Test connections to dependent databases and verify data access.

◦ Verify communication paths to other application servers.

◦ Test authentication flows for users and service accounts.

◦ Confirm network connectivity to required internal and external resources.

Step 3. Obtain System Owner Acceptance

1. Coordinate acceptance testing with system owners, including:

◦ Provide test plans or validation checklists to system owners.

◦ Schedule acceptance testing window with business unit representatives.

◦ Support system owners during their validation activities.

◦ Document any issues identified during owner acceptance testing.

2. Document acceptance and obtain sign-off, including:

◦ Record what testing was performed and by whom.

◦ Capture the owner’s acknowledgment that the system is ready for production.

◦ Document any known limitations or issues accepted by the owner.

◦ Obtain formal sign-off before proceeding to production restoration.

Step 4. Configure Enhanced Monitoring

1. Enable elevated logging on restored systems, including:

◦ Configure advanced audit policies for authentication, process creation, and system changes.

◦ Enable PowerShell Script Block Logging on Windows systems.

◦ Configure auditd rules for critical file and process monitoring on Linux systems.

◦ Verify logs are flowing to SIEM or log collection infrastructure.

2. Enable and validate incident-specific detection rules on restored systems, including:

◦ Confirm the detection rules authored during contain and eradicate (command-and-control

domains, file hashes, behavioral patterns based on observed attacker TTPs) are active and targeted

at the restored systems.

◦ Tune alert thresholds and scope for the enhanced monitoring window if signal-to-noise needs

adjustment now that the systems are back in production.

◦ Add any rules identified during recovery scoping that were not implemented earlier, coordinating

with detection engineering rather than creating ad hoc rules.

◦ Test detection rules to confirm they generate expected alerts on the restored systems.

Recover Activity | Chapter 14 | 405
