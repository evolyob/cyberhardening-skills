﻿# 第 13-2 章：根除階段－惡意常駐機制清除與後門拔除

> 模組化子章節 | 隸屬來源:  (行 1733 ~ 3461)

---

Creating service winpmem

Installed service winpmem

Started service winpmem

Memory Info:

CR3: 0x1ae002

NtBuildNumber: 0x65f4

KernelBase: 0xfffff806d4000000

[...]

Padding 8320 pages from 0x45f80000

Copying 3584 pages (0xe00000) from 0x48000000

Padding 750080 pages from 0x48e00000

Copying 3860480 pages (0x3ae800000) from 0x100000000

Completed imaging in 53.568839s 2

Stopped service winpmem

Removing driver from C:\Users\jwrig\AppData\Local\Temp\1405366611.sys

1 Acquire a whole-system memory image with WinPMEM.

2 Memory capture completed in under one minute for the target with 32 GB RAM.

After capturing memory, analysts can use tools like Volatility and MemProcFS to extract and analyze

artifacts from the memory dump. Volatility provides plugins that parse memory structures to reveal

processes, network connections, loaded modules, registry hives, and other artifacts. This offline analysis

allows multiple analysts to examine the same memory image in parallel without impacting the running

system.

Volatility runs on any system with a Python 3 environment, and can analyze memory

captures for Windows, Linux, and macOS systems.

One particularly valuable resource from Volatility memory analysis is the enumeration of installed drivers

on a Windows system. Windows drivers with vulnerabilities represent an opportunity for an attacker to gain

escalated privileges, ultimately allowing attackers to disable endpoint protection systems and other system

controls. The driver enumeration scan in Listing 73  uses Volatility to display all loaded drivers from the

captured memory image, including the suspicious KfeCoSvc driver associated with Kyocera printer software

that is vulnerable to privilege escalation attacks [10]

.

Listing 73 | Volatility Windows Driver Enumeration

$ vol -qf ircase504.dmp windows.driverscan.DriverScan 1

Volatility 3 Framework 2.26.2

Offset         Start          Size      Name

0xbf84ba6cf4d0 0xf80666610000 0x2a000   \Driver\acpiex

0xbf84ba707e10 0xf80666860000 0x93000   \Driver\pci

0xbf84ba757cb0 0xf8067b3b0000 0x12000   \Driver\uiomap

0xbf84ba7eac10 0xf806d4000000 0x0       \Driver\WMIxWDM

0xbf84ba8ccdf0 0xf806d4000000 0x0       \Driver\PnpManager

0xbf84ba8cedf0 0xf806d4000000 0x0       \Driver\SoftwareDevice

0xbf84ba8cfdf0 0xf806d4000000 0x0       \Driver\DeviceApi

0xbf84ba8d4df0 0xf806d4000000 0x0       \Driver\ACPI_HAL

0xbf84ba9d0060 0xf80666640000 0xa000    lxss

0xbf84ba9d7e20 0xf80665960000 0xe0000   CNG

[...]

0xbf84ea056e20 0xf80682840000 0x1160000 \Driver\KfeCoSvc 2

0xbf84ea05ee20 0xf80681cc0000 0xd5000   \Driver\PEAUTH

[...]

0xbf84fca729d0 0xf806826e0000 0x1b000   \Driver\WdNisDr

0xbf84fe14fe20 0xf806839b0000 0x10000   \Driver\winpmem 3

0xbf84fe2f3aa0 0xf80682800000 0xf000    \Driver\WpdUpFltr

1 Enumerate running drivers from the memory image (output has been modified to fit within the available space).

2 KfeCoSvc driver associated with Kyocera software.

3 WinPmem driver used for memory capture.

Browsing Memory Artifacts with MemProcFS

While Volatility remains the most widely used memory analysis framework, MemProcFS offers a compelling

alternative that can accelerate memory investigation during eradication. MemProcFS mounts a memory

image as a virtual file system, allowing analysts to browse memory contents using familiar file navigation

tools rather than running individual plugins and waiting for output.

The file system abstraction in MemProcFS provides immediate access to processes, modules, handles,

registry hives, and network connections through a directory structure. Further, MemProcFS integrates with

other analysis tools through the file system interface, allowing analysts to use standard UNIX or PowerShell

commands to search, filter, and extract artifacts from memory.

For example, after collecting a memory image with WinPMEM, the analyst mounts it using MemProcFS as

shown in Listing 74 . Next, analysts search the mounted file system for instances of backup.exe, an IoC

identified during log investigation, using PowerShell Get-ChildItem and Select-String as shown in Listing 75.

The search revealed multiple artifacts associated with backup.exe, including registry entries, prefetch files,

and file reads from the user’s Downloads folder.

Listing 74 | Mount Memory Image with MemProcFS

PS C:\tools\MemProcFS> .\MemProcFS.exe -device F:\memory.dmp -forensic 1

Initialized 64-bit Windows 10.0.26100

==============================  MemProcFS  ==============================

- Author:           Ulf Frisk - pcileech@frizk.net

- Info:             hxxps://github[.]com/ufrisk/MemProcFS

- Discord:          [社群討論群組]

- License:          GNU Affero General Public License v3.0

- Licensed To:      GNU Affero General Public License v3.0 - OPEN SOURCE USER.

---------------------------------------------------------------------

MemProcFS is free open source software. If you find it useful please

become a sponsor at:  Thank You :)

---------------------------------------------------------------------

- Version:          5.16.8 (Windows)

- Mount Point:      M:\

- Tag:              26100_852e07b1

- Operating System: Windows 10.0.26100 (X64)

==========================================================================

Listing 75 | Search MemProcFS Filesystem for Indicator of Compromise

PS M:\> Get-ChildItem -Path .\forensic\ -Recurse -File | Select-String -SimpleMatch 'backup.exe'

forensic\csv\timeline_all.csv:231:"2025-03-07

19:41:11",REG,MOD,0,0x0,0x0,\Root\InventoryApplicationFile\backup.exe|87931ab5a15fc7f5 1

forensic\csv\timeline_all.csv:266:"2025-03-07

19:41:09",NTFS,MOD,0,0x0,0x5efbc400,\1\Windows\Prefetch\BACKUP.EXE-AB6C9DDF.pf 2

forensic\csv\timeline_all.csv:277:"2025-03-07

19:41:08",NTFS,CRE,0,0x0,0x5efbc400,\1\Windows\Prefetch\BACKUP.EXE-AB6C9DDF.pf 3

forensic\csv\timeline_all.csv:1496:"2025-03-07

19:41:04",NTFS,RD,0,0xb49ae6,0x77d06400,"\1\Users\Robert Paulson\Downloads\backup.exe" 4

