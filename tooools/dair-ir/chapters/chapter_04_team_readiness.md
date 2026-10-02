# Chapter 4: Getting Started: Roles, Teams & Playbooks

That format, a checklist of numbered actions framed by the problem each one was meant to prevent, set the

template for practical incident response documentation in the years that followed. The Step-by-Step

sections that close each chapter of this book are a direct continuation of that lineage.

In January 2004, the National Institute of Standards and Technology (NIST) published Special Publication

800-61, Computer Security Incident Handling Guide , building on the foundations laid by CIAC, the US Navy,

and SANS.  Unlike the earlier six-step models, NIST SP 800-61 introduced a four-step incident response

lifecycle: Preparation; Detection and Analysis; Containment, Eradication, and Recovery; and Post-Incident

Activity. This four-step model continued to be recommended in the March 2008 update (NIST SP 800-61

Revision 1) and the August 2012 update (NIST SP 800-61 Revision 2). In April 2025, NIST departed from the

four-step model to align with the broader NIST Cybersecurity Framework (CSF), adopting a new six-step,

high-level model: Govern, Identify, Protect, Detect, Respond, and Recover.

Figure 11 | Timeline of Incident Response Models and Early Cybersecurity Incidents

The development of incident response models has been shaped by the evolving landscape of cybersecurity

threats and the growing recognition of the need for structured incident response. From the early days of

CERT and CIAC to the widely adopted frameworks from SANS and NIST, these models have provided

organizations with the tools and methodologies needed to respond to and recover from cybersecurity

incidents. As threats continue to evolve, so too should the models and practices for incident response,

ensuring that organizations remain resilient in the face of an ever-changing threat landscape.

FROM THESE FOUNDATIONS

The arc from CIAC’s 1990 guidelines through NIST SP 800-61 Revision 3 reflects three decades of

4 Getting Started

Throughout this book, we’ll explore several important considerations to review and assess the incident

response process. Some involve vocabulary, enabling everyone on the team to communicate effectively and

efficiently. Others are strategies that provide a clear way to measure the effectiveness of the response

effort.

In this chapter, we’ll look at some of the common terms used in incident response. We’ll also examine the

important considerations of core incident response concepts.

INCIDENT

An incident is an adverse event in an information system and/or network, or the threat of such an event

occurring. [1]

An incident implies harm, or an attempt to cause harm.

This is the classic definition of an incident, but there are many nuances to consider. For example, not all

incidents look the same: some result from a deliberate attack, others from human error, and still others

from environmental causes beyond anyone’s control. Defining an incident as malicious, accidental, or

Accidental Incidents

These incidents result from unintentional actions that cause harm to systems or data. A user deleting

sensitive data, a firewall misconfiguration that exposes internal services to the internet, a developer

committing API credentials to a public repository, or a partner accidentally exposing customer data in a

Google Cloud bucket all warrant an incident response.  [2]

Accidental incidents often overlap with malicious

incidents during the early stages of investigation, since the initial indicators (e.g., exposed data or

unauthorized access) can look similar before the root cause is understood. When the root cause is

understood, the incident response effort shifts to remediation and prevention, with less focus on

determining a threat actor’s actions.

Environmental Incidents

These incidents are caused by natural events or infrastructure failures rather than human action. Examples

include power outages that result in unclean system shutdowns and data corruption, flooding that damages

a data center, or a cloud provider outage that disrupts critical services. While environmental incidents are

outside the scope of this book, organizations should maintain response plans that address them alongside

cybersecurity incidents.

In practice, not every organization declares an incident immediately. In regulated industries, the label

incident can trigger notification obligations and regulatory timelines, so many organizations deliberately

operate in a pre-incident investigative state until they know more. During this phase, the response team

gathers information and assesses scope without formally classifying it as an incident. This approach is

common and pragmatic, but it also means that response activities covered later in this book may begin

before the organization officially declares an incident.

EVENT

An event is any observable occurrence in a system and/or network. This is a straightforward explanation,

