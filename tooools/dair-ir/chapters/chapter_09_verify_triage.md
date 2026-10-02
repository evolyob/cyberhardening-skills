﻿# Chapter 9: Verify and Triage Activities: Severity Scoring

Step 1. Select and Combine Detection Methodologies

Representative activities include:

• Use signature-based detection for efficient, high-confidence identification of known threats.

• Apply behavioral detection to identify threats that evade signatures, including mass file encryption, unusual access patterns, living-off-the-land techniques, and insider misuse.

• Scope behavioral baselines to business units or functional groups so meaningful anomalies stand out from normal activity.

• Layer ML-based detection for scoring and correlation at scale, using human-in-the-loop workflows to preserve analyst judgment on final classification.

• Map detection logic to MITRE ATT&CK techniques rather than specific indicators so rules remain effective as attackers modify tools.

Step 2. Operate Detection Data Sources

Representative activities include:

• Review EDR telemetry for process injection, credential dumping, persistence, and suspicious parent-child process chains.

• Analyze network monitoring data for C2 beaconing, lateral movement, and anomalous data volumes.

• Query SIEM platforms for attack patterns spanning multiple log sources.

• Apply SOAR automation to respond to high-confidence alerts.

• Monitor log source health to confirm critical feeds are delivering data as expected.

Step 3. Adapt Detection to Cloud-Native Environments

Representative activities include:

• Query cloud provider flow logs, control plane events, and Kubernetes audit logs for suspicious activity.

• Use eBPF kernel monitoring and container runtime socket telemetry to identify suspicious container activity.

• Use service mesh telemetry for east-west traffic visibility between services.

• For serverless and microservices workloads, collect function telemetry and watch for abnormal invocation patterns, unexpected outbound connections, unusual access to secrets or environment variables, and deviations from baseline execution characteristics.

• Unify telemetry across on-premises, hybrid, and multi-cloud environments to enable cross-environment correlation.

Step 4. Implement Data Reduction and Prioritization Strategies

Representative activities include:

• Apply detection-driven collection: define detection use cases first, then identify required data sources.

• Filter high-volume, low-value logs at the source before SIEM ingestion.

• Implement tiered data retention with hot, warm, and cold storage to balance accessibility and cost.

• Dispose of data that no longer supports a detection or forensic use case rather than degrading quality through aggregation or sampling.

• Correlate multiple low-confidence signals into high-confidence alerts.

• Apply statistical analysis to identify anomalous patterns such as periodic beaconing.

Step 5. Conduct Active Threat Hunting

Threat hunting in detect runs as a standing program, distinct from the IOC-driven enterprise sweep that scope runs during a verified incident.

Representative activities include:

• Operate threat hunting as a documented program with rotating hypotheses, tracked cadence, and auditable last-run dates.

• Prioritize hunting for TTPs and behavioral indicators over low-level indicators like hashes or IP addresses (Pyramid of Pain).

• Search for beaconing patterns, lateral movement, data staging, and living-off-the-land techniques.

• Run standing IOC sweeps against current and recent telemetry using IOCs from threat intelligence feeds. Incident-specific IOC sweeps belong to the scope activity once an incident is verified.

• Analyze encrypted traffic metadata (TLS client fingerprints, connection patterns, certificate attributes).

• Deploy TLS inspection for internal systems where policy permits to provide richer visibility for hunting and investigation.

• Document findings and new IOCs discovered during hunting.

Step 6. Monitor Passive Detection Sources

Representative activities include:

• Review automated alerts from security tools.

• Monitor employee reports of suspicious activity.

• Acknowledge employee reports promptly and supportively, even for false alarms, to sustain reporting culture.

• Track observations from system administrators and help desk personnel during routine operations.

• Validate third-party notifications using multiple factors (infrastructure legitimacy, IOC cross-reference, report quality) rather than source reputation alone.

Step 7. Respond to Detection Events

Representative activities include:

• Apply a false-positive prefilter using the local knowledge base before escalating, ruling out alerts that match documented benign sources without sending them to verify and triage.

• Document the EOI for handoff with the alert source, observation timestamps, affected assets, and technical indicators collected during detection.

• Escalate the documented EOI to verify and triage. Verification of whether the incident is real, CTI enrichment, and the continue/stop/defer decision belong to that phase.

• For EOIs originating from external researchers, acknowledge the report and establish the channel for ongoing updates.

Step 8. Continuously Improve Detection Capabilities

This step captures phase-specific feedback only; broader organizational changes are handled in debrief Step 8.

Representative activities include:

• Track detection metrics (MTTD, alert volume, false positive rate).

• Conduct purple-team exercises to test detection coverage against adversary evasion techniques.

• Update detection rules based on new threats and TTPs.

• Address detection gaps identified during incident response.

• Monitor for log tampering, disabled audit policies, and gaps in log data as indicators of adversary evasion.