[...]

1 Registry entry for the application file inventory hive for backup.exe

2 Modification of the prefetch file for backup.exe

3 Creation of the prefetch file for backup.exe

4 Read the backup.exe file from Robert Paulson’s Downloads folder.

Whole-system memory investigation provides the broad visibility needed to understand attacker activity

across the entire system. Use whole-system memory capture when investigating unknown compromises,

mapping attacker lateral movement, or identifying all systems and processes requiring eradication. The

comprehensive nature of whole-system memory analysis makes it particularly valuable during the eradicate

activity, ensuring analysts identify all attacker artifacts before recovery begins.

Network Investigation

Network analysis provides broad visibility into attacker communications and data exfiltration activities.

Unlike host-based investigation, which focuses on individual systems, network analysis reveals how the

attacker moved through the environment, which systems they accessed, and what data they may have

exfiltrated. This broader context of the attacker’s behavior across systems complements the detailed insight

that host-focused analysis provides. This perspective is essential for understanding the full scope of

compromise and identifying all systems requiring eradication efforts.

Network Data Sources

Network investigation during eradication relies on multiple data sources that offer varying levels of visibility

into attacker activity.  Packet capture (PCAP) offers the most detailed view, recording complete network

conversations including payload data. When available, packet captures allow analysts to reconstruct exactly

which data the attacker accessed or exfiltrated, which commands they executed over the network, and

which tools they deployed. However, full packet capture generates enormous storage requirements and is

typically limited to specific network segments or time windows. The cost-benefit of PCAP has also degraded

as encrypted traffic has become the norm: most attacker communications are now encapsulated by TLS,

making captures less valuable for analyzing attacker activity without decryption capabilities in place.

NetFlow and similar flow data (IPFIX, sFlow) provide a more scalable alternative, recording metadata about

volumes, making it valuable for identifying lateral movement and data exfiltration even when packet

captures are unavailable.

DNS logs represent another important data source that attackers often overlook when covering their tracks.

Every system lookup for command-and-control domains, malware distribution sites, or exfiltration

endpoints leaves a record in DNS logs. Proxy logs provide similar visibility into web traffic, capturing URLs,

user agents, and response codes that reveal the behavior of attacker tools and data-staging activities. Many

attackers tunnel their communications through web proxies to blend with normal traffic, making proxy logs

essential for understanding the full scope of attacker operations. Firewall logs round out the perimeter view,

documenting allowed and blocked connection attempts that help identify both successful attacker access

and failed reconnaissance attempts.

Network Detection and Response Platforms

Organizations that have deployed Network Detection and Response (NDR) platforms gain significant

investigative advantages during eradication. While often positioned as tools for threat hunting and real-time

detection, NDR platforms also offer valuable investigative features that help responders understand attacker

activity across the network. These systems integrate multiple detection capabilities, including signature-based alerting, machine-learning-based anomaly detection, behavioral analytics, and threat intelligence

integration. For incident response analysts, alerts generated by NDR platforms provide a valuable

investigative resource, enabling responders to quickly identify suspicious network activity associated with

the incident.

NDR tools often provide built-in investigation workflows that guide analysts through examining network

activity, pivoting from one indicator to related events across the environment. These workflows can

accelerate initial analysis, helping responders identify systems requiring deeper investigation. However,

analysts should treat NDR findings as one input among many rather than a complete picture of attacker

activity. The real value of NDR during eradication lies in its ability to surface connection patterns and

anomalies that point to compromised systems, which responders can then investigate using the network

data sources and connection-mapping techniques described below.

NDR platforms surface connection patterns and anomalies. Use these findings as a starting

point for deeper investigation with other network data sources.

Network Data for Connection Mapping

Beyond NDR platforms, responders can analyze raw network data to map attacker connections directly.

This approach works with the flow data, DNS logs, and firewall logs available in most environments,

providing connection mapping capabilities without specialized NDR tooling. By mapping these connections,

responders can ensure that eradication actions address every compromised system, removing all attacker

access points.

For example, consider an incident where an attacker gained unauthorized access to a system in an AWS

environment. Using Virtual Private Cloud (VPC) flow logs, responders can reconstruct the attacker’s

network connections to identify all the systems they accessed.

One option for visualizing these connections is to generate a network connectivity graph using the VPC

Flow Log Analysis tool. Written by Florian Pfisterer (with a simplified fork by this author), this open-source

tool processes VPC flow logs and generates a visual graph of network connections, with thicker lines

indicating greater data transfer between systems. [11]

Using this author’s fork of the VPC Flow Log Analysis tool, analysts can generate a network connectivity

graph from VPC flow logs collected during the incident. The example in Listing 76  demonstrates the

commands used to combine VPC flow log files collected from the AWS S3 log storage destination, generate

the network graph data, and start a local web server to visualize and interact with the graph. By assigning

host names in the graph-generator/known-ips.ts file, responders can easily review connectivity between the

systems under investigation and other systems in the environment.

Listing 76 | AWS VPC Flow Log Analysis Graph Generation