but the concept of events and how analysts assess and evaluate them can be complicated and vary when

working with commercial products and vendors that shape vocabulary to fit their offerings. The following

examples expand on the concept of events.

Whether working in an incident response team or a security operations center (SOC), whether involved in a

case by applying digital forensics investigation techniques, or as a system administrator maintaining

systems, analysts work with events. Events are an unending flow of information that characterizes and

records the activities of systems and networks. Examples of events include:

• Fortinet firewall log entry: msg="Unregistered device localhost add succeeded" device="localhost"

adom="FortiManager"

• Apache web server error log: PHP Fatal error: Uncaught Error: Call to undefined function

add_action() in public_html/wp-content/plugins/hello.php:69

• Support desk ticket #12345: User reports sluggish performance on their workstation

• Windows Event ID 104: The System event log was cleared.

• Linux auth log entry: systemd: pam_unix(systemd-user:session): session opened for user httpd by

(uid=0)

• Network device log: Administrator accessed UniFi OS via unifi.ui.com. Source IP: 95.181.86.2

• OPS engineer reports a previously unrecognized local user on camera access server: badmin

Many analysts think of events exclusively as data recorded by logging sources. However, events can also

come from non-digital sources, such as a system administrator’s report of a system outage, or a user’s

request for assistance when their workstation suddenly becomes sluggish.

When discussing the flow of events in any collection of systems, this book uses the analogy of a waterfall.

Consider the waterfall as the flow of events, cascading down from the top of a rocky outcropping, as shown

in Figure 12. Analysts can monitor these events as they flow down the waterfall, or as they are collected in a

pool at the bottom.

Figure 12 | Waterfall of Events

Analysts extract insights from event flows, identifying patterns and anomalies that could indicate an

incident. The event might be a message in a log file, an activity observed on the network, a report of unusual

activity from a user, or another observable occurrence. Most events are not indicative of an attack or

incident. However, some events will warrant further investigation. These are referred to as Events of

Interest (EOI).

EVENT OF INTEREST

An Event of Interest  (EOI) is an event that warrants further investigation. When considering the unending

Consider the events shown in Figure 13. This illustration annotates several of the events:

• Unrecognized browser session: The web application server records the start of a new session for a user

who has not previously logged in.

• Access from source IP 95.181.86.2: A Web Application Firewall (WAF) logs an access request from

95.181.86.2, an IP address that is known to be associated with malicious activity by Cyber Threat

Intelligence (CTI) sources.

• Unusual access time: A system accesses an application at 3:00 AM, a time when the system is typically

not in use.

• Incorrect username login attempt: A user attempts to log in with the username admin, which is not a

valid username for the system.

Figure 13 | Waterfall of Events with Events of Interest

Each of these events could indicate an incident, or they could be benign. However, any single event by itself

provides limited insight. Events are best reviewed in context, and that context is often provided by other

events, ordered by time, source, reporting system, and other factors. While some individual events may

indicate the presence of an incident, analysts often need to assess the flow of events as a whole to identify

an incident.

ORGANIZATIONAL DEFINITION OF EOI

An event is not necessarily an incident, though it can contribute insight into the occurrence of an

incident, or multiple events can be correlated to identify an incident. However, what qualifies as an

EOI for one organization might not apply in another.

For example, consider the MySQL database query shown in Listing 25, reporting on login failures for a

WordPress server.

Listing 25 | MySQL Query Reviewing WordPress Login Failure Events for the Last 24 Hours

mysql> SELECT event_type, DATE_FORMAT(FROM_UNIXTIME(MIN(created_on)), '%Y-%m-%d %H:%i:%s')

AS first_observed_failure, client_ip, COUNT() AS failure_count FROM wp_wsal_occurrences

WHERE alert_id = 1002 AND FROM_UNIXTIME(created_on) >= NOW() - INTERVAL 1 DAY GROUP BY

event_type, client_ip ORDER BY first_observed_failure ASC;*

+--------------+------------------------+-----------------+---------------+

| event_type   | first_observed_failure | client_ip       | failure_count |