• Retrain and recalibrate ML-based detection models to address model drift, validating training data for quality and avoiding contamination from mislabeled examples.

• Retain test environments for validating changes to detection logic before production deployment.

• Capture detection expertise in knowledge management systems for future reference.

• Review threat intelligence on attacker tooling and evasion methods.

• Surface staffing and sourcing decisions (analyst training investment, MSSP supplementation) to debrief Step 8 rather than acting on them within the detect activity.

9 Verify and Triage

Activities

In the DAIR model, we introduce an activity that is not specifically called out in other popular incident response models: verify and triage.  This step is often implied in the detection phase of PICERL or NIST SP 800-61 (Computer Security Incident Handling Guide), but we believe it is important to explicitly call it out.

Figure 57 | Verify/Triage Activity Waypoint

In the verify and triage activity, analysts are asked to perform two important actions:

• Verify the incident: Use the information collected during the detect activity to assess the incident’s validity and assign an initial risk impact classification to engage the broader incident response team.

• Triage the incident: Working with decision makers, determine appropriate response actions based on the risk impact classification and available incident information, including resource assignment to investigate the incident.

In this activity, analysts begin coordinating more actively with decision makers : individuals with the authority to decide on the incident response process. These decision makers are often managers or executives who can provide the necessary resources to respond to the incident, but may also include data owners, legal counsel, business unit leaders, or other stakeholders who have a vested interest in the outcome of the incident response process.

THE IMPORTANCE OF VERIFICATION

During verification, we use information collected during the detect activity to determine whether the incident is real or a false positive. Verification ensures that the incident response team is not spending resources on a non-existent incident, freeing the team to focus on other responsibilities. It also helps to build decision-maker confidence by ensuring the response is appropriate for the risk as understood at the beginning of the response effort.

In some cases, verification is straightforward: a defaced website, for example, is a clear indication of compromise. In other cases, the indicators of compromise are less clear, and the incident response team may need to spend time verifying the incident before proceeding with the response effort.

At this stage of the incident response process, we often have limited insight into the incident and must rely on information collected during the detect phase to make an initial assessment. We should also accept that sometimes the verification process will not reveal evidence of a compromise, despite unexplained behavior that might suggest otherwise.

VERIFICATION AS A GATING FUNCTION

A student once asked why the verify and triage step precedes the response action loop: “Wouldn’t it be better to move from detection directly to response action, repeating the verify-and-triage activity as we do for the scope, contain, eradicate, and recover activities?

VERIFICATION RESPONSE ACTIONS

During verification, the IRT reviews the information collected in the detect activity to determine the validity of the incident. Based on the information available, the IRT may take one of the following actions:

• Continue the incident response process: If the IRT determines that the incident is real, they will escalate and initiate the incident response process, engaging the broader incident response team and other company stakeholders and decision makers.

• Stop the incident response process: If the IRT determines the incident is not real, they will close it and document the findings for future reference.

• Defer verification: If the IRT is unable to determine the validity of the incident based on the information available, they may defer decision-making while requesting additional information from the reporting party or other sources.

The decision to continue, stop, or defer allows the analyst to make an initial assessment of the reported incident before engaging the broader incident response team, company stakeholders, and decision makers.

We include an illustration of this process in Figure 58.

Figure 58 | Verification Process

DOCUMENTATION

Documenting an incident as it unfolds produces a more accurate record than writing the documentation after the fact. Analysts naturally defer documentation under the pressure of active response. However, memories of specific commands, timestamps, and decisions fade once the response effort concludes, and reconstructing them later often produces an incomplete or misleading record. The incident response team should treat documentation as a continuous practice that begins at verification and accumulates throughout the response actions loop, rather than a task deferred to the end of the incident.

Documenting as the incident progresses produces a better record and breaks the tedious documentation task into smaller, more manageable pieces across the incident response process.

Using the documentation platform established during the incident preparation activity for incident tracking (see Identify a Platform for Incident Tracking ), the incident response analyst should capture information about the incident. This will begin an information-collection process that will continue throughout the incident’s lifecycle. Information to collect during the verification activity may include:

• Incident identifier: A unique identifier for the incident, often generated by the incident tracking platform.

• Incident title: A descriptive title for the incident, often based on the source of the report or the incident classification. The title serves as a quick, intuitive reference for the team when referring to the incident.

• Handler ID: The identifier for the incident response analyst responsible for assessing the incident.

• Incident summary: A brief description of the incident, including the source of the report, the date and time of the report, and any other relevant information.

• Incident classification: An initial incident classification, based on the information available. Some incident classifications might be unauthorized access, phishing, malicious code, sensitive data disclosure, account compromise, public-facing exploit, and more.

• Evidence references: References to evidence collected during the detect activity.

The documentation started during the verification activity is usually used throughout the incident response process to track the incident, document response actions, and provide a record for future reference.

