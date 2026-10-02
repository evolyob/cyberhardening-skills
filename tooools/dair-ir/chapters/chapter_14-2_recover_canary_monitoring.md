# 第 14-2 章：復原階段－金絲雀監控、認證強化與上線簽核

> 模組化子章節 | 隸屬來源:  (行 969 ~ 1935)

---

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

calendar time from incident to normal operations, substantially reducing the Mean Time to Resolution

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

AWS aws ec2 create-volume --snapshot-id snap-0123456789abcdef0 --availability-zone us-east-1a

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

API access, network connections, and resource changes provides enhanced visibility during the post-recovery monitoring period. The additional cost of verbose logging is often justified during the critical

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

updates when situations arise that require prompt announcements.

For large incidents, organizations should establish a communication cadence with stakeholders and affected

users early and stick to it. Provide updates at regular intervals, even when there is no new information to

share. Use multiple communication channels to reach users through their preferred media (keeping in mind

that systems such as chat or email may not be available during the incident).

Post-Recovery Problem Attribution

Systems sometimes exhibit problems after recovery that are unrelated to the incident or the recovery

effort. Hardware failures, latent software bugs, configuration drift, and normal operational issues can all

emerge coincidentally after restoration. When they do, the incident response effort is frequently blamed.

This attribution problem is difficult to avoid entirely. System owners and users naturally associate any post-recovery problem with the recent incident response work. The incident response team touched the system,

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

• Pre-staged gold images greatly accelerated workstation recovery compared to individual system

restores. Maintaining current images should become standard practice.

• AD-dependent systems created a bottleneck that kept clinical systems offline. Future business

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
