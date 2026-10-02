# Chapter 11: Scope Activity: Blast Radius & Pivot Analysis

First, organizational resources should be managed effectively throughout the incident response process, including multiple iterations of the response actions loop.  Teams may experience fatigue across multiple iterations, requiring careful rotation and rest periods to maintain effectiveness. Budget constraints may limit the time invested in the response effort, forcing teams to prioritize the most critical scoping and remediation activities. Tool limitations may constrain iteration speed, particularly when forensic analysis or evidence collection requires time-consuming manual processes. Decision makers should balance the need for a thorough response with resource realities, avoiding burnout while ensuring sufficient effort to resolve the incident.

Second, documentation requirements create a significant burden across multiple iterations. Each iteration generates substantial documentation that should be maintained coherently across the entire incident lifecycle. Legal and compliance requirements add complexity, particularly when regulatory frameworks mandate specific documentation standards or retention periods. Knowledge transfer between shifts requires careful coordination to ensure that incoming team members understand the current state and can continue response activities without duplication or gaps. Decision makers should be careful not to require excessive documentation that detracts from active response efforts, balancing the need for thorough records with the realities of incident dynamics.

Third, stakeholder patience often wanes as iterations continue. Leadership may not understand why multiple iterations are necessary, viewing repeated cycles as evidence of poor planning or execution rather than as the natural progression of incident understanding. Business units may pressure for faster resolution, prioritizing return to normal operations over thorough remediation. Effective communication from the incident response team helps manage these expectations by explaining the value of iterative learning, demonstrating progress through each cycle, and acknowledging the business need for resolution. The response actions loop transforms incident response from a linear checklist into a dynamic learning process. By embracing iteration rather than viewing the need for comprehensive response efforts as failure, organizations can more thoroughly address sophisticated attacks that would overwhelm traditional sequential approaches. Success lies not in executing the loop perfectly once, but in cycling through it as many times as necessary to achieve true incident resolution. This iterative approach, while potentially requiring more time initially, ultimately delivers more complete remediation and valuable organizational learning that prevents future incidents.

RESPONSE ACTIONS LOOP: STEP-BY-STEP

The following steps provide a condensed reference for response actions loop activities. Each step corresponds to topics covered earlier in this chapter, organized for use when managing the iterative cycle of scoping, containment, eradication, and recovery. The chapters that follow examine each activity in greater depth.

The loop is inherently iterative: a single pass rarely produces a complete response because initial understanding is partial, new insights surface during eradication, and evidence analysis reveals previously unknown attack vectors. Expect to cycle through the loop multiple times, with each activity expanding in sophistication as understanding improves.

Step 1. Run the Loop Expecting Each Activity to Deepen Across Iterations

Representative principles include:

• The four constituent activities (scope, contain, eradicate, recover) are owned by their own chapter step-by-step sections; this guide focuses on what is unique to running them as a loop. Refer to the individual scope, contain, eradicate, and recover step-by-step guides for the per-activity work.

• Sequence depends on incident state, not on a fixed order: scope is usually the first activity in any iteration but contain may precede or run in parallel when an active threat requires it.

• Each subsequent iteration should produce more sophisticated and complete results than the previous one as understanding accumulates.

Step 2. Identify Iteration Triggers Requiring Additional Response Cycles

Representative iteration triggers include:

• New indicators of compromise were discovered during analysis.

• Evidence of incomplete eradication or reinfection.

• Revelations from forensic analysis that require expanded scoping.

• Changing business priorities or regulatory requirements.

Step 3. Maintain Cross-Phase Documentation and Communication

The loop owns the cross-phase communication cadence; the per-activity documentation steps in scope, contain, eradicate, and recover feed into this cadence. Representative activities include:

• Record decision documentation for each activity (what, when, who, rationale).

• Track the impact assessment of response actions on business processes and system availability.

• Provide stakeholder communication tailored to different audiences (executive summaries, technical briefings, user notifications).

• Maintain documentation continuity across iterations, linking related findings and actions.

• Adjust communication frequency and detail based on incident severity and stakeholder needs.

Step 4. Build Cumulative Understanding Across Iterations

Representative activities include:

• Document findings from each iteration to support the overall incident narrative.

• Link new discoveries to prior iterations for continuity.

• Ensure knowledge transfer between shifts through coordinated documentation.

Step 5. Monitor for Technical Indicators of Resolution

Representative indicators include:

• No new IOCs discovered during scoping activities.

• Monitoring shows no signs of attacker activity.

• Eradication verification confirms threat removal.

• Systems are operating normally after recovery.

Step 6. Assess Business Indicators for Loop Conclusion

Representative indicators include:

• Operational objectives are met.