Further, it can be used by the incident response team to provide updates to decision makers and other stakeholders as the incident response process progresses. Later, this documentation will be used to create a final incident report or as part of an organization’s cyber insurance claim.

At this point in the process, however, there is often a feeling of urgency to move quickly. While this is important, it is also important to document the incident accurately, with sufficient detail that it is useful for subsequent activities in the incident response process. A modern adage is that if you are typing too fast to take notes, you are just going too fast . Taking the time to document the incident also helps moderate the investigation’s pace, ensuring that the team does not move so quickly that it misses important details. for incident response documentation. This recommendation came from his many years as an expert witness, during which he witnessed numerous cases in which opposing attorneys questioned the integrity of the documentation.

Ed spoke of one case where he was waiting to be called while an attorney cross-examined another witness. The witness was a lead investigator in a major data breach investigation and had several notebooks of incident documentation submitted as evidence.

“Attorney: "Can you confirm that these notes were taken during your breach investigation?"

Witness: "Yes, this is my notebook from the investigation."

Attorney: "Can you also confirm that this notebook was only used for this investigation?"

Witness: "Yes, this is the notebook I used."

Attorney: "Are you in the habit of destroying evidence?"

Witness: (stunned) "No."

Attorney: "We counted the pages in this notebook, and there are 175 sheets out of the 180 sheets identified on the cover. What evidence did you intentionally remove?"

Modern investigations rely on digital documentation platforms rather than physical notebooks, but the lesson remains essential: opposing counsel will seek opportunities to question the integrity of notes and documentation. Avoid contamination of incident documentation by keeping notes focused on the incident at hand. Consider how the notes could be interpreted by an outside party. Try to be clear and accurate while being concise.

INITIAL RISK ASSESSMENT

In the Documentation section, we examined the importance of documenting the incident during the verification activity. We didn’t yet capture an initial risk assessment for the incident.

Before presenting the incident details to a decision-maker for consideration of response effort resource allocation, the incident response analyst should provide an initial risk assessment of the incident. There are many ways to classify incidents and assess their impact. Several projects are available to assist organizations with this task, including:

• Vocabulary for Event Recording and Incident Sharing (VERIS): Used in the Verizon Data Breach Investigations Report (DBIR) and other incident sharing communities to quantify incident impact

• Factor Analysis of Information Risk (FAIR): A risk analysis framework that helps organizations quantify and manage information risk

• NIST SP 800-30: A US government risk assessment framework that helps organizations identify, assess, and respond to risks to their information systems For many organizations, though, the initial risk assessment is simply a classification of the incident based on its perceived impact on the organization. This includes financial, operational, and reputational loss, as well as the potential regulatory impact. While these considerations will vary substantially among analysts within the same organization, evaluating the perceived impact allows the analyst to classify the risk into broad categories that can be used to communicate incident details to decision makers.

Many organizations classify incident risk into four levels:

• Low: Minor security anomalies with minimal impact.

• Medium: Potential security concerns requiring investigation but not disrupting operations.

• High: Confirmed incidents impacting business operations or data integrity.

• Critical: Major security incidents requiring executive escalation and immediate containment.

Adding the initial risk assessment to the incident documentation will help decision makers understand the potential impact of the incident on the organization, based on the analyst’s assessment.

VERIFICATION AND CYBER THREAT INTELLIGENCE

Cyber Threat Intelligence (CTI) provides valuable context during verification, helping analysts distinguish genuine threats from false positives and informing the risk assessment that guides triage decisions. By integrating CTI into verification workflows, organizations can make faster, more accurate determinations about whether to continue, stop, or defer incident response efforts.

In this section, we’ll examine three ways CTI strengthens verification: enriching Events of Interest to validate suspicious indicators, informing the initial risk classification with attribution and threat-actor context, and pivoting from a single indicator to related IOCs that expand the verification scope.

EOI Validation and Enrichment

When analysts encounter suspicious Events of Interest (EOI) during verification, CTI platforms can provide

Figure 59 | CTI Insight for IP Address IOC from VirusTotal

Figure 60 | CTI Insight for IP Address IOC from AlienVault OTX

CTI enrichment also helps identify false positives before they consume investigation resources. Legitimate services sometimes exhibit behavior that triggers security alerts: content delivery networks with unusual traffic patterns, cloud infrastructure with dynamic IP allocation, or security tools performing authorized scanning. Threat intelligence platforms often maintain databases of known-good infrastructure that can quickly rule out false positives. For example, regularly timed outbound connections to an unfamiliar IP address might initially appear to match common command-and-control activity patterns, but CTI enrichment revealing that the IP address belongs to Microsoft’s Windows Notification Service (WNS) infrastructure can quickly close the verification loop, as shown in Figure 61 and Figure 62.

Figure 61 | VirusTotal CTI for IPv6 Address Reveals Microsoft ASN

Figure 62 | VirusTotal CTI for IPv6 Address Reveals Server Identity

