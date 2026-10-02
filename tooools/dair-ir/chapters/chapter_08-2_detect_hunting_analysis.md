# Chapter 08-2: Detection: Threat Hunting, Anomaly Analysis & Detection Engineering

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

Human observations remain invaluable for detection, often identifying issues that automated systems miss.

In Prepare Activity , we examined security awareness training programs that develop this detection capability, allowing analysts to use employee observations as a source of incident detection.

Employees frequently serve as the first line of defense for threats, reporting suspicious emails, unusual system behavior, or social engineering attempts. Effective training and a culture that encourages reporting suspicious events help staff recognize indicators of compromise and understand reporting procedures.

Tying in pop culture references can enhance engagement, like the Dall-E-generated poster in Figure 56 encouraging employees to report suspicious activity.

Figure 56 | The Danger Things Dall-E Poster

When employees report suspected incidents, even false alarms, the organization gains detection coverage that technical systems cannot provide. Fostering a culture of vigilance encourages reporting, enhancing overall detection capabilities.

System administrators and help desk personnel often identify anomalies during routine operations: a server that keeps crashing, unexpected network traffic patterns, or unauthorized changes to systems they manage.

These observations, when properly escalated, can reveal ongoing compromises. Establishing clear escalation paths during preparation ensures these observations reach the incident response team promptly.

The way SOC analysts and help desk staff respond to employee reports matters as much as whether employees make them. A dismissive response, a slow acknowledgment, or a confusing intake process discourages future reporting and erodes the culture of vigilance that detection programs depend on.

Organizations should develop professional, supportive communication templates for acknowledging reports, providing status updates, and closing the loop when an investigation concludes. Even when a report turns out to be a false alarm, a brief response thanking the employee reinforces the behavior the organization wants to encourage.

Reinforcing the value of employee reports through timely, supportive communication helps build a culture where staff feel empowered to contribute to detection efforts.

Third-party notifications from customers, partners, or security researchers sometimes provide the first indication of a breach. While not ideal from a detection timeline perspective, these external reports remain an important source of detection. A published security.txt file (RFC 9116) provides a standard channel for researchers to reach the security team directly (see Establish External Reporting Channels ). Organizations should establish procedures for receiving and validating external notifications as part of preparation activities.

Cloud-Native Detection Sources

Cloud-native detection is a specialized subset of technical detection that warrants separate treatment due to the distinct characteristics of cloud environments: ephemeral workloads, API-driven infrastructure, shared responsibility models, and distributed architectures. The tools and techniques described in the Technical Detection Sources section (EDR, NDR, SIEM) still apply, but cloud environments introduce additional data sources and detection patterns that analysts should understand. Specialized detection solutions vary depending on the cloud deployment architecture: containerized, serverless, or hybrid environments.

The Incident Response for Cloud Systems  chapter explores cloud detection strategies in greater depth, including provider-specific tooling and cross-cloud correlation approaches.

Container and Kubernetes Detection

Container and Kubernetes detection employs multiple approaches to identify threats in containerized environments. Kernel-level monitoring using extended Berkeley Packet Filter (eBPF) enables systems to observe system calls from containerized workloads, identifying unexpected processes, file system modifications, or anomalous network connections. Container runtime socket monitoring provides an alternative detection method by observing the Docker or containerd API for container lifecycle events, image operations, and configuration changes that might indicate compromise or policy violations.

Logging systems, including Kubernetes audit events, provide visibility into API server activity, enabling detection of suspicious actions such as unauthorized pod creation, privilege escalation attempts, or access to sensitive secrets. Service mesh architectures offer additional network-level visibility between services, capturing traffic patterns that kernel-based or runtime monitoring might miss. For traffic entering or leaving the cluster, NDR tools at ingress points provide detection capabilities that complement mesh-level monitoring.

Container environments present unique detection challenges due to their ephemeral nature. When containers terminate, evidence of compromise may disappear before analysts can investigate. Organizations should configure centralized log collection and consider runtime detection tools that capture forensic artifacts in real time for high-sensitivity workloads.

Serverless and Microservices Detection

Detection in agentless environments, such as serverless functions and microservices, requires alternative approaches, as traditional endpoint agents cannot run in these execution environments.

Cloud provider logs, function telemetry, and event anomaly analysis serve as the primary sources of detection for serverless and corresponding microservices workloads. Analysts should watch for abnormal invocation patterns, unexpected outbound connection attempts, unusual access to secrets or environment variables, and deviations from baseline execution characteristics (such as timeouts, throttling, and unusual memory and CPU consumption). The ephemeral nature of these environments makes real-time detection