• Acceptable risk level has been achieved.

• Cost-benefit analysis supports concluding the active response.

• Resource constraints require prioritization of decisions.

Step 7. Engage Decision-Makers for Loop Exit Determination

Representative activities include:

• Present technical and business indicators to leadership.

• Discuss risk acceptance for residual uncertainties.

• Confirm regulatory requirements for incident closure are met.

• Establish ongoing monitoring plans for continued vigilance.

Step 8. Address Practical Considerations Throughout Iterations

Representative considerations include:

• Manage team fatigue through rotation and rest periods to maintain effectiveness across multiple cycles.

• Account for budget constraints and tool limitations that may affect iteration speed, particularly time-consuming forensic analysis or evidence collection.

• Balance documentation requirements with active response efforts, avoiding excessive documentation that detracts from active response.

• Manage stakeholder patience as iterations continue. Leadership may view repeated cycles as poor execution rather than as the natural progression of incident understanding.

• Communicate progress to stakeholders to manage expectations, explain the value of iterative learning, and address business pressure for faster resolution.

11 Scope Activity

In the DAIR model, we introduce another activity not specifically called out in other popular incident response models: scope. This step bridges the gap between initial incident verification and effective containment by determining the extent of the compromise across the organization. Without proper scoping, incident response teams risk addressing only the visible symptoms while leaving significant portions of the attack undetected and unaddressed.

Figure 69 | Scope Activity Waypoint

THE PURPOSE OF SCOPING

Scoping transforms the team’s understanding from "we have an incident" to "we know some of the breadth and depth of this incident." This activity takes the indicators of compromise (IOCs) identified during detection and verification, then systematically searches for them across the environment to understand the true extent of the breach.

Scoping is essential to effective incident response. Organizations that fail to properly scope incidents often experience repeated compromises, eradicating malware from known-infected systems while leaving other compromised systems untouched. The NovaFlow incident  exemplifies this failure: Jordan identified a suspicious process (ssupd) on the development system, but failed to search for the same IOCs elsewhere in the environment, missing the broader compromise.

Scoping answers fundamental questions that shape the entire response effort:

• Is this an isolated incident affecting a single system, or has the attacker established a widespread presence?

• Which systems have been compromised, and which remain unaffected?

• What is the timeline of the attack, and how long has the attacker maintained access?

• What data or resources has the attacker accessed or exfiltrated?

• Are there multiple attack vectors or persistence mechanisms deployed across different systems?

Scoping is an essential step in the incident response process, notably absent from traditional models. Organizations that apply effective scoping techniques gain a comprehensive understanding of the incident, enabling targeted containment, eradication, and recovery efforts that address the root cause rather than just the symptoms.

INDICATORS OF COMPROMISE IN SCOPING

Effective scoping relies on identifying and leveraging indicators of compromise: the artifacts that reveal malicious activity or attacker presence. IOCs come in many forms, and understanding their variety helps responders cast a wider net during scoping activities.

In this section, we’ll examine two categories of IOCs that inform scoping: technical indicators that provide concrete, searchable artifacts, and behavioral indicators that reveal attacker activity through patterns rather than discrete artifacts.

Technical IOCs

Technical indicators provide concrete, searchable artifacts that can be systematically hunted across the environment:

File-based Indicators: These indicators include malware hashes, suspicious filenames, or specific file paths used by attackers. A single malicious executable discovered on one system should trigger searches across all systems for the same file hash, similar filenames, or files in unusual locations. Network Indicators: These indicators are broad but particularly valuable, allowing organizations to leverage investigative insight to quickly assess a large number of systems.  Network indicators include IP addresses, domain names, URLs, network signatures, and other network anomalies (often characterized by Network Detection and Response (NDR) platforms), including unusual network activity patterns.  For example, if an investigation reveals anomalous network activity attributed to an attacker command-and-control (C2) server, scoping should identify all systems that have communicated with that attacker infrastructure. This level of analysis may reveal additional compromised systems not yet exhibiting obvious symptoms. Process and Service Indicators : These indicators include suspicious process names, service names, Attackers often use consistent naming patterns across compromised systems, making these valuable for scoping. Randomly-named processes or services can also be valuable indicators, since they deviate from normal system behavior.

Registry and Configuration Indicators : These indicators involve specific keys, values, or configuration changes within the system registry.  PowerShell scripts stored in registry values, WMI event subscriptions, or modified system settings can serve as IOCs for broader searches. Similarly, non-Windows systems may have comparable indicators revealed in configuration files (e.g., ASCII-based or encoded data, including macOS property list files).