Build a local knowledge base of false positive sources specific to the organization’s document the finding for future reference. Over time, this organizational memory reduces verification time for recurring false positives.

Informing Initial Risk Classification

The same IOC can represent vastly different risk levels depending on what threat intelligence reveals about its origin, associated threat actors, and typical attack patterns. Using the CTI context, analysts can better assess the initial risk classification during the verification assessment.

For example, consider how attribution context influences our understanding of risk. A phishing email with a credential harvesting link might warrant a medium classification if threat intelligence associates it with a mass-distributed commodity campaign targeting broad populations. The same indicator escalates to high or critical if CTI links it to a threat actor known for targeting similar organizations with follow-on ransomware deployment.

The technical indicator is identical, but the threat context fundamentally changes the appropriate response.

Not all CTI signals carry equal weight when communicating risk to decision-makers. Threat intelligence indicators fall along a spectrum from circumstantial to behavioral:

• Circumstantial indicators : Infrastructure observations common to both legitimate and malicious activity. Examples include domain registration through low-cost registrars (Namecheap, Porkbun), free-tier hosting and CDN services (Cloudflare free tier, GitHub Pages), and short-validity certificates from automated certificate authorities (Let’s Encrypt). These indicators are easily reproduced by any actor and frequently appear in benign use, so they raise suspicion but rarely confirm intent.

• Behavioral indicators (TTPs) : Patterns that reflect a threat actor’s documented operational habits.

Examples include specific domain naming conventions ( secure-[vendor]-portal.com impersonation), tooling artifacts, and action sequencing documented in CISA advisories or vendor reporting. These indicators are harder for unrelated actors to reproduce coincidentally and provide stronger attribution confidence.

When briefing executives or other decision-makers, distinguish these classes explicitly. A finding supported by multiple TTP-level matches warrants different language than one resting primarily on circumstantial infrastructure as the basis for risk classification.

SAME DOMAIN, TWO RISK ASSESSMENTS

Consider a scenario: during routine log review, an analyst for an IT services provider notices connections to an unfamiliar domain in employee web proxy server logs: secure-sendwise-portal.com.

Investigating the domain, he notices it was registered only thirty-six hours ago, according to WHOIS data, which immediately raises suspicion.

Listing 34 | Proxy Log Entries Showing Connections to Newly Registered Domain

1734955847.284    127 172.16.42.108 TCP_MISS/200 0 CONNECT 198.51.100.47:443 - ORIGINAL_DST/198.51.100.47 - 1734955847.412     94 172.16.42.108 TCP_MISS/200 4891 GET hxxps://secure-sendwise-portal[.]com/api/v2/status - ORIGINAL_DST/198.51.100.47 application/json 1 1734955848.156    203 172.16.42.108 TCP_MISS/200 12847 GET hxxps://secure-sendwise-portal[.]com/assets/notify.js - ORIGINAL_DST/198.51.100.47 application/javascript 1734955912.891    142 172.16.42.108 TCP_MISS/200 2156 POST hxxps://secure-sendwise-portal[.]com/api/v2/register - ORIGINAL_DST/198.51.100.47 application/json 2 1734956147.445     87 172.16.42.108 TCP_MISS/200 891 GET hxxps://secure-sendwise-portal[.]com/api/v2/status - ORIGINAL_DST/198.51.100.47 application/json

1 Initial API call to the newly registered domain.

2 POST request suggesting data submission to an external site.

The traffic pattern shows a workstation connecting to the domain, loading JavaScript, and making periodic API calls. Without additional context, the analyst needs to determine whether this warrants escalation.

Interpretation 1: Assessment Without CTI Enrichment

The analyst investigates using available context. WHOIS shows the domain was registered thirty-six hours ago, but newly registered domains are common for SaaS vendors spinning up customer-specific infrastructure. The domain name secure-sendwise-portal.com follows a pattern consistent with legitimate secure document transfer services.

Checking the asset inventory, the analyst identifies that 172.16.42.108 is associated with a workstation in the accounting department. Accounting staff regularly interact with secure document portals, electronic signature platforms, and vendor payment systems as part of their normal duties. The traffic pattern (API calls, JavaScript loading, form submission) is consistent with a web application workflow.

The analyst concludes this is likely a new vendor tool that Accounting has started using. Without evidence of malicious behavior, the analyst documents the finding and closes the ticket.

→ Risk Classification: Low - Legitimate business activity, no further action.

Interpretation 2: Assessment With CTI Enrichment

A second analyst reviews the same finding but queries CTI platforms before closing. The results reveal a different picture.

The registrar (Namecheap), nameserver configuration (Cloudflare free tier), and Let’s Encrypt certificate pattern match infrastructure fingerprints documented in recent CISA advisories for Scattered Spider operations. The domain naming convention ( secure-[vendor]-portal.com) follows a pattern used by this threat actor to impersonate legitimate vendor login pages.