CHALLENGES IN DETECTION

Plainly said, the task for detection teams is challenging. Wading through large volumes of data, contending with encrypted traffic, facing adversaries actively evading detection, and addressing skills gaps within security teams all complicate effective threat identification. Understanding these challenges helps organizations develop strategies to work around limitations and improve detection capabilities over time.

Data Volume and Velocity

The volume and velocity of security data generated in modern environments can overwhelm analysis capabilities and delay threat identification. Larger networks can easily generate terabytes of log data daily from endpoints, network devices, cloud services, and applications, making comprehensive analysis difficult even with sophisticated tools and automation.

The quantity of data from multiple, disparate sources requires careful prioritization and filtering to ensure analysts focus on the most relevant signals.  Even with SIEM platforms and machine learning models, the volume of alerts can exceed analyst capacity, leading to alert fatigue and missed detections. Data retention costs add to this challenge, forcing organizations to make difficult decisions about which data to keep for historical analysis and which to discard after short periods.

An effective strategy for managing data volume is to focus on detection-driven collection: every event retained in a log should align with a specific detection use case. If no use case exists for a data source, there is limited value in retaining it. This principle shifts the default from collect everything and hope it proves useful to define what threats to detect and collect the data those detections require.

Organizations can implement detection-driven collection through several practical strategies:

• Start from use cases : Begin with specific attack detection scenarios and work backward to identify the required data sources, filtering or discarding sources that do not support a defined detection objective.

• Tiered data retention : Implement hot, warm, and cold storage tiers that keep recent high-fidelity data readily accessible while archiving older data to cost-effective storage for historical investigations.

• Filtering at the source : Wherever possible, remove known-good noise before ingestion by filtering routine events, such as successful authentication from service accounts or expected network traffic patterns.

• Intentional data disposal : Rather than degrading data quality through aggregation or sampling at ingestion, retain full-fidelity data for the time needed for useful detection and investigation analysis, then purge deliberately.

• Correlation-based alerting: Reduce alert volume by requiring multiple related signals before generating analyst-facing notifications, converting dozens of low-confidence events into single high-confidence alerts.

• Constant tuning: Regularly review and adjust detection rules, thresholds, and data sources to optimize signal-to-noise ratios as the environment and threats change. Retain test environments so the team can test changes to detection logic before deployment to production systems.

The goal is not to collect less data, but to collect the useful data and process it efficiently so analysts can focus on signals that matter.

DETECTION-DRIVEN COLLECTION: AZURE STORAGE LOGGING

Azure Blob Storage diagnostic logging is a great way to illustrate the detection-driven collection principle. A moderately active storage account can generate millions of StorageBlobLogs entries daily, with the vast majority representing routine read requests for public content. Ingesting all of this data into a Log Analytics workspace incurs storage costs and adds to the analyst burden without proportional detection value.

Instead, organizations can use Data Collection Rules (DCR) with ingest-time transformations to filter storage logs before they reach the workspace. Start by defining what threats storage logging should detect: unauthorized access attempts, data exfiltration, and suspicious deletion activity. Then configure a DCR transformation with a Kusto Query Language (KQL) query that evaluates each log entry against detection criteria during ingestion.

The following KQL transformation demonstrates this filtering approach, keeping only security-relevant events while discarding routine access patterns.

Listing 30 | DCR Transformation for Storage Log Filtering

source

| where StatusCode >= 400 1

or OperationType in ("DeleteBlob", "PutBlob",

"PutBlock", "CopyBlob") 2

or (CallerIpAddress !startswith "10."

and CallerIpAddress !startswith "192.168.") 3

| project TimeGenerated, OperationType, StatusCode,

CallerIpAddress, AccountName, ObjectKey, UserAgentHeader 4

1 Keep all failed requests (4xx and 5xx status codes).

2 Keep write and delete operations regardless of status.

3 Keep requests from IP addresses outside expected internal ranges.

4 Select only desirable columns to further reduce data ingestion volume.

This approach can reduce log volume substantially while preserving the events that actually support threat detection. The transformation runs at ingestion time within the DCR pipeline, so filtered events never consume workspace storage or processing resources.

Encrypted Traffic