Account-based Indicators: These indicators include unauthorized user accounts, suspicious account usage patterns, or privilege escalations. An attacker-created account on one system warrants immediate investigation for similar accounts throughout the organization.

Behavioral IOCs

Beyond static technical indicators, behavioral patterns can reveal attacker activity that may not be captured by traditional IOCs. Behavioral indicators often require more sophisticated analysis but can uncover widespread compromise that static indicators miss.

Temporal Patterns: Temporal patterns observed in logging data, SIEM trend analysis, or aggregate network investigations may indicate coordinated activity across multiple systems. Simultaneous logons, synchronized file modifications, or regular beacon intervals can indicate widespread compromise even when individual events appear benign. Attackers often operate on consistent schedules, creating predictable patterns that become visible when analyzed across the environment. Data Movement Patterns : These patterns show unusual data flows between systems or to external destinations. Large data transfers, especially during off-hours, may indicate exfiltration activities. Systems that do not typically communicate but are suddenly transferring large amounts of data warrant investigation as potential indicators of data staging or exfiltration. Lateral Movement Indicators : These indicators include authentication, remote access, or service usage patterns that indicate an attacker moving between systems.  Pass-the-hash attacks, remote desktop sessions, or WMI usage for remote execution leave distinctive patterns that differ from normal administrative activity. Multiple authentication attempts across many systems in a short timeframe often reveal automated lateral movement tools.

SCOPING METHODOLOGIES

To be effective in scoping, analysts can apply several systematic approaches to ensure comprehensive coverage while managing resource constraints. The following methodologies help analysts scope incidents effectively.

In this section, we’ll work through two complementary methodologies: enterprise-wide hunting to search for IOCs across all available data sources, and progressive scoping to prioritize investigation in phases when resources cannot cover the entire environment at once.

Enterprise-Wide Hunting

After identifying an IOC, analysts should search for matching evidence across the organization. This analysis should start with centralized log analysis tools, including SIEM platforms, log aggregation systems, or other data resources to quickly search collected logging data across the environment. Starting with log analysis typically provides rapid initial results, though it requires that the organization already have comprehensive log collection in place.

Endpoint Detection and Response (EDR) platforms are also particularly valuable for searching and identifying IOCs across all managed endpoints. Modern EDR tools enable analysts to run complex queries that can find files, processes, network connections, and registry modifications across thousands of systems. When EDR systems are not available, analysts should consider inventory management tools, active scanning tools to probe systems for IOCs, network scans to identify specific services (such as open ports), authenticated scans for file presence, or specialized compromise assessment tools including custom PowerShell or shell scripts.

For comprehensive scoping, analysts should use threat-hunting platforms that combine multiple data sources into a single interface. Platforms that integrate endpoint, network, and logging data provide the broadest view of potential compromise indicators. By combining these data sources in a single platform, analysts can use overlapping analysis coverage to reduce the chance of missing compromised systems.

Progressive Scoping

Given resource limitations, scoping often proceeds in phases rather than attempting to investigate the entire environment simultaneously.

Critical Asset Prioritization: This approach focuses initial scoping on high-value systems, including domain controllers, file servers, databases, and systems containing sensitive data. These systems warrant immediate attention regardless of initial IOC location.  Sometimes referred to as pivoting in an investigation, critical asset prioritization ensures that the most important organizational assets are quickly assessed and protected.

Lateral Expansion : This phase extends scoping to systems directly connected to known-compromised hosts, including those on the same network segment, those with recent authentication from compromised accounts, and those sharing administrative credentials. Lateral expansion follows the likely paths an attacker would take to move through the environment.

Environmental Sweep : This phase eventually extends to all systems in the environment, ensuring no compromised systems remain undiscovered. Environmental sweeps may occur over days or weeks for large organizations.

TIMELINE RECONSTRUCTION

An important output of scoping is understanding the attack timeline, including when different systems were compromised and how the attack progressed through the environment. Building this timeline helps analysts understand the scope of the incident and provides critical context for containment and eradication decisions.

Timeline reconstruction is an iterative activity. Each pass through the response actions loop surfaces new artifacts that extend the timeline earlier or reveal additional attacker activity.

Work toward identifying the initial compromise, the patient zero  system (the first system compromised), and the initial compromise vector, recognizing that early iterations of the analysis may conclude without any of these being confirmed. This analysis requires careful review of logs, file timestamps, and process creation times across multiple systems to find the earliest evidence of attacker activity. Look for the oldest artifacts related to the incident, including the first malicious file execution, initial network connection to attacker infrastructure, or earliest authentication anomaly.

Next, map the attacker’s lateral movement through the network to trace their path from initial compromise to broader access. Authentication logs, remote access records, and file movement patterns reveal how the attacker expanded their presence across the environment. Analysts should pay particular attention to privilege escalation events and authentication to high-value systems such as domain controllers or database servers.