+--------------+------------------------+-----------------+---------------+

| failed-login | 2024-12-30 12:44:36    | 13.214.39.195   |             9 |

| failed-login | 2024-12-30 12:59:02    | 185.196.220.113 |         40592 | 1

| failed-login | 2024-12-30 13:10:18    | 13.214.202.144  |             3 |

| failed-login | 2024-12-30 22:11:25    | 3.101.81.132    |             8 |

| failed-login | 2024-12-30 22:18:20    | 54.151.17.204   |            10 |

| failed-login | 2024-12-31 10:44:19    | 35.72.8.125     |             3 |

| failed-login | 2024-12-31 11:51:57    | 18.183.180.112  |             1 |

+--------------+------------------------+-----------------+---------------+

7 rows in set (8.59 sec)

mysql> select object, event_type, user_agent from wp_wsal_occurrences WHERE alert_id =

1000 AND client_ip = '185.196.220.113';

Empty set (3.75 sec) 2

1 40,592 failed login attempts from 185.196.220.113

2 No successful login activity from 185.196.220.113

The first SQL query interrogates the WordPress Security Audit Log (WSAL) table for failed login

events, grouping by event type and client IP address, ordered by the first observed failure. Each of

these events represents one or more login failures, and each could qualify as an EOI for investigation.

The second query interrogates the same table to retrieve successful login events for the IP address

with the most login failures. However, the absence of successful login  records (the empty set)

indicates that the login failures did not result in a successful login.

One organization, upon reviewing this logging data, might characterize it as an attack and commence

an investigation. Another organization might consider it an attack, but not an EOI, since the attack

was unsuccessful.

The decision to use one or more events to qualify as an incident should take into account the

organization’s policies and priorities. While the events themselves are objective, their interpretation

an aggregated view, denoting multiple login failure events and a successful login followed by an MFA failure

as aggregate EOI. This view is still not necessarily an incident, depending on organizational policy (see the

sidebar Organizational Definition of EOI). However, the aggregate EOI provides a fuller picture of the events

that could indicate an incident warranting investigation.

Figure 14 | Waterfall of Events with Aggregate Events of Interest

For the incident response team, events are an important data source that provides insights into potential

incidents. Ideally, organizations should collect and store useful events for a reasonable retention period,

one that accounts for event type and organizational needs. This collected pool of events provides historical

context and valuable data for analysts, often stored in a Security Information and Event Management (SIEM)

system or another log management platform.

INDICATOR OF COMPROMISE

An Indicator of Compromise (IOC) is evidence of a successful compromise. While some events can also be

used as IOCs, IOCs are typically more specific data points. IOCs are associated with a source of intelligence,

such as a threat intelligence feed, to provide the insight needed to characterize evidence as produced by a

compromise. IOCs may be characterized as atomic, computed, or behavioral. [3]

The most commonly reported IOC type is an atomic IOC . The phrase atomic means the IOC is a single,

specific data point that can’t be broken down further. Atomic IOCs are valuable as an analysis tool because

they rarely generate false positives. They are also easy to apply in automated detection systems, as no

additional computation or analysis is required to identify the IOC. Common examples of atomic IOCs

include file names, registry keys, URLs, and IP addresses.

A computed IOC is derived from data observed in a system after some calculation or analysis. For example,

an attacker might randomize the name of a file used to stage a persistence mechanism on a compromised

Windows workstation, thereby preventing easy atomic IOC identification based on the file name. However,

computing a hash of the file contents, disregarding the file name, produces an IOC that can be used to

identify the file. Other examples of computed IOCs include a regular expression match in a command-line

expression. The pattern can trigger an IOC alert when the command line exceeds a specified length or

contains content that matches a known attack pattern. Like atomic IOCs, computed IOCs are easy to apply

in automated detection systems, but require slightly more processing to identify.

Finally, a behavioral IOC  is a data point derived from the combined analysis of attacker behavior, events,

atomic IOCs, and computed IOCs.  Behavioral IOCs are more complex to identify, as they require analyzing