Encryption limits network-based detection visibility into communications content. As more communications use TLS encryption for web traffic, encrypted DNS, and VPN connections, network monitoring tools increasingly rely on metadata analysis rather than deep packet inspection. While encryption provides important privacy and security benefits, it also creates areas of reduced visibility for threat hunting, where attackers can hide command-and-control communications or data exfiltration activity.

ENCRYPTED TRAFFIC DETECTION TECHNIQUES

Since payload inspection is limited with encrypted traffic, detection focuses on metadata and behavioral analysis: Flow-based analysis techniques, including Encrypted Traffic Analysis (ETA), use packet sizes, timing characteristics.

Certificate and handshake metadata inspection leverages certificate attributes, Server Name Indication (SNI) values, TLS versions, cipher suites, and handshake fingerprints. Services like Encrypted Client Hello (ECH, the successor to Encrypted Server Name Indication or ESNI) complicate detection, providing less opportunity to glean useful information from encrypted sessions. For these TLS connections, fingerprinting techniques such as JA4+ allow analysts to gain insight based on TLS handshake parameters, helping identify malicious clients even when traffic is encrypted. [5] For example, in the analysis shown in Listing 31 , we extract JA4 fingerprints from TLS Client Hello messages in a packet capture file using TShark, the text-based version of the Wireshark packet analyzer. TShark reveals the JA4 fingerprint t13i3110as_e8f1e7e78f70_1f22a2ca17c4 for the client session. Using a local JA4 database in JSON format, we query for this fingerprint using jq, revealing that the TLS connection corresponds to the AnyDesk remote desktop application, version 9.6.1.

Listing 31 | TLS JA4 Fingerprint Analysis

$ tshark -r netedge-20260105.pcapng -Y "tls.handshake.type == 1" -T fields -e

tls.handshake.ja4 | sort -u

t13i3110as_e8f1e7e78f70_1f22a2ca17c4

$ jq '.[] | select(.ja4_fingerprint == "t13i3110as_e8f1e7e78f70_1f22a2ca17c4")'

~/ja4db.json

{

"application": "AnyDesk",

"library": null, "device": null, "os": null,

"user_agent_string": "",

"certificate_authority": null, "verified": false,

"notes": "AnyDesk v9.6.1",

"ja4_fingerprint": "t13i3110as_e8f1e7e78f70_1f22a2ca17c4",

"ja4_fingerprint_string": "",

"ja4s_fingerprint": "",

"ja4h_fingerprint": null, "ja4x_fingerprint": null, "ja4t_fingerprint": null, "ja4ts_fingerprint": null, "ja4tscan_fingerprint": null

}

JA4 fingerprinting provides valuable context for encrypted traffic analysis, enabling analysts to identify applications and clients even when payloads are inaccessible and other privacy controls are applied to protect client and server details.

Behavioral context analysis provides additional insight for analysts when working with encrypted traffic.

This approach focuses on detecting unusual patterns indicative of EOIs in encrypted network activity.

Indicators include abnormal outbound data volumes, connections to unusual destinations, and new encrypted channels from systems that do not normally generate such traffic.

Organizations should focus network detection efforts on connection metadata, including destination addresses, connection timing and duration, data volume patterns, and certificate information that remains visible even when content is encrypted. TLS inspection capabilities for internal systems where policy permits can provide a valuable source of detection data for threat hunting and subsequent investigation.

Combined, these metadata and behavioral approaches allow organizations to maintain meaningful detection coverage even as encryption adoption continues to grow.

Adversary Evasion

Sophisticated attackers actively work to evade detection, treating security tools as obstacles to overcome rather than insurmountable barriers. Understanding common evasion techniques helps analysts recognize when attackers are attempting to hide their activities.

Attackers frequently target logging infrastructure to remove evidence of their activities. Clearing Windows Event Logs, disabling audit policies, or timestomping files to obscure activity timelines are common techniques. Analysts should monitor for gaps in log data and unexpected changes to logging configurations as potential indicators of compromise. The Scope chapter’s Anti-Forensic Techniques  section examines these further.

Rather than deploying custom malware that signature-based detection might catch, attackers increasingly use legitimate system tools for malicious purposes. PowerShell, Windows Management Instrumentation (WMI), PsExec, and other built-in utilities provide powerful capabilities that attackers exploit. These tools generate activity that blends with normal administrative operations, making behavioral detection essential.