Identify when attackers deploy persistence mechanisms to understand the attacker’s evolution from initial access to established presence. This timeline helps responders understand which persistence mechanisms are the oldest and potentially most deeply embedded in the environment. Common persistence mechanisms include scheduled tasks, registry modifications, service installations, and account creations, each leaving timestamped artifacts that can be analyzed.

Finally, determine when sensitive data was accessed or removed by reviewing file access logs, database query logs, and network traffic patterns. This timeline is critical for breach notifications and understanding the full impact of the incident. Many regulatory frameworks require organizations to report the timeline of data access or exfiltration, making this analysis essential for compliance. The timeline example shown in Figure 70  illustrates how multiple first contact  events across different systems can reveal the attacker’s progression through the environment over time. In this illustration, multiple systems exhibit initial compromise events and the use of different C2 infrastructure over time (denoted as LOLC for the attacker lolcats[dot]org domain, and W1GA for the attacker www1-google-analytics[dot]com domain). This timeline was reconstructed from network activity logs into a simple CSV file and visualized using a short Python script to plot the events over time.

Figure 70 | Sample Network Activity Timeline

Listing 41 | Network Activity Data Summary CSV
"2025-03-19 16:46:11",172.16.42.103→W1GA
"2025-03-19 14:46:22",172.16.42.103→LOLC
"2025-03-19 16:48:39",172.16.42.105→W1GA
"2025-03-19 15:16:13",172.16.42.105→LOLC
"2025-03-19 16:50:23",172.16.42.107→W1GA
"2025-03-19 16:55:19",172.16.42.108→W1GA
"2025-03-19 16:57:04",172.16.42.109→W1GA
"2025-03-19 16:10:48",172.16.42.2→W1GA
"2025-03-19 16:38:15",172.16.42.3→W1GA
Timeline reconstruction often reveals that incidents have been ongoing for weeks or months before
detection. This discovery underscores the importance of comprehensive scoping rather than focusing only
on recently identified symptoms.

Understanding the full timeline helps identify any systems that have been compromised early in the attack but haven’t yet been discovered through IOC searches.

SCOPING CHALLENGES

Comprehensive scoping across an entire organization introduces significant challenges. Understanding these challenges helps incident responders develop strategies to work around limitations and improve scoping effectiveness over time.

In this section, we’ll address three obstacles: visibility gaps across the environment, anti-forensic techniques attackers use to hide their activity, and the scale and complexity of large environments.

Visibility Gaps

Organizations rarely have complete visibility across their entire environment, creating blind spots that attackers can exploit.  Unmanaged systems including Bring Your Own Device (BYOD) endpoints, shadow IT infrastructure, and legacy systems may harbor compromise and escape standard scoping tools. These systems often exist outside the organization’s asset inventory, making them difficult to assess during incident response. Even when analysts know these systems exist, they may lack the necessary access credentials or management tools to search for IOCs.

Limited logging on certain systems or classes of systems presents another visibility challenge.  This is particularly true for legacy systems, embedded devices, and industrial control system (ICS) platforms that lack robust logging capabilities.  Network devices, printers, and Internet of Things (IoT) devices often internal diagnostics including connection tables and error counters accessible through its web interface, it does not generate syslog events, forward logs to SIEM platforms, or provide the historical audit trails that incident responders rely on for timeline reconstruction. For many organizations, network flow data becomes the primary source of evidence for determining whether industrial control systems like the S7-1200 have been accessed or manipulated during an incident, making comprehensive network visibility essential in ICS environments.

Figure 71 | Siemens S7-1200 [1]

While network flow data is valuable, it has its own limitations. Most enterprise switches export flow data using packet sampling by default, often at ratios of 1:1000 or higher. Sampling at these rates can miss short-lived connections or the low-volume C2 beaconing characteristic of targeted attacks. Analysts should verify the configured sampling rate for network flow capture devices and, where feasible, request unsampled export on paths carrying high-value traffic.

OT environments face a more severe constraint: many industrial switches lack the processing capacity to generate flow data at all, and those that do often produce sampled output that misses the low-volume protocol traffic typical of ICS. Purpose-built OT monitoring tools provide passive protocol-aware visibility without imposing load on the control network, parsing industrial protocols such as Modbus, DNP3, and S7comm to extract asset inventories and communication baselines that general-purpose flow tools cannot produce. Commercial platforms such as Dragos provide turnkey capabilities for threat analysis, and open-source alternatives include Malcolm from Idaho National Laboratory and Zeek extended with the ICS Network Protocol Parsers (ICSNPP) package. See Chapter 19 for guidance on scoping in OT environments. Cloud and hybrid environments require different scoping approaches than traditional on-premises infrastructure. Serverless functions, containers, and cloud-native services may not be visible to traditional scoping tools designed for Windows endpoints. Organizations should ensure their scoping strategies include cloud-specific tools and techniques, such as cloud provider APIs, container runtime security tools, and cloud-native logging services. The ephemeral nature of many cloud resources means that evidence can disappear when resources are deallocated, making timely scoping critical.