Further investigation reveals that Scattered Spider has targeted technology companies in the past thirty days using fake vendor portals to harvest credentials and MFA tokens.

→ Risk Classification: High - Immediate containment of affected workstation, credential reset for user, expand scoping to identify other affected systems, investigate whether credentials or sensitive data were submitted through the portal.

Both analysts examined the same proxy logs and applied reasonable judgment. The first analyst’s conclusion was defensible given the available context: the domain name looked legitimate, and the user’s role explained the traffic pattern. Without CTI enrichment, the indicators were ambiguous.

The second analyst’s CTI query transformed an ambiguous finding into a confirmed threat by revealing infrastructure fingerprints that matched known adversary patterns. CTI did not change the technical evidence, but it provided the context needed to interpret that evidence correctly.

Threat intelligence also informs risk classification by revealing the capabilities of attackers and the typical impact. CTI sources often document the outcomes of previous campaigns attributed to specific threat actors, including average dwell times, data exfiltration volumes, and recovery costs for victim organizations.

This historical context helps analysts calibrate their risk assessment against real-world consequences rather than theoretical harm.

When integrating CTI into risk classification, analysts should consider the following factors:

• Attribution confidence: How reliably does the CTI source link this indicator to a specific threat actor or campaign?

• Relevance to the organization : Does the threat actor target the organization’s industry, geography, or size?

• Attacker capability : Is the threat actor associated with sophisticated, persistent attacks or opportunistic, take-what-they-can operations?

• Typical impact: What outcomes have previous victims experienced when targeted by this threat actor?

The absence of threat intelligence does not indicate the absence of threat. Novel attacks, zero-day exploits, and emerging threat actors will not appear in CTI feeds until after initial victims have been compromised and intelligence has been collected and shared. Analysts should treat CTI as one input to verification, not the sole indicator of whether an incident is real.

Pivoting to Related Indicators

Threat intelligence platforms often provide relationships between indicators, allowing analysts to expand their verification scope based on known associations. A single suspicious indicator may connect to additional domains, IP addresses, file hashes, or behavioral patterns associated with the same campaign or threat actor.

When CTI reveals related indicators, analysts can search for those additional IOCs across the environment to determine whether the initial finding represents an isolated event or a broader compromise. This pivoting capability transforms verification from a single-indicator assessment into a more comprehensive evaluation of potential threat presence.

For example, an analyst investigating a domain hosting a ransomware message might discover through CTI that the domain shares infrastructure with several other domains used by the same threat actor. Searching proxy logs or DNS records for those related domains could reveal additional affected users or systems that the initial detection missed, as shown in Figure 63 . This expanded scope informs both the verification decision (continue vs. stop) and the subsequent scoping activity if the incident is confirmed.

Figure 63 | CTI Enrichment Reveals Related Indicators

CTI pivoting also helps analysts anticipate what else to look for if the incident is confirmed.  Threat intelligence often documents the Tactics, Techniques, and Procedures (TTPs) associated with specific threat actors or campaigns. If the indicator under verification is attributed to a threat actor known for deploying specific persistence mechanisms or lateral movement techniques, analysts can proactively search for those TTPs during scoping rather than discovering them reactively.

CTI pivoting is a powerful tool, but should not be relied upon as a sole means of verification. Threat actors can adapt their techniques, and new indicators may emerge that are not yet documented in CTI sources. CTI does not eliminate the need for thorough investigation and analysis during verification.

VERIFICATION ACTIVITY EXAMPLES

The following examples illustrate where verification is an important part of the incident response process.

The Unresponsive WordPress Site

A repeating help desk ticket caught the attention of the incident response team. A WordPress server used for distributing customer documentation for a software product was repeatedly reported as down or unresponsive. System administrators rebooted the server multiple times, resolving the issues. Engineering would close the help desk ticket, unable to reproduce the performance problems after a reboot, but the system would still become unresponsive, sometimes hours or days later.

Internal reporting from a savvy help desk analyst suggested that the problem might be broader than the engineering team realized. To verify the incident, the IRT collected logging information from the Apache web server. Reviewing the log activity revealed a large number of requests for a specific PHP file in the WordPress wp-includes directory, as shown in Listing 35.

Listing 35 | Apache Web Server Log Activity

42.105.168.75 - - [30/Jun/2024:00:36:29 -0400] "GET /wp-includes/FkhDUPZ.php HTTP/1.1" 200

65046892 "" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

42.105.168.75 - - [30/Jun/2024:00:36:29 -0400] "GET /wp-includes/FkhDUPZ.php HTTP/1.1" 200

65046886 "" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

42.105.168.75 - - [30/Jun/2024:00:36:29 -0400] "GET /wp-includes/FkhDUPZ.php HTTP/1.1" 200

65046884 "" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