Attackers who understand detection thresholds can operate just below them. Data exfiltration spread across many small transfers rather than one large transfer, authentication attempts spaced to avoid lockout policies, and lateral movement timed to coincide with normal business hours all exploit threshold-based detection limitations.

THE PRE-ATTACK LAB

Attackers with disciplined tradecraft test their techniques before deploying them against targets.

Sophisticated threat actors maintain lab environments that mirror common enterprise security stacks, testing malware and attack procedures against EDR products, SIEM detection rules, and network monitoring tools.

The 2022 Conti ransomware leaks revealed the extent of this practice. [6] Internal chat logs showed the group budgeted several thousand dollars monthly to purchase security and antivirus tools for continuous testing against their malware. The group also invested $60,000 to acquire a legitimate Cobalt Strike license through an intermediary company. In one chat, Conti manager Reshaev instructed a subordinate on operational security: “Install EDR on every computer (e.g., Sentinel, Cylance, CrowdStrike); set up a more complex storage system; protect LSAS dumps on all computers... detection strategies and continuous improvement essential.

As attackers adapt their techniques, detection teams cannot solely rely on endpoint signatures or static rules. Threat intelligence on emerging evasion techniques, regular updates to detection rules, and purple-team exercises that test detection coverage all contribute to maintaining effective detection capabilities.

Purple teaming is particularly valuable for reducing the gap between detection capability and attacker tradecraft. In a purple-team exercise, the red team demonstrates specific attack techniques while the blue team observes the resulting telemetry and develops or refines detections in near real time. This collaborative approach builds detection engineering skills that are difficult to develop from alerts alone. It also serves as a practical litmus test: if the SOC cannot track an internal red team operating from a known machine on the organization’s own network, detecting a sophisticated external adversary will be substantially more difficult.

Skills Gap

The skills gap in security operations means many organizations struggle to effectively use their detection tools and interpret the alerts they generate. The shortage of experienced analysts who can tune detection systems, investigate alerts, perform threat hunting, and develop new detection rules limits detection effectiveness across the industry.

Entry-level analysts often lack the deep technical knowledge needed to distinguish sophisticated attacks from benign anomalies, while experienced analysts are in high demand and difficult to retain. Organizations should invest in training programs that develop detection skills within their teams, leverage managed security service providers (MSSPs) to supplement internal capabilities, and implement knowledge management systems that capture detection expertise for future reference.

Automation and AI-assisted detection capabilities can help bridge some of the skills gap by providing analysts with context and recommendations (see Accelerating Incident Response with AI ). While valuable, these tools also require oversight from experienced personnel to avoid missing threats or creating excessive false positives.

DETECT ACTIVITY EXAMPLES

The following examples illustrate where detection is an important part of the incident response process.

The External Breach Hunter

Yoshihiro, a tier-1 SOC analyst on duty, opened an email on Tuesday morning with the subject line "Security Issue - Exposed Administrative Systems." The message had arrived through the security disclosure address published in the organization’s security.txt file, routing it directly to the security team rather than to a general support queue. The sender, Tom Liston, described exposed administrative portals and suspicious accounts on the organization’s patient management system.

Listing 32 | Excerpt from Liston’s Disclosure Email

From: Tom Liston <tliston@yourflyis0pen.com>

To: security@genusight.com

Subject: Genusight Medical Security Issue - Exposed Administrative Systems

Hello,

I identify compromised systems online as a hobby (yes, really). While scanning external attack surfaces this week I came across what looks like an active compromise in your patient management system.

The admin interface at hxxps://admin[.]genusight[.]com/login is publicly reachable. From what I can see, the system was protected by default or weak credentials that an attacker has already taken advantage of.

Two accounts on the system stand out: admin_backup (created 2026-03-02) svc_temp     (created 2026-03-05) Neither matches the adm_firstname.lastname convention I can see elsewhere in your environment.

Both have been authenticating from IP addresses in Eastern Europe over the past 45 days.

Authentication logs are attached.

An outside notification usually means internal detection missed something, and that’s worth a look too.

Glad to answer questions.

Regards,

Tom Liston

hxxps://yourflyis0pen[.]com/ Yoshihiro recognized the sender’s name. Tom Liston is a longtime handler at the SANS Internet Storm Center who has made a hobby of identifying compromised systems. However, recognition of the sender does not substitute for verification.

Yoshihiro approached the report with healthy skepticism. He had seen plenty of false alarms from well-meaning but mistaken researchers, and more than a fair share of social engineering attempts disguised as security notifications. Rather than relying on any single indicator, he worked through a structured verification process before deciding how to respond.