Anti-Forensic Techniques

Sophisticated attackers actively work to impede scoping efforts by employing anti-forensic techniques to hide their presence and confuse investigators. Recognizing these techniques helps responders develop counter-strategies and avoid drawing incorrect conclusions from manipulated evidence. Log deletion or modification removes evidence of attacker activity, creating gaps in timeline reconstruction and making it difficult to identify all compromised systems. Attackers may delete specific log entries related to their activities or clear entire log files to cover their tracks. To counter this, analysts should look for evidence of log manipulation itself, including gaps in log timestamps, unusual log file sizes, or security events indicating log clearing. An example of a Windows Event Log indicating log deletion is shown in Figure 72.

Figure 72 | Windows Event Log Indicating Log Deletion

Collecting logs from multiple sources can also help reconstruct attacker activity even when some logs have been deleted. When multiple log sources are not available, analysts can sometimes infer deleted events by correlating with network logs or other system events. For example, on Windows systems, each logging event is assigned a sequentially incrementing event record ID (viewable in Event Viewer by clicking Details | XML View). Gaps in event ID sequences may indicate deleted log entries.

Figure 73 | Windows Event Viewer Event Record ID Field

Sophisticated attackers may also manipulate logs without deleting them. Log replay and flooding techniques pollute the log stream to obscure malicious activity, for example, by replaying legitimate events to make an attacker session blend with normal traffic, flooding the SIEM to cause event drops, or spacing detectable events below alert thresholds. Countering these techniques requires baseline understanding of expected log volumes, alerting on sudden surges or unusual quiet periods, and correlation across independent log sources that are unlikely to be manipulated in a coordinated way. Timestomping modifies file timestamps to hide the timing of malware installations or blend malicious files with legitimate system files. Attackers use timestomping to make recently installed malware appear as though it has been present since system installation.  When analyzing systems where timestomping is suspected, analysts should examine alternative timestamp sources including filesystem metadata ($MFT entries on Windows), backup system records, or network detection timestamps for file downloads. Encryption and obfuscation hide indicators from automated scanning tools, requiring manual analysis to identify compromise. Attackers may encrypt malware payloads, obfuscate PowerShell commands, or use packing techniques to avoid signature-based detection. Network traffic encryption can similarly hide C2 communications from network-based scoping tools. Behavioral analysis and memory forensics often prove more effective than signature matching when dealing with encrypted or obfuscated threats. Living-off-the-land techniques use legitimate system tools like PowerShell, Windows Management Instrumentation (WMI) utilities including wmic.exe and mofcomp.exe, and .NET Framework tools ( csc.exe, installutil.exe, and others), making it difficult to distinguish malicious activity from normal administrative operations. Attackers choose these techniques specifically to blend in with normal activity and avoid detection during scoping. Analyzing command-line arguments, execution context, and temporal patterns helps identify malicious use of legitimate tools. Establishing baselines of normal administrative activity provides a reference point for identifying anomalies, and behavioral detections augmented with machine learning can surface deviations that static rules miss.

Scale and Complexity

Large, complex environments present practical scoping challenges that can overwhelm even well-resourced incident response teams. Organizations should develop strategies to manage these challenges while maintaining comprehensive scoping.

The sheer volume of data generated during scoping can overwhelm analysis capabilities and delay incident response. Searching for IOCs across thousands of systems generates significant volumes of log data, file listings, and process information requiring analysis. Analysts should prioritize scoping efforts using the progressive scoping methodology described earlier, focusing first on high-value targets and known-compromised systems before expanding to the broader environment. Automation tools can help process large data volumes, though analysts should still validate automated findings to avoid missing sophisticated attacks.

False positives from legitimate software or normal activity that matches IOC patterns complicate scoping and consume investigative resources. Each potential match requires investigation to determine whether it represents a genuine compromise or benign activity. For example, searching for a malware filename might match legitimate software that happens to use a similar name, or network IOC searches might identify VPN connections that look suspicious but are actually legitimate. Documenting known false positive sources helps streamline future investigations and reduce analysis time.