42.105.168.75 - - [30/Jun/2024:00:36:29 -0400] "GET /wp-includes/FkhDUPZ.php HTTP/1.1" 200

65046886 "" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" 1

1 Multiple requests for the FkhDUPZ.php file in the WordPress wp-includes directory return large HTTP response sizes.

By itself, this was not enough to verify that this was an incident, though the engineering team could not explain the purpose of the strangely named FkhDUPZ.php file in the WordPress wp-includes directory.

Inspecting the contents of the file revealed the PHP file source code, as shown in Listing 36.

Listing 36 | Contents of Suspicious PHP File

intel-nyc1-01:~$ cat /var/www/html/wp-includes/FkhDUPZ.php

<?php

$b6bb6=explode("1l","stsixe_yek_yarra1lcexe_lruc1ltilps_gerp1ldomhc1lstegf1lteg_ini1lemitotrts1l

ecalper_gerp1lrid_

pmet_teg_sys1lnepof1lstsixe_elif1lsoprts1lknilnu1lemitmelif1ldro1lstsixe_noitcnuf1lmirt1lpeelsu1

lemaner1lezilairesnu1lel

if_5dm1lesolc_lruc1ltes_ini1lrhc1lesolcf1lyarra_ni1ltcartxe1ltimil_emit_tes1lhctam_gerp1ltroba_r

esu_erongi1lpeels1lehcac

tatsraelc1lhcuot1ltpotes_lruc1lrtsbus1letirwf1lnelrts1lfoef1lezilaires1llru_esrap1lelbatirw_si1l

5dm1lstnetnoc_teg_elif1l

emitorcim1lecalper_rts1ltini_lruc1lelif_si");foreach($b6bb6

as$b66bb6666⇒$b6bbb6){$b6bbb6=preg_split("//",$b6bbb6,-1,PR

EG_SPLIT_NO_EMPTY);$b6bb6[$b66bb6666]=implode("",array_reverse($b6bbb6));};$b66666b=FILE;$bb66b=

explode("9","b6bbbbb 69b6bb6bbb9bbbbbb9b69b6bb66b9b66bb6b69bb6bbb69b6666b6b9bbbb6b669b6bbb6b69bbb6bbb9bb9b6b66b669bb6 9bb669bbbb6b9bb6b6bbb9b6 bbbbb6b9bb666666b9b66bbb9bb66bb6669bbb6b6b69b6bb6b69bb6b6b69bb6b69b6b9b666b9bbb6bb9bbbb69bbb669b bb6b6669b6bbb9bbb6bb6bb9 bbbbbb69bbbb9bb66669b6b6bb9bbbb6bb9bbb6b69bb66bbb669b6b6bb69b6bb669bb66b66b9b6b66b6b69bbbb6b6b9b 66bb6b9b66666");foreach( $bb66b as$b6666b66⇒$bbb6bbb6){$$bbb6bbb6=$b6bb6[$b6666b66];}; ... 1

1 Obfuscated PHP code (truncated).

Obfuscated code on its own does not establish malicious intent. Legitimate WordPress plugins and themes occasionally obfuscate source for licensing or intellectual property protection, so the IRT treated the obfuscation as cause for further review rather than confirmation of compromise.

The IRT computed a SHA-256 hash of FkhDUPZ.php and submitted it to CTI sources, which returned matches against known PHP webshell families. As corroboration, the team confirmed that FkhDUPZ.php did not appear in the official WordPress release manifest for the installed version, indicating the file had been added outside the legitimate update process. With the CTI match and the file-integrity discrepancy together, the IRT confirmed the report as an incident, escalating the event to involve the broader incident response team and other company stakeholders and decision-makers.

Undesirable system activity, such as high CPU utilization, unexpected storage consumption, or unexplained instability, is not always an indicator of compromise, but it should be investigated to identify the root cause. In this case, the incident response team verified the incident by examining the Apache web server logs to identify anomalies, including frequent requests to the FkhDUPZ.php file, unusually large HTTP response sizes for those requests, and the contents of the suspicious PHP file.

The Unpaid Toll

An accounts payable clerk forwarded a suspicious text message he received to the incident response team, as shown in Figure 64. The message purports to come from the Rhode Island Turnpike and Bridge Authority (RITBA), a US state agency that operates toll bridges in Rhode Island. It demands payment for an unpaid toll.

Figure 64 | Suspicious Text Message

“Rhode island turnpike(RITBA): This is a final reminder regarding the unpaid toll from your trip. A $15 daily overdue fee will be applied if it is not settled today. hxxps://google[.]com/amp/rhodeislandturnpike.com

Figure 65 | Unpaid Toll Redirect to "Rhode Island Turnpike" Website

While the site had a semi-professional appearance that matched other Rhode Island government websites, the IRT suspected this was a phishing attempt. Using threat intelligence resources, the analyst learned that the rhodeislandturnpike.com domain had been registered that day, as shown in Listing 37 . Further, the website server certificate was also created that day, as shown in Listing 38.

