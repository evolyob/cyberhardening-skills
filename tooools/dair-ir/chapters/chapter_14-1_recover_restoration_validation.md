﻿# 第 14-1 章：復原階段－安全還原、完整性校驗與逐步通電

> 模組化子章節 | 隸屬來源:  (行 1 ~ 967)

---

# Chapter 14: Recover Activity: Safe Restoration & Canary Validation

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

◦ Identify unauthorized installations of remote access utilities commonly utilized by attackers.

◦ Review authorized tool configurations for unauthorized access grants.

◦ Implement allowlisting to prevent the unauthorized installation of remote access tools.

4. Address cross-trust boundary persistence, including:

◦ Enumerate forest trusts, external trusts, and federated identity relationships.

◦ Review authentication logs in trusted environments for suspicious cross-boundary activity.

◦ Coordinate eradication with administrators of trusted domains and identity providers.

◦ Verify removal of cross-boundary artifacts in all affected environments.

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

14 Recover Activity

The recover activity represents the transition from eliminating threats to restoring normal operations. This

activity leverages insights from detection, scoping, containment, and eradication activities to test and

validate systems before bringing them back into production.

Recovery is not only removing containment measures and reactivating systems. Rather, it is an orchestrated

process that ensures restored systems are secure, functional, and ready to support operations before

returning them to production.

Figure 122 | Recover Activity Waypoint

The recover activity balances competing pressures: the urgency to restore operations against the need for

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