Dynamic environments where systems are constantly created, modified, or destroyed present unique scoping challenges, particularly in cloud environments using auto-scaling or containerized workloads. Compromised systems may be automatically destroyed before analysts can examine them, and new systems may be created with embedded compromise from tainted images. In these environments, analysts should focus scoping efforts on examining system images, container registries, and infrastructure-as-code templates in addition to running systems. Organizations should implement logging solutions that capture system state even for short-lived resources, ensuring evidence persists after system destruction. Cloud scoping often requires querying audit logs to trace compromised identities and unauthorized resource activity. Each major cloud provider offers equivalent audit log capabilities with different query syntax. Table 14 provides a quick reference for translating common audit log queries across providers.

Table 14 | Cloud Audit Log Quick Reference
Query audit logs
AWS aws cloudtrail lookup-events
Azure az monitor activity-log list
GCP gcloud logging read
Filter by resource
AWS aws cloudtrail lookup-events --lookup-attributes
AttributeKey=ResourceName,AttributeValue=<name>
Azure az monitor activity-log list --resource-id <resource-id>
GCP gcloud logging read 'resource.type="<type>"'
AWS aws cloudtrail lookup-events --lookup-attributes
AttributeKey=Username,AttributeValue=<user>
Azure az monitor activity-log list --caller <object-id>

GCP gcloud logging read 'protoPayload.authenticationInfo.principalEmail="<email>"' Filter by time range AWS aws cloudtrail lookup-events --start-time <time> --end-time <time> Azure az monitor activity-log list --start-time <time> --end-time <time> GCP gcloud logging read 'timestamp>="<time>"' These commands provide a starting point for cross-platform audit log analysis during scoping investigations.

INTEGRATION WITH RESPONSE ACTIVITIES

This section concludes with a discussion of how scoping integrates with other incident response activities including containment, eradication, and recovery.

Scoping doesn’t occur in isolation but integrates closely with other incident response activities. The information gathered during scoping feeds directly into containment, eradication, and recovery decisions, while new discoveries during those activities often trigger additional scoping efforts. In some organizations, the scoping step may directly contribute to containment, then to eradication and recovery, but this is not a requirement. Particularly for later iterations of the response actions loop, scoping may occur in parallel with containment, eradication, and recovery activities. Analysts may also see value in transitioning from scoping to recovery directly without additional containment or eradication steps, for example when no new compromised systems are discovered but additional context warrants updates to the root cause analysis for the incident.

The scope activity transforms incident response from reactive firefighting to strategic remediation. By systematically identifying all affected systems and understanding the full extent of compromise, organizations can mount effective responses that truly eliminate threats rather than merely addressing symptoms. This comprehensive understanding proves essential for breaking the cycle of incomplete remediation and reinfection that affects organizations with immature incident response capabilities.

SCOPE ACTIVITY EXAMPLES

The following examples illustrate where scoping is an important part of the incident response process.

The LinkedIn Attachment

Renee is an incident response analyst supporting a mid-sized SaaS company. A product manager reported suspicious activity on her workstation after opening a document received through a LinkedIn direct message from someone claiming to be an industry analyst. The document promised a leaked competitive analysis of the company’s closest rival. Renee was asked to analyze the document and determine whether it contained any malicious content.

Renee performed initial analysis of the document using a dedicated workstation isolated from the corporate network, beginning with file size, hash, and file type identification using the Fileutils file command, as shown in Listing 42.

Listing 42 | Unsolicited Document File Command Output
$ ls -l malware -rw-r—r--@ 1 renee staff   1.6M Oct 21 16:29 malware
$ sha256sum malware
9484272e48f908e816a68f295a105d885b9d0ba52d8255d95c9bf237f71eae6b  malware
$ file malware
malware: PDF document, version 1.4

The document appeared to be a standard PDF file, but Renee wasn’t yet ready to open it in a PDF viewer. She extracted summary information about the PDF structure using Pdfinfo, as shown in Listing 43.

Listing 43 | Unsolicited Document Pdfinfo Command Output
$ pdfid.py malware
PDFiD 0.2.10 malware
PDF Header: %PDF-1.4
obj                   27
endobj                27
stream                 5
endstream              5
xref                   4
trailer                4
startxref              4
/Page                  1
/Encrypt               0
/ObjStm                0
/JS                    0
/JavaScript            0
/AA                    0
/OpenAction            0
/AcroForm              0
/JBIG2Decode           0
/RichMedia             0
/Launch                0
/EmbeddedFile          0
/XFA                   0
/URI                   6
/Colors > 2^24         0