data and understanding attacker Tactics, Techniques, and Procedures (TTPs). They also require a baseline of

normal system behavior. Behavioral IOCs are also a valuable tool for detecting incidents, allowing analysts

to identify attackers using new or unknown techniques through anomaly analysis or pattern matching.

Analysts work with IOCs to identify the presence of an attacker in a system, on the network, in logging data,

or as part of forensic analysis. Threat intelligence feeds provide a valuable source of IOCs, allowing analysts

to identify known threats and apply indicators to their systems to detect attacker presence.  For example,

consider the IOCs shown here, disclosing logging entries when an attacker exploits a vulnerability in the

Fortinet FortiGate firewall product (CVE-2024-55591):

“Following admin creation log with seemingly randomly generated user name and source IP: type="event"

subtype="system" level="information" vd="root" logdesc="Object attribute configured"

user="admin" ui="jsconsole(127.0.0.1)" action="Add" cfgtid=1411317760 cfgpath="system.admin"

cfgobj="vOcep" cfgattr="password[*]accprofile[super_admin]vdom[root]" msg="Add system.admin

vOcep [4]

Using this threat intelligence, analysts can examine Fortinet device logs to identify successful exploitation of

the Fortinet FortiOS vulnerability described in CVE-2024-55591. By developing a detection capability that

can automatically evaluate Fortinet device logs, analysts can use the IOC to identify compromised Fortinet

devices. In this case, analysts can match the log entry using an atomic IOC by focusing on the static

elements of the log entry. Using the syntax described by the Sigma detection format, analysts can develop a

computed IOC using pattern matching with the regular expression syntax. A sample Sigma rule is included

in Listing 26.

Listing 26 | Sigma Rule for Fortinet FortiOS IOC Detection

title: Fortinet FortiOS Exploit Attempt - FG-IR-24-535

id: 8c67a5b8-9e6b-4f34-a90f-7b728f02856e

status: experimental

description: Detects exploitation of CVE-2024-55591 against Fortinet FortiOS devices where an

attacker creates a new admin user.

references:

- hxxps://www[.]fortiguard[.]com/psirt/FG-IR-24-535

author: Joshua Wright

date: 2025-03-12

logsource:

category: firewall

product: fortinet

service: fortios

detection:

keywords: 1

- 'type="event"'

- 'subtype="system"'

- 'logdesc="Object attribute configured"'

- 'action="Add"'

- 'cfgpath="system.admin"'

- 'cfgattr="password[*]accprofile[super_admin]vdom[root]"'

condition: keywords

falsepositives:

- Unknown

level: high

tags:

- attack.persistence

- cve.2024.55591

- cve.2024.24472

- fortios

- fortinet

1 The keywords used in the Sigma rule to identify the FortiOS exploit matching the IOC intelligence disclosed in the Fortinet

advisory.

An IOC is a piece of intelligence that analysts can make actionable. Whether applied through Sigma rules for

log detection, an Endpoint Detection and Response (EDR) product, a Network Detection and Response

(NDR) product, or another tool, the IOC represents the actionable insight needed to identify incidents.

WHAT ABOUT INDICATORS OF ATTACK (IOA)?

Indicator of Attack (IOA) is a term popularized by CrowdStrike to describe its detection capabilities

based on an attacker’s behavior. The authoritative reference for IOA is written by Kurt Baker, senior

director of product marketing for intelligence at CrowdStrike:

“Indicators of attack (IOA) focus on detecting the intent of what an attacker is trying to accomplish,

regardless of the malware or exploit used in an attack. Just like AV signatures, an IOC-based

detection approach cannot detect the increasing threats from malware-free intrusions and zero-

day exploits. [5]

CrowdStrike uses IOAs to identify the presence of an attacker in a system based on the attacker’s

behavior rather than the specific tools or techniques used. Along with advanced threat detection

capabilities, CrowdStrike uses a series of connected events deemed suspicious or malicious to detect

threats.