He first validated that the URLs in the email pointed to actual organizational infrastructure rather than lookalike domains that a social engineer might use to impersonate a real system. Next, he cross-referenced the suspicious account names against the (correctly-asserted) standard adm_firstname.lastname naming convention, confirming that admin_backup and svc_temp did indeed exist and did not match the policy-dictated provisioning pattern.

He then reviewed the authentication logs attached to the report, geolocating the source IP addresses and confirming that the organization had no business presence or remote workers in the regions shown. Finally, he assessed the overall quality of the report: specific technical detail, reproducible evidence, and a clear detection event will transition to the verify and triage phase, where the team will validate the specific claims and determine the appropriate response. The combination of a published disclosure channel, structured triage, and multi-factor validation transformed a message that might otherwise have languished in a help desk queue into actionable threat intelligence.

The SIEM Wizard

Active threat hunting enables analysts to proactively identify threats that automated alerting systems might miss, particularly when searching for suspicious patterns rather than known malicious indicators. Mature detection teams operate threat hunting as a documented program rather than an ad hoc effort, tracking hunt hypotheses, target data sources, cadence, and last-run dates in a table that supports both coverage reviews and regulator inquiries. See Establish a Threat Hunting Program  in the Prepare chapter for guidance on designing and documenting this program.

Lucía, a threat hunter on the security operations center (SOC) team, ran beaconing detection as one of the recurring hunts in her team’s program. Beaconing behavior in outbound traffic is a common indicator of command and control communication, where compromised systems regularly check in with attacker infrastructure. Beaconing is particularly suspicious because legitimate applications rarely communicate with external servers at perfectly consistent intervals, while malware often implements regular callback schedules to receive commands or exfiltrate data.

Lucía opened Kibana and crafted an Elasticsearch aggregation query to identify URLs with consistent access patterns over the past seven days, shown in Listing 33. Her query grouped all proxy requests by destination URL and analyzed the distribution of requests over time, looking for patterns that suggested automated, scheduled communication rather than human-driven web browsing.

Listing 33 | Elasticsearch Query for Beaconing Detection

{

"size": 0, 1

"query": {

"range": {

"@timestamp": {

"gte": "now-7d", 2

"lte": "now"

}

}

},

"aggs": {

"by_url": {

"terms": {

"field": "url.keyword", 3 "size": 500

},

"aggs": {

"over_time": {

"auto_date_histogram": {

"field": "@timestamp", 4 "buckets": 50

}

},

"request_count": {

"value_count": { 5

"field": "@timestamp"

}

}

}

}

}

}

1 Don’t return individual documents, only aggregation results.

2 Search only the past seven days of proxy log data.

3 Group all requests by destination URL.

4 Create a histogram showing when requests occurred for each URL.

5 Count the total number of requests for each URL.

The query returned hundreds of URLs with varying access patterns. Lucía reviewed the results, examining the time distribution histograms for each URL. Most showed the irregular patterns typical of human access: bursts of activity during business hours, gaps during lunch, quiet periods overnight. Others exhibited consistent patterns from legitimate automated systems like software update checkers and monitoring tools, which Lucía recognized from previous hunting sessions.

One URL immediately caught her attention: api.cloudserv-cdn.com showed exactly 2,016 requests over the past seven days, with the histogram displaying perfectly spaced intervals. Lucía calculated the timing: a week of requests at that volume worked out to exactly five minutes between each request. This precision in timing was unusual, and alarming.

Lucía dug deeper into this suspicious URL, crafting a follow-up query to identify which client systems were accessing it and examining the specific timestamps. She found that all requests originated from a single workstation in the finance department, and the timestamps confirmed the pattern: requests occurred at exactly :05, :10, and every five minutes thereafter with no variation in timing. The domain itself raised additional concerns when she checked threat intelligence feeds. It was registered only three weeks ago through a registrar frequently abused by threat actors for cheap, rapidly provisioned domains, and the hosting provider was associated with malicious infrastructure.

Lucía documented her findings, noting the suspicious beaconing pattern, the recently registered domain, the consistent five-minute interval, and the affected workstation details. She escalated this detection event to the incident response team for verification and triage, where they would investigate whether the workstation was genuinely compromised or if there was a legitimate explanation for this highly regular communication pattern.

DETECT: STEP-BY-STEP