$ gzcat ~/flowlogs/*.log.gz > flowlogs_combined.txt 1

$ head -4 ../flowlogs_combined.txt

2 058390152209 eni-e362dfbb 10.0.2.1 10.0.3.1 50413 5432 6 11 34622 1764152928 1764152962 REJECT

OK

2 058390152209 eni-e978320b 10.0.2.2 10.0.3.1 56261 5432 6 74 64131 1764153408 1764153436 ACCEPT

OK

2 058390152209 eni-9991a6a9 10.0.5.1 10.0.4.1 65098 443 6 254 2911921 1764155508 1764155560

ACCEPT OK

2 058390152209 eni-429b8a69 10.0.1.1 10.0.2.2 32540 443 6 214 4242067 1764151368 1764151400

ACCEPT OK

$ LOG_TEXT=../flowlogs_combined.txt npm run build-graph 2

> vpc-flow-log-analysis@1.0.0 build-graph

> ts-node ./graph-generator/build-graph.ts

read and parse requests: 63.438ms

Found 90436 requests.

generate nodes and edges: 23.035ms

export graph data to file: 0.718ms

Exported log graph to /Users/jwright/flowlogs/vpc-flow-log-analysis/client/graph.json

$ npm run client 3

> vpc-flow-log-analysis@1.0.0 client

> ./node_modules/http-server/bin/http-server client

Starting up http-server, serving client

Available on:

hxxp://127[.]0[.]0[.]1:8080

hxxp://192[.]168[.]1[.]140:8080

Figure 99 | AWS VPC Flow Log Connection Graph

Network investigation findings directly inform eradication scope: every system the attacker accessed

requires examination for persistence mechanisms, every external IP address contacted should be blocked,

and every compromised credential used for lateral movement should be rotated. Visualization or other

network mapping techniques help responders understand the attacker’s actions and ensure eradication

actions address all compromised systems.

Malware Investigation

When malware is discovered during the incident, detailed analysis becomes essential for effective

eradication. Understanding what the malware does, how it persists, and what network infrastructure it uses

directly informs eradication actions: responders need to know what artifacts to remove, what network

connections to block, and what other systems might be infected with the same malware.

Malware analysis during eradication serves specific practical objectives. The primary goals focus on

gathering actionable intelligence: determine whether a suspicious file is malicious, enumerate the artifacts

it creates (files, registry keys, and processes), identify persistence mechanisms that require removal, and

extract network indicators of compromise (IOCs) for continued scoping and containment.

Malware investigation involves both static and dynamic analysis techniques. While comprehensive malware

analysis is a specialized discipline that requires extensive expertise, incident responders need fundamental

capabilities to assess whether executables are malicious and understand their basic functionality.

SAFETY IN MALWARE ANALYSIS

Analysts should apply caution when working with and handling malicious code. It is very easy to

accidentally execute malware during analysis, to distribute it unintentionally, or to tip off attackers

that their code is being studied.

Safe malware analysis requires strict isolation procedures:

• Use a dedicated analysis system that never connects to production networks.

• Never store production data, credentials, or sensitive information on analysis systems.

• Whenever possible, perform analysis in virtual machines with snapshots for quick restoration to a

clean state.

• Disable shared folders, clipboard sharing, drag-and-drop, and other VM integration features.

• Avoid using broadly-accessible network storage for malware samples.

• Transport malware samples on clearly labeled removable media, encrypted and password-protected.

• For high-risk samples, use air-gapped systems with no network connectivity.

Malware investigation can provide valuable insight into the incident response process, but requires

careful handling to avoid unintended consequences.

Static Analysis

Static analysis involves examining the malware binary without executing it. This approach is safer than

running the malware (though it still requires safe handling of the malware; see the sidebar Safety in Malware

Analysis) and can quickly reveal useful information about the sample’s purpose and capabilities.

Static analysis techniques can include:

• File identification (name, size, metadata attributes)

• File hashing

• Strings extraction

• PE (Portable Executable) structure analysis

• Disassembly of code sections

• Cross-referencing observed artifacts with threat intelligence sources

Basic identification and file hashing provide a foundation for further analysis with cyber threat intelligence

(CTI) sources. Threat intelligence platforms like VirusTotal, Hybrid Analysis, and other online services allow

analysts to submit file hashes and retrieve existing analysis reports. Using a hash (or other identifying

characteristic, such as a string-based search) allows analysts to collect and review CTI insight without

Figure 100 | VirusTotal Search Result for File Hash

If the hash matches a known malware family, analysts may find existing analysis reports for

other samples in the same family that describe the malware’s behavior, persistence

mechanisms, and network infrastructure, potentially saving hours of manual analysis.

Different malware versions in the same family will often share similar characteristics,

allowing responders to apply existing knowledge to new samples.

Analysts can gain considerable insight by analyzing file metadata and the structure of malware samples.  For

Windows malware samples, PE (Portable Executable) analysis tools like PE Studio or PE-Bear reveal

compilation timestamps, imported libraries and functions, embedded resources, and digital signature

information. Imported functions can reveal what capabilities the malware uses: imports from ws2_32.dll

indicate network activity, crypt32.dll suggests encryption routines, and advapi32.dll functions like

RegSetValueEx indicate registry manipulation. The example in Figure 101  shows PE-Bear’s analysis of a

malware sample, revealing imported functions from kernel32.dll including functionality to determine if the

malware is running in a debugger, a common tactic used to detect a sandboxed environment.

Figure 101 | PE-Bear PE Malware Analysis Example

For deeper analysis, tools like Ghidra reveal the disassembled code, though this level of analysis requires

significant expertise and time.

Static analysis provides analysts with valuable insight into malware samples without the risks associated

with execution. However, it has limitations: static analysis may not reveal the full behavior of the malware,

especially if it employs obfuscation or other anti-analysis techniques. To gain a more comprehensive

understanding of malware functionality, dynamic analysis is often necessary.

Dynamic Analysis

Dynamic analysis involves executing the malware in a controlled environment and observing its behavior.

This approach reveals what the malware actually does rather than what it might do. The tradeoff is

increased risk: analysts will be running malicious code, which requires careful isolation to prevent

unintended consequences.

The basic workflow for dynamic analysis follows a consistent pattern:

• Prepare the environment : Start and configure monitoring tools, but keep recording disabled until

analysis begins.

• Snapshot the environment: Take a virtual machine snapshot immediately before executing the malware

to accommodate quick restoration.

• Enable monitoring tools : Start recording with the desired monitoring tools before launching the

malware sample.

• Execute the malware : Run the sample and interact with it as needed to trigger functionality (clicking

prompts, providing input, or waiting for scheduled triggers).

• Terminate the malware: End the malware process using commands such as kill or Stop-Process, or via

GUI tools.

• Stop monitoring tools: Disable recording to capture a clean end state.

• Review the output : Analyze captured data to identify artifacts, persistence mechanisms, and network

activity.

This dynamic analysis process is iterative. Each time analysts complete the basic workflow, they will learn

more about the malware. It is often necessary to repeat the dynamic analysis multiple times to obtain a

complete picture of the malware’s behavior.

Monitoring or instrumentation tools capture the malware’s behavior during execution.  For Windows

systems, Process Monitor from Sysinternals is a widely used tool for dynamic analysis. Analysts can

configure Process Monitor to capture detailed file system, registry, network, and process activity, using

filtering features to focus on the malware process and its children. The example in Figure 102 shows Process

Monitor capturing activity from a malware sample, revealing process execution for cmd.exe.

Figure 102 | Process Monitor Dynamic Analysis Example

Automated sandbox platforms also offer an alternative to manual dynamic analysis.  Online services like

Hybrid Analysis and Joe Sandbox execute samples in instrumented environments and produce detailed

behavioral reports. These platforms handle the isolation and monitoring complexity, providing reports that

enumerate file system changes, registry modifications, network connections, and process activity. For

known malware families, sandbox reports often provide sufficient detail to guide eradication without

requiring manual analysis.

Practical Limitations

Not all malware yields to basic analysis techniques. Recognizing when a sample exceeds the capabilities of

the incident response team and requires specialist assistance is important:

• Heavy obfuscation or packing: When string extraction reveals nothing readable and static analysis tools

show encrypted or compressed content, the malware authors have deliberately hidden functionality.

Unpacking requires specialized skills and tools.

• Anti-analysis techniques : Some malware detects virtual machines, debuggers, or sandbox

environments and either refuses to execute or behaves differently in them. If dynamic analysis produces

no activity, the sample may be evading the analysis environment.

• Kernel-mode rootkits : Malware operating at the kernel level requires specialized tools and kernel

debugging expertise.

• Cryptographic analysis : Advanced ransomware assessment to determine whether decryption is

possible often requires malware reverse engineering and cryptographic expertise.

When necessary, engage specialized malware analysis resources, whether internal security research teams,

managed security service providers, or external forensic consultants.

A combination of signals often tips the balance toward external help: the sample does not appear in

VirusTotal or other community repositories; static analysis reveals heavy packing or obfuscation; and the

in-house team is already struggling to make progress. Together, these three signals can suggest the

malware is not a commodity-level variant, and continuing to work the sample without a specialist retainer

can waste days of eradication time. Engaging retainer IR support early in this scenario is usually faster and

cheaper than doing so after several days of unsuccessful analysis.

The goal of malware analysis during eradication is to obtain insight for practical action. Focus analysis

efforts on answering specific questions: what does this malware create, where it persists, what needs to be

done to remove it, and how the findings can help scope other infected systems.

Business Email Compromise Investigation

Business Email Compromise (BEC) incidents involve attackers gaining access to or impersonating business

email accounts to commit financial fraud. Unlike malware-driven intrusions, BEC cases rarely involve

malicious executables or host-based persistence.  Instead, attackers rely on legitimate identity credentials

and built-in email features such as forwarding rules, OAuth app grants, legacy protocol access, and token

reuse.

BEC attacks have resulted in over $55 billion in losses since 2013, making them among the most financially

impactful cyber threats organizations face. [12]

Threat actors conduct extensive reconnaissance before

attacking, researching organizational structure, identifying employees with financial decision-making

authority, and studying communication patterns. Common targets include executives, attorneys,

accounting staff, and anyone authorized to initiate wire transfers or modify payment details. This

preparation allows attackers to craft convincing requests that exploit trust relationships and business

processes.

BEC incidents present unique eradication challenges because the most valuable investigative artifacts live in

cloud identity and email platforms rather than on endpoints. Initial access methods range from credential

phishing to OAuth token hijacking, and attackers with administrative access to email systems represent the

biggest threat. Administrative access allows attackers to create mail flow rules, forwarding configurations,

and other changes to email systems that execute fraudulent attack elements without any visibility on end-user devices. Successful investigation requires that analysts understand the exploited access vectors, the

operational changes to mail delivery systems, and the enumeration of fraudulent transactions committed

during the attack.

Email System Investigation

When conducting a BEC investigation, analysts should examine mailbox rules and message forwarding

configurations on affected accounts. BEC attackers frequently create inbox rules that automatically forward

copies of incoming email to external addresses, delete messages from specific senders (particularly security

alerts or responses from fraud targets), or move messages to obscure folders where victims will not notice

them. These rules provide persistent access to communications even after the attacker’s initial access is

inbox rules for affected accounts. The ForwardTo, DeleteMessage, and MoveToFolder attributes will reveal any

policy actions taken on inbound messages. The example in Listing 77 demonstrates how to list inbox rules

for a specific user account, revealing any rules that might indicate attacker persistence.

Listing 77 | Enumerating Inbox Rules for BEC Investigation

PS C:\> Get-InboxRule -Mailbox "jwalcott@falsimentis.com" | Select-Object Name, Description,

Enabled, ForwardTo, DeleteMessage, MoveToFolder | Format-List 1

Name          : Daily Reports

Description   : Move daily reports to Reports folder

Enabled       : True

ForwardTo     :

DeleteMessage : False

MoveToFolder  : Reports

Name          : auto-archive 2

Description   :

Enabled       : True

ForwardTo     : dxvpflrcdhquzyixdn@midnitemeerkats.com 3

DeleteMessage : True

MoveToFolder  :

1 Enumerate inbox rules for the CEO account.

2 Suspicious rule forwarding email externally and deleting the original message.

3 External forwarding address controlled by the attacker.

Examine organization-level mail flow and transport rules for incidents involving administrative access.

Sophisticated BEC attackers may create organization-wide rules that redirect specific messages, block

security notifications, or allow domains under their control to bypass inbound message controls.

SUBLIME EML ANALYZER: FREE AND POWERFUL EMAIL ANALYSIS TOOL

The Sublime EML Analyzer  is a free tool that parses raw (EML-formatted) email messages and

evaluates them against the Sublime Core Feed, a curated set of detection rules maintained by the

Sublime security research team. Analysts can upload a suspicious email message and receive

immediate analysis that identifies phishing indicators, spoofing techniques, malicious attachments,

and social engineering patterns without needing to manually inspect headers or decode message

content.

Figure 103 | Sublime EML Analyzer Message Analysis Sample

The value for incident responders is speed and coverage. Rather than manually reviewing email

headers for authentication failures or examining URLs one at a time, the EML Analyzer applies

hundreds of detection rules simultaneously and returns results organized by severity. During a BEC

investigation, this can quickly confirm whether a suspicious message matches known phishing

patterns, identify the specific techniques used to bypass email security controls, and provide

evidence for the investigation timeline.

Identity and Access Investigation

Review OAuth application permissions and third-party integrations for each affected account.  Modern BEC

attacks often involve OAuth consent phishing, in which victims grant malicious applications access via

OAuth consent flows. These applications maintain access to email even after password resets, making them

a persistent threat that password rotation alone will not resolve.

For Microsoft 365 environments, use Microsoft’s Get-AzureADPSPermissions.ps1 script to enumerate all

delegated permission grants across the tenant as shown in Listing 78. [13]

This script inventories delegated

permissions and application permissions, revealing which applications have access to user data and what

level of access they possess. The output CSV file lists all applications with granted permissions, allowing

analysts to identify any high-privilege applications that may have been authorized during the compromise

window.

Listing 78 | Enumerate Delegated Permissions in Microsoft Entra

PS C:\IR> .\Get-AzureADPSPermissions.ps1

Connecting to Microsoft Graph...

Retrieving OAuth2PermissionGrants...

Exporting results to .\Permissions.csv

PS C:\IR> Get-Item .\Permissions.csv

Directory: C:\IR

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

-a---         11/28/2025  10:13 AM         24576 Permissions.csv

Listing 79 | Review Delegated Permissions in Microsoft Entra

PS C:\IR> Import-Csv .\Permissions.csv

[...]

TenantId           : 7f3e74e1-3855-4d44-a3db-5f3f9b37a1f9

UserDisplayName    : Lukas Dolman

UserPrincipalName  : ldolman@falsimentis.com

UserObjectId       : ecb20947-41fd-47c3-b27a-31c88a0e2a69

ClientAppId        : 7486f14b-2bc5-42f8-87bd-a2d1b5725db6

ClientName         : Power BI Reports Viewer

Permission         : Calendars.Read, Calendars.Read.Shared

ConsentType        : Principal

ConsentCreatedDate : 2024-05-09T16:22:54Z

TenantId           : 7f3e74e1-3855-4d44-a3db-5f3f9b37a1f9

UserDisplayName    : <tenant-wide>

UserPrincipalName  : <tenant-wide>

UserObjectId       : 00000000-0000-0000-0000-000000000000

ClientAppId        : 67c06044-2e2d-4cae-91e3-32ba827ac202

ClientName         : SecureSync Data Connector

Permission         : email, offline_access, Mail.ReadWrite, Mail.Send, Files.ReadWrite.All 1

ConsentType        : AllPrincipals

ConsentCreatedDate : 2025-11-26T03:41:09Z

1 Delegated permissions indicate a potential BEC persistence mechanism.

Look for applications with high-privilege permissions, such as email, Mail.ReadWrite, Mail.Send, or

MailboxSettings.ReadWrite that were granted during the compromise window. Applications with these

permissions can enumerate, read, send, and manage email without user interaction, making them effective

persistence mechanisms for BEC attackers.

Investigate delegated permissions and multi-mailbox access configurations. Attackers with access to one

compromised account often grant themselves additional permissions to access other mailboxes. Look for

recently added mailbox delegation permissions, particularly "Full Access" or "Send As" permissions that

allow one user to read another user’s email or send email on their behalf. These permissions persist

independently of password changes and require explicit revocation. For Microsoft 365 environments, use

Get-MailboxPermission and Get-RecipientPermission to identify all delegated access configurations across

affected accounts.

Financial Transaction Investigation

Another important element in a BEC investigation is to analyze financial transactions initiated during the

compromise window. These resources will vary considerably by environment and will require close

coordination with finance and accounting teams to identify relevant transactions.

Analyze authentication logs and sign-in patterns to establish the timeline of attacker access. Review sign-in

logs for suspicious patterns such as impossible travel (logins from geographically distant locations within

short time periods), sign-ins from unusual locations or IP addresses, or multiple accounts accessed from the

same IP address. This analysis helps identify the scope of compromise and any additional accounts requiring

investigation.

In Microsoft 365 environments, export sign-in logs from the Entra admin center and analyze location

patterns using PowerShell. The script in Listing 80  parses exported sign-in logs and displays each

authentication event with timestamp and location, sorted by user and time.

Listing 80 | Analyzing Sign-In Locations from Exported Logs

PS C:\IR> $signins = Get-Content .\SignInLogs.json | ConvertFrom-Json

PS C:\IR> $signins | Select-Object userPrincipalName, createdDateTime,

@{Name='Location';Expression={"$($.location.city), $($.location.state)"}}, 1

ipAddress | Sort-Object userPrincipalName, createdDateTime | Format-Table

userPrincipalName       createdDateTime        Location          ipAddress

-----------------       ---------------        --------          ---------

ldolman@falsimentis.com 11/26/2025 3:35:25 AM  Ashburn, Virginia 44.206.5.255

ldolman@falsimentis.com 11/26/2025 3:37:10 AM  Ashburn, Virginia 3.216.143.186

ldolman@falsimentis.com 11/26/2025 3:38:14 AM  Columbus, Ohio    3.12.218.40 2

ldolman@falsimentis.com 11/26/2025 3:39:18 AM  Ashburn, Virginia 44.220.31.71

ldolman@falsimentis.com 11/26/2025 3:40:22 AM  Columbus, Ohio    3.145.230.62

[...]

1 Calculated property combines city and state into a single Location column.

2 Sign-ins alternating between Virginia and Ohio within minutes indicate an impossible travel scenario.

The output in Analyzing Sign-In Locations from Exported Logs reveals an impossible travel pattern: the user

ldolman@falsimentis.com authenticated from both Ashburn, Virginia, and Columbus, Ohio, within a five-minute window. Since these locations are approximately 300 miles (482 kilometers) apart, physical travel

Coordinate with finance and accounting teams to trace any fraudulent transactions initiated during the

compromise window. BEC attackers often monitor email traffic for weeks before striking during major

payment periods, or end-of-quarter rushes when workload may increase the likelihood of a successful

attack. Review wire transfer requests, invoice payments, and vendor payment modifications that occurred

during the identified compromise period.

Victim by Proxy

Not every BEC incident involves a compromise of the victim organization’s own email or identity systems. In

a common variant, a supplier’s mailbox is compromised, the attacker inserts messages into an established

payment thread, and the victim pays a fraudulent account in good faith. The organization typically becomes

aware only when the real supplier chases the unpaid invoice days or weeks later, as shown in Figure 104.

Figure 104 | Victim-by-Proxy BEC Scenario

Investigation in this scenario is constrained by the artifacts the victim actually has. The victim’s own mail

flow, identity logs, and endpoints show no compromise because there was none. The evidence available is

the email that arrived in the victim’s inbox, the payment records in the accounts payable system, and

whatever the supplier is willing to share about its own incident. In this scenario, the IRT can focus the

investigation on three areas:

• Email header and content analysis : Examine the headers of the messages that instructed the payment

change. Compare the sending domain to the supplier’s legitimate domain for lookalike substitutions (for

example, wehost4every1.com versus wehost4evrey1.com), and check for reply-to addresses that diverge

from the From address.

• Domain registration timing : Query WHOIS for the apparent sender’s domain. A lookalike domain

registered days or weeks before the first suspicious email is a strong indicator of a staged BEC attack

rather than a legitimate communication. The same check on the victim organization’s own domain

sometimes reveals that the attacker also registered a lookalike of it, typically after extracting payment,

to intercept the supplier’s follow-up messages and delay discovery.

• Information flow analysis : Check whether the attacker introduced new information or only replayed

information the victim had already sent. An attacker operating from a compromised thread often can

only mirror the victim’s own details with plausible filler between them, while a legitimate supplier

typically provides new details such as invoice numbers or payment confirmations the victim has not

seen.

When the compromise is on the supplier’s own email server rather than a lookalike domain,

fraudulent messages share the same technical fingerprint as legitimate ones: identical

sending mail server, matching SPF and DKIM results, consistent user agent, and consistent

message headers. The victim organization has no technical basis to differentiate attacker-initiated messages from genuine supplier email. As the victim-by-proxy organization, use

that technical consistency when communicating with the supplier’s security team:

messages that pass every authentication check from the supplier’s own infrastructure are

themselves evidence the compromise sits on the supplier’s side, supporting the case to

advocate a thorough investigation on their end.

Coordinate with the supplier’s security team if they engage. Remote organizations are often reluctant to

Investigation should focus on three primary areas: data access patterns, privilege changes, and exfiltration

methods. Review pertinent data access logs, application access logs, and cloud storage records to identify

which data the insider accessed and whether they downloaded or transferred information outside normal

business patterns. Examine recent changes to user accounts, group memberships, and permission

assignments that may indicate privilege escalation. Analyze email logs, cloud storage uploads, USB device

connections, and any data leakage alerts to understand how data may have left the environment.

Technically sophisticated insiders may create persistence mechanisms to maintain access after their

primary credentials are revoked. Look for remote access tools, secondary accounts, or modified system

configurations that could allow continued access. Understanding these mechanisms during investigation

ensures that subsequent eradication actions address all access paths.

Document all investigation findings meticulously, as insider threat cases frequently result in legal

proceedings. Maintain detailed records of the insider’s access, the unauthorized activities discovered, and

the data accessed or exfiltrated. Work closely with legal counsel throughout the investigation to ensure that

evidence collection aligns with legal requirements and supports the organization’s goals in responding to

the threat.

INSIDER THREAT FROM DAY ONE: KNOWBE4’S NORTH KOREAN IT WORKER

In July 2024, security awareness training company KnowBe4 discovered it had hired a North Korean

threat actor posing as a remote IT worker. [14]

The attacker passed four video interviews using an AI-enhanced photograph derived from a stock image (as shown in Figure 105 ), cleared background

checks using a stolen U.S. identity, and provided verified references prior to hire.

Figure 105 | Stock Photo (Left) and AI Fake (Right) Used by North Korean Threat Actor

Upon receiving a company-issued workstation sent to a U.S. address, an accomplice connected the

laptop to a Raspberry Pi device, extending access to the North Korean threat actor’s location. The

threat actor used the laptop remotely, working overnight to simulate normal business hours in the

U.S. Shortly thereafter, the KnowBe4 SOC detected unusual activity from the new hire’s account.

“On July 15, 2024, a series of suspicious activities was detected on the user beginning at 9:55pm EST

(sic; July 15 is EDT ). When these alerts came in KnowBe4’s SOC team reached out to the user to

inquire about the anomalous activity and possible cause. XXXX responded to SOC that he was

following steps on his router guide to troubleshoot a speed issue and that it may have caused a

compromise.

Following additional suspicious behavior, including manipulated session history data, harmful file

transfers, and attempts to execute unauthorized software, the KnowBe4 SOC terminated the

employee’s access and began a full investigation. The investigation revealed that no company data

was compromised due to KnowBe4’s restricted system and data access policies for new employees,

which prevented the attacker from accessing sensitive systems. Further, the quick actions to identify

and contain the insider threat limited the attacker’s ability to establish deeper persistence in the

KnowBe4 environment.

This incident demonstrates that insider threats can begin on day one of employment. It highlights the

value of KnowBe4 defense-in-depth controls to limit insider threats from new hires, including least-privilege access, robust monitoring, and rapid incident response.

Supplier and Supply Chain Investigation

Supply chain compromises present unique eradication challenges because the malicious code or access

often arrives through trusted channels and legitimate update mechanisms. When a supplier or partner

organization is compromised, the attacker gains access to multiple downstream organizations

simultaneously, and eradication requires not only removing the attacker’s artifacts from the environment

but also understanding the scope of the supply chain compromise across the broader ecosystem.

Supply chain attacks fall into four broad categories, each requiring different investigation and eradication

approaches:

• Hardware supply chain attacks, in which physical devices are modified during manufacturing, shipping,

or maintenance.

• Software supply chain compromises, in which software the organization runs in its own environment is

poisoned upstream from software vendors or open-source projects.

• SaaS vendor compromises, in which a vendor runs the software and the organization places its data on

the vendor’s platform.

• Managed service provider and staff access compromises , in which a vendor’s staff or expertise is

provided to the organization with legitimate access to its environment.

The sections that follow examine each of these threat categories in more detail.

Software Supply Chain Compromises

Software supply chain compromises affect software that the organization runs in its own environment,

where an upstream vendor’s product or package has been poisoned and reaches the environment through

Boundary software : These products operate at the network edge: firewalls, VPN concentrators, remote

access gateways, and similar edge appliances. A compromise exposes the organization’s full internal

network to an attacker holding a privileged vantage point, and detection is complicated because the

compromised device is often the same device the organization relies on for security controls.

Internal software: Libraries, data center appliances, internal applications, and developer toolchains all run

inside the organization’s systems. A compromise here typically requires the attacker to traverse the

environment laterally to reach high-value targets, but the breadth of internal software and its dependencies

(captured by supply chain risks such as the Apache Log4j vulnerability) makes the search surface large.

When attackers compromise software vendors and inject malicious code into legitimate software updates,

the resulting compromises appear to come from trusted sources and may bypass security controls that

would normally detect malicious activity. In a software-based supply chain compromise, start by identifying

all systems that installed the compromised software version. Review software deployment logs, package

manager histories, and endpoint management systems to build a comprehensive list of affected systems.

This scope may extend beyond initially identified systems due to the pervasive nature of supply chain

attacks.

Analyze the malicious code to understand its capabilities and artifacts. Work with the software vendor to

obtain information about indicators of compromise specific to the compromised version. Since supply chain

incidents can affect so many end users, security researchers and the incident response community often

share IOCs for major supply chain incidents shortly after identification.

For example, a 2025 supply chain attack discovered by GitLab’s Vulnerability Research Team identified

multiple compromised Node Package Manager (NPM) packages with a worm-like propagation mechanism to

distribute the Shai-Hulud malware. [15]

In their assessment of the incident, GitLab researchers shared

multiple IOCs to identify the malicious artifacts created by the compromised NPM packages, as shown in

Table 26.

Table 26 | GitLab NPM Supply Chain Compromise IOCs

TYPE INDICATOR DESCRIPTION

File bun_environment.js Malicious post-install script in node_modules

directories

Directory .truffler-cache/ Hidden directory created in user home for

Trufflehog binary storage

Directory .truffler-cache/extract/ Temporary directory used for binary

extraction

File .truffler-cache/trufflehog Downloaded Trufflehog binary (Linux/Mac)

File .truffler-cache/trufflehog.exe Downloaded Trufflehog binary (Windows)

Process del /F /Q /S "%USERPROFILE%`" Windows destructive payload command

Process shred -uvz -n 1 Linux/Mac destructive payload command

Process cipher /W:%USERPROFILE% Windows secure deletion command in

payload

TYPE INDICATOR DESCRIPTION

Command curl -fsSL hxxps://bun[.]sh/install

| bash

Suspicious Bun installation during NPM

package install

Command powershell -c "irm

bun.sh/install.ps1|iex"

Windows Bun installation via PowerShell

Use threat intelligence platforms and malware analysis tools to gather IOCs related to the

specific supply chain compromise to support more comprehensive investigation efforts.

Supply chain malware is often designed to meet specific goals such as committing financial fraud (including

decentralized finance/cryptocurrency theft), gaining persistence on compromised endpoints, exfiltrating

data, or conducting hacktivist campaigns. Examine the affected software elements to identify the possible

goals of the attack and guide subsequent assessment. For example, if malware distributed through a supply

chain compromise includes functionality to establish persistence or facilitate remote access, analysts should

investigate whether the compromised software was used to move laterally within the environment.

Sophisticated supply chain attacks will use the initial compromise as a foothold for further activity. Review

logs from affected systems for signs of lateral movement, credential dumping, or deployment of additional

tools. The scope of eradication may extend well beyond removing the compromised software if the attacker

used it to establish additional persistence.

VENDOR BREACH ACCOUNTABILITY: MARQUIS V. SONICWALL

When a vendor compromise leads to a downstream customer breach, the question of legal

accountability becomes significant. A growing number of organizations are pursuing litigation against

their security product and service vendors, shifting breach-related lawsuits from the traditional

consumer-to-company direction toward enterprise-to-vendor claims.

In August 2025, ransomware actors breached Marquis, a fintech company providing marketing and

compliance solutions to more than 700 banks and credit unions. The attack exposed Personally

Identifiable Information (PII) belonging to customers of Marquis’s clients. A month later, Marquis’s

firewall vendor, SonicWall, disclosed that it had suffered a breach, with attackers stealing customer

firewall configuration files from its cloud backup service. SonicWall initially claimed only 5% of

customers were affected, then revised that figure to 100%. [16]

Marquis filed suit against SonicWall in February 2026, alleging that SonicWall’s delayed and

incomplete disclosure prevented Marquis from mitigating the harm to its customers. According to

Marquis, SonicWall assured them that their firewall protection was unaffected for several weeks after

the compromise (presumably under the initial 95% unaffected group). Marquis alleges that SonicWall’s

failure to disclose the full scope of the breach in a timely manner allowed attackers to continue

exploiting the compromised firewalls, leading to the downstream breach at Marquis.

This case is part of a broader trend. In 2018, a breach at email security vendor Barracuda Networks

exposed personal health information from one of its clients, Zoll Services, leading to a lawsuit that

ultimately favored Barracuda. The 2023 MOVEit breach (see Modern Breach Complexity: The MOVEit

Supply Chain Attack) sparked dozens of lawsuits against the vendor, many of which remain pending.

products or services fail is increasing.

For incident response teams, these developments reinforce the importance of documenting vendor

interactions during an incident, particularly around disclosure timelines and the accuracy of vendor

communications about impact scope. Organizations should also review vendor contracts to confirm

they include notification requirements, indemnification clauses that hold the vendor accountable for

losses caused by their products or services, and clear accountability for security failures.

Hardware Supply Chain Attacks

Hardware supply chain compromises involve physical modifications to devices during manufacturing,

shipping, or maintenance. These attacks are rare but extremely difficult to detect and eradicate. Indicators

include unexpected firmware modifications, unauthorized hardware components, or unusual device

behavior that cannot be explained by software analysis.

Physical hardware modifications cannot be remedied by software and typically require hardware

replacement. Conduct a thorough inspection of suspicious devices to identify unauthorized chips, modified

firmware, or unexpected network behavior at the hardware level.

Document all serial numbers, procurement sources, and shipping chains for affected hardware. This

information helps determine the scope of potential compromise and whether other devices from the same

batch or supplier may be affected. Coordinate with hardware vendors and law enforcement, as hardware

supply chain attacks often have broader implications beyond a single organization.

COUNTERFEIT CISCO EQUIPMENT IN MILITARY SYSTEMS

In 2024, the U.S. Department of Justice sentenced the operator of a decade-long counterfeit

networking equipment scheme to more than six years in prison. [17]

The scheme imported tens of

thousands of low-quality network devices from China and Hong Kong, applied counterfeit Cisco

labels and packaging, and then sold them through Amazon and eBay storefronts, making over $100

million in revenue.

The counterfeit equipment ended up in hospitals, schools, government agencies, and military

systems, including platforms supporting U.S. fighter jets and aircraft flight simulators. Security

researchers including F-Secure Labs who analyzed similar counterfeit Cisco switches found hardware

implants (as shown in Figure 106) designed to bypass the device’s Secure Boot protections, allowing

modified firmware to run without detection. [18]

Figure 106 | Counterfeit Cisco WS-2960X-48TS-L V01 Switch with Hardware Modification

This case illustrates the investigative challenges posed by hardware supply chain attacks. Attackers

placed hardware implants inside network infrastructure devices, then injected them into corporate

and government procurement channels. Unlike software compromises, which forensic analysis can

identify, hardware implants may not contain obvious backdoors. Analysis reports for these

counterfeit devices indicate that the implanted hardware existed solely to bypass authentication

checks and run pirated software to avoid detection as counterfeit devices. However, the same

techniques could just as easily enable persistent backdoor access that survives firmware updates and

factory resets.

SaaS Vendor Compromises

SaaS vendor compromises occur when a vendor runs software on behalf of the organization and stores the

organization’s data on that platform. The organization’s own environment remains intact, but its data,

authentication tokens, or integrations hosted by the vendor are exposed through the vendor’s compromise.

Eradication focuses on cutting off data flows, rotating credentials stored at the vendor, and auditing

downstream systems that trusted tokens issued through the compromised integration.

Start by enumerating what data and credentials the organization shared with or stored on the compromised

vendor. Many SaaS integrations maintain OAuth tokens, API keys, or service credentials on the vendor’s

platform so that the vendor can act on the organization’s behalf, and a compromise of the vendor exposes

all of those credentials simultaneously.

Work with the vendor to obtain compromise timelines and specific IOCs, then check the organization’s own

logs for abuse of any credential that was stored at the vendor: API calls from unexpected sources, token

incidents where the partner reports evidence of specific data exposure, enumerate the disclosed data to

identify what information may have been affected, and apply non-disclosure agreements as needed to

collect detailed information from the partner to assess risk and impact.

SUPPLY CHAIN COMPROMISE: THE SALESLOFT DRIFT INCIDENT

Drift is a conversational marketing platform that provides AI-powered chatbots for business websites.

When visitors land on a company’s website, Drift engages them through automated chat, qualifies

leads, answers questions, and routes high-intent prospects to human sales representatives. The

platform supports over fifty third-party integrations, including Salesforce, Slack, HubSpot, Zendesk,

GitHub, Google Workspace, and others. [19]

In August 2025, attackers compromised Salesloft’s Drift platform and stole OAuth tokens that

provided access to customer environments. Using a single stolen Salesloft token, the threat actor

could access tokens for any organization that had linked Drift to its systems. Google Threat

Intelligence identified over 700 potentially impacted organizations whose connected platforms were

exposed through this single point of compromise. [20]

The attackers systematically exploited this access to query integrated platforms for sensitive data.

They extracted customer records, sales opportunities, and support cases from Salesforce instances.

More importantly, they harvested credentials stored within these systems: AWS access keys, VPN

credentials, Snowflake tokens, and other secrets that organizations had stored in connected

platforms. These stolen credentials opened doors to yet more systems, creating a cascading

compromise that extended far beyond the original Drift integration.

“Google warns the breach goes far beyond access to Salesforce data, noting the hackers responsible

also stole valid authentication tokens for hundreds of online services that customers can integrate

with Salesloft, including Slack, Google Workspace, Amazon S3, Microsoft Azure, and OpenAI. [21]

- Brian Krebs, Krebs on Security

On August 20, 2025, Salesloft and Salesforce revoked all active access and refresh tokens, and

Salesforce removed Drift from their partner marketplace. Organizations affected by this compromise

faced eradication challenges extending across every system that had integrated with Drift. They

needed to identify which credentials were stored on connected platforms, rotate all potentially

exposed secrets, audit downstream systems such as AWS and Azure for unauthorized access, and

monitor for extortion attempts using harvested data.

The Drift incident illustrates how modern supply chain compromises cascade through

interconnected systems. A single compromised service provider exposed not only its own data but

also authentication materials that unlocked access to dozens of other platforms, which in turn

contained credentials for yet more infrastructure. Each layer of integration amplified the blast radius

of the original breach.

On the remediation side, rotate all credentials that the organization stored with the vendor, revoke OAuth

grants the vendor held to the organization’s systems, and coordinate with the vendor on removing the

organization’s data from the compromised environment if the data can no longer safely reside there.

Managed Service Provider and Staff Access Compromises

Managed service provider and staff access compromises occur when a vendor provides personnel or

expertise to the organization with legitimate access to its environment. Examples include IT outsourcing

arrangements, in which vendor staff operate inside the organization’s network under their own or shared

accounts, and specialist engagements in which a vendor’s consultants hold administrative credentials for a

bounded project. A compromise of the vendor’s own environment, or of the vendor’s identity infrastructure,

becomes a compromise of the access that vendor holds to the organization.

When responding to this type of compromise, start by identifying all access points the vendor has into the

environment, including VPN connections, API integrations, federated authentication, and shared

infrastructure. Review authentication logs for all accounts associated with the vendor and its staff. Look for

unusual access patterns, access from unexpected locations, or access during timeframes when the vendor

was known to be compromised.

Rotate credentials and tokens the vendor holds for the organization before declaring eradication complete.

Depending on the access model, rotation may require re-provisioning accounts, re-issuing tokens, and re-establishing federation trust with the vendor’s identity provider.

Coordinate with the compromised supplier or partner throughout the eradication process regardless of

which category applies. They may have valuable information about the attacker’s capabilities, IOCs specific

to the compromise, and the timeline of malicious activity. When possible, share information about what the

investigation uncovers, as these findings may help the supplier understand the broader impact of their

compromise.

Cloud Investigation

Cloud environments introduce investigation and eradication challenges that depart from the procedures of

traditional on-premises infrastructure. The ephemeral nature of cloud resources, the prevalence of

infrastructure-as-code, and the complex identity and access management systems require different

approaches to understanding and removing the presence of attackers.

Cloud incidents typically fall into two main categories requiring distinct eradication techniques:

Infrastructure-as-a-Service (IaaS) compromises involving virtual machines, containers, and storage, and

Software-as-a-Service (SaaS) compromises involving cloud applications, OAuth tokens, and API abuse.

IaaS Investigation and Eradication

Infrastructure-as-a-Service compromises present two distinct attack surfaces that require different

investigative approaches: the cloud control plane and the infrastructure itself. Understanding this

distinction helps structure a thorough investigation before removing the attacker’s access.

Cloud Control Plane Investigation

The cloud control plane encompasses all the management APIs, IAM systems, and configuration services

that govern how cloud resources are created, modified, and accessed. Attackers who compromise control

plane access can create new resources, modify security configurations, and establish persistence

mechanisms that survive infrastructure rebuilds.

Control plane investigation relies primarily on log analysis and differential analysis.  Review cloud provider

audit logs (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) to identify all API calls made during

actions that could establish persistence or expand access.

Differential analysis compares the current environment against a known-good baseline (see the sidebar

Differential Analysis for Threat Investigation ). Organizations using Infrastructure-as-Code (IaC) tools like

Terraform, CloudFormation, or Pulumi can compare the deployed state against their source-controlled

definitions to identify unauthorized changes. For environments without IaC, compare against documented

architecture diagrams, previous configuration exports, or pristine reference environments. Pay particular

attention to IAM policies, assume-role trust relationships, security groups, and resource configurations that

differ from expected baselines.

Investigate IAM thoroughly. Attackers frequently create new roles, modify existing policies, or add

themselves to privileged groups.  Examine assume-role policies that allow cross-account access, as

attackers may use compromised credentials to pivot to other AWS accounts or Azure subscriptions. For

example, the AWS IAM enumeration example in Listing 81  lists all IAM roles with sts:AssumeRole

permissions, revealing roles that can be assumed by other principals including an external AWS account

identified as 013628954028.

Listing 81 | Enumerate AWS IAM Roles with AssumeRole Permissions

$ aws iam list-roles | jq -r '

.Roles[]

| .RoleName as $r

| .AssumeRolePolicyDocument.Statement[]

| select(.Effect=="Allow" and (.Action|tostring|contains("sts:AssumeRole")))

| ($r), (.Principal | tojson), ""' 1

[...]

aws-elasticbeanstalk-ec2-role

{"Service":"ec2.amazonaws.com"}

survivorBingo-role-jv27lw38

{"Service":"lambda.amazonaws.com"}

survivorBingo-role-jv27lw38

{"AWS":"arn:aws:iam::013628954028:root"} 2

1 Prints each IAM role followed by the principals allowed to assume it.

2 The role can be assumed by an external root account with AWS account ID 013628954028.