In practice, the distinction between an IOA and a behavioral IOC is subtle. While simpler detection

mechanisms (atomic IOC and computed IOC) remain valuable for detecting known threats, IOAs and

behavioral IOCs offer more advanced capabilities for detecting known and unknown threats. Whether

analysts use the term IOA or behavioral IOC, the concept is the same: identifying the presence of an

attacker based on their behavior, rather than limiting detection to specific atomic or computed IOCs.

MEAN TIME TO DETECT

Mean time to detect (MTTD) is a metric used to measure the average time it takes to identify a security

incident. It is used to measure the performance of an organization’s SOC and incident response team.

MTTD is calculated by taking the total time to detect all incidents over a specific period and dividing it by

the number of incidents detected during that period:

As a performance metric, MTTD is useful for tracking the time lag between when an incident occurs and

when it is detected. For example, if an attacker compromises a system and remains undetected for several

days, the MTTD will be high, indicating that the organization’s detection capabilities need improvement.

Conversely, a low MTTD indicates that the organization can quickly identify and respond to incidents.

Challenges with MTTD Measurement

MTTD is a broad metric that can vary significantly based on the type of incident, the organization’s size and

complexity, and the maturity of its security operations. According to various security reports, average

MTTD ranges from days to months, depending on the organization and attack type. The IBM Cost of a Data

Breach Report indicates that organizations take an average of 204 days to identify a breach. [6]

The Verizon

Data Breach Investigations Report shows significant variance across different attack vectors, with some

incidents detected in minutes while others remain undetected for months. [7]

Organizations with mature

security operations centers (SOCs) and robust detection capabilities often achieve MTTD measured in hours

or even minutes for critical incidents. Industry leaders with advanced threat detection and automated

monitoring systems report MTTD of less than twenty-four hours for most incident types. [8]

Another challenge with MTTD is defining when an incident occurs. In many cases, the exact time of the

compromise is unknown, and organizations should estimate the occurrence time based on the earliest

observed IOC. However, this metric is subject to change, and the occurrence time will be updated as new

evidence is discovered during the investigation. Often, the occurrence time is only known after the incident

has been fully investigated and remediated, making the MTTD a retrospective metric.

For MTTD to be useful, it should be tracked over time and consistently defined across the organization.

Organizations should establish clear criteria for what constitutes an incident and ensure that all incidents

are logged with accurate timestamps for when they occurred and when they were detected. By tracking

MTTD over time, organizations can identify trends, assess the effectiveness of their detection capabilities,

and make informed decisions about where to invest in improving their security posture.

MEAN TIME TO RESPOND

Mean time to respond (MTTR) is a metric that measures the average time to respond to and resolve a

security incident after it is detected. While MTTD measures the efficacy of an organization’s detection

MTTR is calculated by taking the total time to respond to and resolve all incidents over a specific period and

dividing it by the number of incidents resolved during that period:

As a performance metric, MTTR helps track how quickly an organization can contain, resolve, and recover

from security incidents. For example, if an organization takes an average of forty-eight hours to respond to

and resolve incidents, this provides a baseline for measuring improvement efforts. A lower MTTR indicates

that the organization has effective incident response processes, adequate staffing, and appropriate tools to

quickly address security threats. Conversely, a high MTTR may indicate gaps in response procedures,

resource constraints, or technical challenges that slow down incident resolution.

MTTR is often used alongside MTTD to provide a comprehensive view of an organization’s security posture.

While MTTD measures how quickly threats are identified, MTTR measures how quickly they are addressed.

Together, these metrics help organizations understand the complete lifecycle from initial compromise to

resolution.

The total time from when an incident occurs to when it is resolved can be expressed as:

Challenges with MTTR Measurement

For MTTR to be a useful metric, organizations should clearly define what constitutes "resolution" for each

incident type. This might include containing the threat, removing the attacker’s presence, recovering

affected systems, and verifying that the threat has been fully addressed. Consistency in measurement is

crucial for MTTR to be a valuable metric, as different teams or departments may have varying definitions of