Listing 37 | Domain Registration Creation Date

$ date -u

Sun Feb 16 20:11:32 UTC 2025

$ whois -i rhodeislandturnpike.com | grep -i 'creation date'

Creation Date: 2025-02-16T06:37:27Z 1

1 Domain registration for rhodeislandturnpike.com was created less than fourteen hours prior.

Listing 38 | Website Server Certificate Start Date

$ date -u

Sun Feb 16 20:13:31 UTC 2025

$ curl -svX HEAD hxxps://rhodeislandturnpike[.]com/ 2>&1 | grep -A6 "Server certificate"

* Server certificate:

*  subject: CN=rhodeislandturnpike.com

*  start date: Feb 16 06:01:28 2025 GMT 1

*  expire date: May 17 06:01:27 2025 GMT

*  subjectAltName: host "rhodeislandturnpike.com" matched cert’s "rhodeislandturnpike.com"

*  issuer: C=US; O=Let’s Encrypt; CN=E5

*  SSL certificate verify ok.

1 The server TLS certificate was created approximately fourteen hours prior.

In their conversation, the accounts payable clerk indicated that he did not follow the SMS link and did not visit the "Rhode Island Turnpike" website. The phone’s browser history confirmed this account. Further, the analyst found no other evidence of web activity to rhodeislandturnpike.com in the company’s web proxy server activity logs.

After conferring with another analyst on the IRT, the incident was classified as an Indicator of Attack (IOA), but not as an Event of Interest (EOI) warranting further investigation. The IRT added the rhodeislandturnpike.com domain name and the server IP address to the threat intelligence platform for monitoring, and the incident was closed.

An indicator of an attack may not always qualify as an event of interest warranting additional investigation. For many organizations, the verification process is an opportunity to limit the number of incidents that require further investigation and to focus on those most likely to have a significant impact on the organization.

The Simple, Secure Storage Bucket

An analyst on the incident response team received a report concerning the disclosure of a vulnerable Amazon Simple Storage Service (S3) bucket. The report was from an unknown source, a self-identified bug bounty hunter , indicating that they found a high-risk vulnerability in the sample-data-bucket S3 bucket. The bug bounty hunter wanted to know the organization’s policy on rewarding bug bounty hunters for their work.

The company analyst reviewed the report and identified that the sample-data-bucket bucket was indeed used by one of the company’s AWS accounts. Using the AWS Command Line Interface, she reviewed the bucket’s security settings, as shown in Listing 39.

Listing 39 | AWS S3 Bucket Policy

$ aws s3api get-bucket-policy --bucket sample-data-bucket | jq '.Policy | fromjson'

{

"Version": "2012-10-17",

"Id": "sample-data-bucket-Policy",

"Statement": [

{

"Sid": "AllowPublicRead",

"Effect": "Allow",

"Principal": {

"AWS": "*"

},

"Action": [

"s3:Get*", 1 "s3:List*" 2

],

"Resource": [

"arn:aws:s3:::sample-data-bucket",

"arn:aws:s3:::sample-data-bucket/*"

]

}

]

}

1 The bucket policy allows any AWS principal to apply S3 get actions, including GetObject, GetBucketLocation, GetBucketPolicy, and more.

2 The bucket policy allows any AWS principal to apply S3 list actions, including ListObjects, ListBucketAnalyticsConfigurations, and more.

Reviewing the policy details, the analyst confirmed that the bucket policy allowed any AWS principal to apply S3 get and list actions to the bucket and its contents. This allowed any AWS account (from any organization) to list the files in the bucket and retrieve the contents of any file. However, she also knew that this bucket was used for public data sharing, including company website resources, the distribution of images, CSS, fonts, JavaScript files, and other related data.

To determine whether this required action by the incident response team, the analyst reviewed the contents of the bucket, as shown in Listing 40.

Listing 40 | AWS S3 Bucket Contents

$ aws s3 ls s3://sample-data-bucket

PRE css/

PRE dist/

PRE fonts/

PRE images/

PRE js-lib/

PRE js/

PRE pdf/

PRE uat/

$ aws s3 ls s3://sample-data-bucket/uat/

2025-02-14 14:56:41     112537 acceptance_summary.pdf

2024-05-12 11:03:12       2520 config.json

2025-02-05 11:20:15      19264 cross_browser_test.xlsx

2024-11-15 09:12:45       5515 database_seed.sql

2025-01-03 14:22:01       6472 error_log.log

2024-10-12 12:01:42      15036 feature_toggle.yaml

2024-12-15 08:45:33      22491 integration_test.py

2025-01-25 10:05:35      17055 mobile_test_cases.docx

2025-02-10 12:40:03      14491 performance_metrics.csv

2024-11-23 17:05:19      12848 performance_report.txt

2024-09-20 11:45:50      30059 sample_api_response.json