Listing 44 | Unsolicited Document Pdf-parser Command Output
$ pdf-parser.py -s /URI malware
obj 9 0
Type: /Annot
Referencing:
<<
/Type /Annot
/Subtype /Link
/Rect [51.7500000  191.750000  542.250000  827.750000 ]
/Border [0 0 0]
/A
<<
/Type /Action
/S /URI
/URI (hxxp://host███████private.duckdns[.]org/eubp/example.zip) 1
>>
>>
obj 19 0
Type: /Action
Referencing:
<<
/URI (hxxps://stc████████lik[.]com/Update/UpdatePDF.exe) 2
/S /URI
/Type /Action
>>
obj 25 0
Type: /Action
Referencing:
<<
/URI (hxxps://stc████████lik[.]com/Update/UpdatePDF.zip) 3
/S /URI
/Type /Action
>>
1 Suspicious URL at Dynamic DNS provider DuckDNS serving example.zip.
2 Suspicious URL hosting the UpdatePDF.exe file.
3 Suspicious URL hosting the UpdatePDF.zip file.

Renee noted three suspicious URLs embedded in the PDF across six references. The URLs pointed to a DuckDNS dynamic DNS domain and a suspicious domain hosting two executable files. With this new insight, Renee noted several elements to use for subsequent scoping activities:

• File-based indicators: the hash of the PDF file.

• Network indicators: the three embedded URLs.

• File-based indicators: the filenames of the referenced files (UpdatePDF.exe and UpdatePDF.zip).

Renee documented the scoping indicators she had identified so far and continued her analysis of the PDF document while searching for additional impacted systems across the organization.

The Cloud Storage Exfiltration

Priya is a cloud security analyst for a financial services company that uses Azure for both production applications and data storage.  She received an automated alert from Microsoft Defender for Cloud indicating a new Blob Storage container named backup-data-archive-2025 was created in the stcorpdata01 storage account three days ago. She double-checked Teams, but there was no associated change order for the new container. The container name followed common internal naming conventions, but the creation timestamp showed it was created at 11:47 PM on a Saturday, well outside normal business hours. Priya began her investigation to determine if this was an IOC.

Priya started by examining the contents of the suspicious container using the Azure CLI, as shown in Listing 45.

Listing 45 | Cloud Exfiltration Container Contents
$ az storage blob list --container-name backup-data-archive-2025 --account-name stcorpdata01 --query "[].{Name:name, Size:properties.contentLength, Modified:properties.lastModified}" --output table

Name                                                Size       Modified

--------------------------------------------------  ---------  -------------------------------- HR/Payroll_2025_Q1.xlsx                             49492787   2025-10-19T23:52:14+00:00 Finance/Budget_Projections_2026.xlsx                134637158  2025-10-19T23:52:18+00:00 CustomerData/client_list_full.csv                   935418906  2025-10-19T23:52:23+00:00 Engineering/Product_Roadmap_Confidential.pptx       67947725   2025-10-19T23:52:31+00:00 Legal/Contracts_Archive_2024.zip                    225770509  2025-10-19T23:52:38+00:00 HR/Employee_Records_Complete.xlsx                   103494067  2025-10-19T23:52:45+00:00 CustomerData/transaction_history_2024.csv           462638387  2025-10-19T23:52:52+00:00 Finance/Audit_Reports_2024.pdf                      164481254  2025-10-19T23:53:01+00:00 Engineering/Source_Code_Archive.zip                 77070336   2025-10-19T23:53:08+00:00 CustomerData/customer_pii_database.csv              340331930  2025-10-19T23:53:15+00:00 [...] The container held 47 blobs totaling approximately 8.2 GiB. The filenames indicated highly sensitive internal data, including payroll information, customer data, intellectual property, and legal contracts. The directory structure (HR/, Finance/, CustomerData/, Engineering/, Legal/) matched the organization’s internal file server layout exactly. All blobs showed upload timestamps within a twenty-minute window on the same Saturday night the container was created.

Next, Priya investigated who created the container by querying the Azure Activity Log, as shown in Listing 46.

Listing 46 | Cloud Exfiltration Container Creation Event
$ az monitor activity-log list --offset 7d --query "[?contains(resourceId, 'backup-data-archive-2025')] | [0]"
{
"authorization": {
"action": "Microsoft.Storage/storageAccounts/blobServices/containers/write",
"scope": "/subscriptions/e7b3c1d9-a842-4f56-b6d1-8a3e5f902c4d/resourceGroups/rg-production-eastus2/providers/Microsoft.Storage/storageAccounts/stcorpdata01/blobServices/default/containers /backup-data-archive-2025"
},
"caller": "c7e2a091-4b38-4d65-9f12-b8a3e6d50c71", 1
"claims": {
"appid": "e4f2d1b8-6a93-4c57-8e1f-9d0b2a3c5e7f",
"hxxp://schemas[.]microsoft[.]com/identity/claims/objectidentifier": "c7e2a091-4b38-4d65-9f12-b8a3e6d50c71"
},
"eventTimestamp": "2025-10-19T23:47:32.381Z",
"httpRequest": {
"clientIpAddress": "203.0.113.88", 2
"method": "PUT"
},
"operationName": {
"localizedValue": "Create or Update Container",
"value": "Microsoft.Storage/storageAccounts/blobServices/containers/write"
},
"resourceGroupName": "rg-production-eastus2",
"status": {
"localizedValue": "Succeeded",
"value": "Succeeded"
}
}
1 Entra ID service principal object ID used to create the container.
2 External IP address originating the request.

The Activity Log event was disconcerting.  Priya cross-referenced the caller’s object ID with Entra ID and confirmed it was the svc-automation service principal, a legitimate identity used by various automated processes throughout the organization. However, the source IP address 203.0.113.88 was neither an internal system nor a known Azure resource. She noted this as a possible indicator that the service principal credentials had been compromised and were being used by an external attacker. Priya expanded her investigation to identify all activity performed by the compromised service principal, as shown in Listing 47.

Listing 47 | Cloud Exfiltration Compromised Service Principal Activity
$ az monitor activity-log list --caller c7e2a091-4b38-4d65-9f12-b8a3e6d50c71 --offset 7d --query "[].{Time:eventTimestamp, Operation:operationName.localizedValue,
Provider:resourceProviderName.localizedValue}" --output table
Time                       Operation                         Provider

-------------------------  --------------------------------  ------------------------- 2025-10-15T14:23:18+00:00  Read Role Assignment              Microsoft.Authorization 2025-10-15T14:28:42+00:00  Read Virtual Machine              Microsoft.Compute 2025-10-16T03:15:27+00:00  List Storage Account Keys         Microsoft.Storage 2025-10-16T08:44:19+00:00  Create Role Assignment            Microsoft.Authorization 2025-10-17T11:32:54+00:00  Create or Update Security Rule    Microsoft.Network 2025-10-17T16:19:08+00:00  Create or Update Virtual Machine  Microsoft.Compute 1 2025-10-19T23:47:32+00:00  Create or Update Container        Microsoft.Storage 2

1 The attacker launched a virtual machine using the compromised service principal.

2 Creation of the unauthorized Blob Storage container.

The compromised service principal showed extensive unauthorized activity over five days. The caller enumerated role assignments, performed reconnaissance of existing virtual machines, obtained storage account access keys, and granted the service principal additional permissions through a new role assignment. Then they modified network security group rules, launched a virtual machine, and created the unauthorized container. Priya also queried the storage account’s diagnostic logs and identified 47 blob upload operations on October 19th corresponding to the files in the unauthorized container. Priya performed additional Activity Log and storage diagnostic log queries to trace the source of the blob uploads. She discovered that while the container was created from the external IP address 203.0.113.88, the uploads originated from a virtual machine at internal IP address 10.0.50.15 within the organization’s Azure virtual network. This event matched the virtual machine created on October 17th, indicating the caller had established infrastructure within the Azure environment to facilitate data exfiltration from internal resources.

Confident she was looking at the actions of an attacker who had compromised the svc-automation service principal, Priya documented the indicators of compromise discovered during her investigation:

• Account-based indicators : Compromised Entra ID service principal svc-automation with object ID c7e2a091-4b38-4d65-9f12-b8a3e6d50c71

• Network indicators: External IP address 203.0.113.88 used to create unauthorized resources

• Cloud resource indicators : Unauthorized Blob Storage container backup-data-archive-2025 in storage account stcorpdata01, attacker-created virtual machine at internal IP 10.0.50.15

• File-based indicators : 47 specific file names matching internal file server structure, including payroll data, customer PII, and intellectual property

• Behavioral indicators : Bulk blob upload pattern during a twenty-minute window, Azure management API activity from an external IP address, service principal usage outside normal automation patterns With these IOCs identified, Priya initiated enterprise-wide scoping activities to determine the full extent of compromise and exfiltration across the Azure environment, as shown in Table 15.

Table 15 | Cloud Exfiltration Scoping Commands
SCOPING OBJECTIVE COMMAND
Extend activity search to 90
days
az monitor activity-log list --caller c7e2a091-4b38-4d65-9f12-b8a3e6d50c71 --offset 90d
Enumerate all role assignments
for compromised principal
az role assignment list --assignee c7e2a091-4b38-4d65-9f12-b8a3e6d50c71 --all
Identify recently created or
modified storage containers
az storage container list --account-name stcorpdata01 --query
"[?properties.lastModified >= '2025-10-15']" --output table