what it means to resolve an incident.

Like MTTD, MTTR varies widely by incident type, organization size and complexity, and the maturity of its

incident response processes. For example, a simple phishing incident in which a user clicks a malicious link

might be resolved in a matter of hours. A complex ransomware attack that requires system restoration from

backups could take weeks or months to resolve. Because the impact of these incidents varies significantly,

organizations can track MTTR using different categories.

• Incident type: Different incident types (e.g., malware infection, data breach, insider threat) can have

vastly different MTTRs. Tracking MTTR by incident type provides a more granular insight into response

effectiveness.

• Severity level: Incidents can be categorized by priority and severity (e.g., P0/Critical, P1/High,

P2/Medium, and P3/Low), with MTTR tracked separately for each level.

• Using percentiles: Instead of relying solely on average MTTR, organizations can track median and

percentile MTTR (e.g., 90th percentile) to better understand the distribution of response times and

identify outliers. MTTR P50/median provides insight into the typical response time, while MTTR P90

highlights the longer tail of incidents that take significantly more time to resolve.

• Time to containment vs. time to resolution: Organizations can track MTTR in stages, such as time to

containment (stopping the immediate threat) versus time to resolution (complete recovery and

validation). This provides insight into tracking different stages of the incident response process, where

containment is often a critical milestone that can prevent further damage and can be measured

separately from the overall resolution time.

MTTR is sensitive to external dependencies that the incident response team does not control. Incidents

often require action from IT operations, legal, human resources, external vendors, or law enforcement, and

the time spent waiting on these parties contributes to MTTR. For example, when the incident response

team opens a ticket with IT to reset a compromised account, the time it takes IT to perform the action

becomes part of MTTR, governed by IT’s service-level agreement (SLA) rather than by incident response

capability.

Ticketing systems typically support pausing the clock during external holds, but in practice,

teams often forget to apply these pauses, and the metric drifts from reality.

Organizations should identify which factors contribute to MTTR. That way, improvement efforts focus on

what the incident response team can influence, and external dependencies are surfaced rather than hidden

in the aggregate number.

MTTR is also a measure of response speed, not response quality. A team that closes tickets quickly without

thorough investigation can achieve a low MTTR while missing persistent threats, related systems, or root

causes. Rewarding low MTTR in isolation creates pressure to close tickets rather than to investigate them

well. Paired quality-oriented measures, described in the following sidebar, complement MTTR by capturing

thoroughness alongside speed.

Incident response teams should work with decision makers to determine the most relevant categories for

tracking and reporting MTTR. The focus should be on what provides the most actionable insight to improve

incident response effectiveness and to measure the impact of investments in tools, training, and process

improvements.

GETTING STARTED WITH INCIDENT RESPONSE METRICS

In the SANS SOC Survey 2025, author Chris Crowley notes that half the organizations surveyed do not

track MTTD or MTTR. Of those that do, 69% rely on manual or mostly manual tracking methods, such

as spreadsheets or ticketing systems, rather than automated tools. [10]

This is understandable, as many

organizations struggle to define and consistently measure these metrics, or have limited resources

(systems and human resources) to dedicate to tracking and analysis.

Even with these limitations, tracking MTTD and MTTR provides valuable data for measuring incident

response effectiveness and for justifying the resources needed to improve security operations. When

incident response teams can demonstrate concrete metrics showing detection and response times,

they can make data-driven cases for additional staff, tools, training, and process improvements.

Executive leadership and budget decision makers are more likely to respond to quantifiable data that

shows current performance, identifies gaps, and projects the impact of proposed investments.

Consider these three approaches to get started:

1. Start simple with manual tracking : Begin by tracking just a few important data points in a

spreadsheet or ticketing system. For each incident, record the timestamp when the incident

occurred (or best estimate), when it was detected, and when it was resolved. Even simple manual

tracking provides valuable baseline data that can demonstrate trends over time and justify

investments in more sophisticated tracking tools.

2. Define clear incident categories and resolution criteria : Work with the incident response team