2024-12-01 10:03:58      40927 sample_users.csv

2025-01-15 13:35:22      24037 security_audit.txt

2024-10-05 15:27:35      19957 test_case.docx

2024-06-17 14:22:10      17103 test_script.sh

2024-11-03 16:30:11       1987 uat.env

2024-09-01 10:10:31      10295 uat_deploy.sh

2024-09-15 08:33:25       9087 uat_log.txt

2025-01-20 09:50:38      26982 ui_mockup.png

2024-07-20 09:15:05      41033 user_data_sample.csv

The S3 bucket contained several folders that appeared to be related to public website resources, as well as a pdf folder and a uat (User Acceptance Testing) folder. The analyst reviewed the contents of the pdf folder and found that it contained public documentation, and the uat folder contained documentation, test data, and sample configuration data for several products.

What remained unclear was whether the bucket configuration and the data met the organization’s business needs. Was the intention to share this data publicly, or was this a misconfiguration? Were any of the files in the bucket sensitive, or was the data intended for public use?

The analyst reached out to the AWS account holder of the sample-data-bucket bucket to confirm its purpose and contents. She advised that the team responsible for this asset review each file contained in the bucket and determine whether sensitive data is disclosed. She insisted that the review was urgent, and asked the account owner to return his analysis by the end of the day. Once that review was complete, she could determine if the bucket configuration and information disclosure warranted further investigation by the incident response team.

During verification, analysts use available information to assess threats and risks to the organization. Analysts apply insight into the potential incident, an understanding of the organization’s policies and procedures, and familiarity with the policies created and reviewed during the preparation activity to determine the appropriate response. In some cases, additional information will be required, necessitating the team deferring the verification decision to a later date.

A TEMPERAMENTAL SERVER

A customer reached out to investigate a Windows server that was behaving erratically. The system administrator reported unexpectedly high CPU utilization across multiple processes, crashed services, and unexplained password changes. This went on for weeks before the administrator responded to a Blue Screen of Death (BSOD) error message. The customer hired us to investigate the incident and determine the source of the compromise.

The system in question was a virtual machine, making it easy to take a snapshot and analyze it offline.

We spent several days investigating processes, services, scheduled tasks, Windows Management Instrumentation (WMI) queries, and other system elements. We reviewed system logs, network activity, memory dumps, and other forensic artifacts to identify the source of the compromise.

We didn’t find any indicators of compromise.

We reported our findings to the customer, who insisted the system was compromised. Because of the system’s unexpected behavior, the customer was convinced that the system was under the control of For this customer, we spent extra time showing them the evidence we collected and explaining why we believed the system was not compromised. Eventually, they rebuilt the system from scratch, and the unexpected behavior ceased.

The Temperamental Server example highlights a recurring verification challenge: proving a negative .

Confirming a system is compromised requires a single credible indicator of attack or event of interest.

Confirming a system is not compromised requires demonstrating coverage across the relevant attack surface, including running processes, persistence mechanisms, scheduled tasks, file system changes, network activity, and authentication logs. Stakeholders rarely accept we found nothing  with the same confidence they accept we found something, and analysts may face pressure to keep investigating long after the team has covered the reasonable scope.

The defensible response is to document investigation scope explicitly: what was examined, what tools were used, what time windows were covered, and what evidence sources were beyond the team’s reach. With that record in hand, a clean verdict can be defended on the basis of the work performed rather than on the absence of findings alone.

TRIAGE ACTIVITY

In the triage activity, analysts work with decision makers to determine appropriate response actions based on the risk impact classification and the incident information available. This may include assigning resources to investigate the incident, engaging legal counsel, or notifying law enforcement, depending on its severity.

Few organizations would claim that they have more resources than they need for their incident response function. For most organizations, the incident response function is a cost center that costs the organization money. Unlike a profit center that generates revenue, the incident response team will always be scrutinized for the resources it consumes. During triage, the incident response analyst provides sufficient insight to decision makers to determine appropriate response actions based on the risk impact classification and the incident information available following the verify activity.

In medicine, triage is the process of determining the priority of patients' treatments based on the severity of their condition. Broadly speaking, patients with high-severity conditions are prioritized over those with less severe conditions. In incident response, a similar concept applies: threats should be prioritized based on organizational policies, often using the potential negative impact on the organization as a guide.

Presenting the Incident

As technical analysts, responders are responsible for helping decision makers understand the incident and its potential impact on the organization. Using the insights gained from the verification activity and initial risk assessment, the analyst’s explanation of the incident substantially impacts how the risk is triaged and response actions taken.

When presenting the incident to decision makers, analysts should consider the following:

• Be clear and concise: Use plain language to explain the incident and the potential impact on the organization.

• Provide context: Explain the incident in the context of the organization’s policies and procedures, and the potential impact on the organization’s operations.

• Offer recommendations: Provide response actions based on the risk impact classification and available
