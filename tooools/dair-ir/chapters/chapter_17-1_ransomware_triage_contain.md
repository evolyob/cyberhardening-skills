﻿﻿# 第 17-1 章：勒索專用劇本－雙重勒索分析、談判風險與緊急隔離

> 模組化子章節 | 隸屬來源:  (行 1 ~ 1341)

---

# Chapter 17: Specialized IR for Ransomware & Double Extortion

Use Case Documentation

Documentation should capture which AI applications have proven valuable and which have not worked well

in specific organizational environments for internal distribution. Not every AI use case succeeds in every

context. Recording what worked (and what did not) helps teams focus effort on high-value applications

rather than repeatedly attempting approaches that have already proven ineffective. This documentation

also helps new team members quickly understand organizational AI practices.

Training

Team members should understand both the capabilities and limitations of AI tools through structured

training rather than relying solely on informal experimentation. Practical exercises build intuition for

effective use. Training scenarios might include analyzing malware samples with AI assistance, generating

incident reports from investigation notes, or troubleshooting common prompt issues. Hands-on practice

reveals where AI adds value and where traditional methods remain superior.

Structured Learning Paths

Effective AI training follows a progressive structure that builds skills incrementally, a learning theory known

as scaffolding. Initial training should cover fundamental concepts: how large language models work,

common failure modes like hallucination, and basic prompt construction techniques. Intermediate training

introduces domain-specific applications such as log analysis, code review, and report generation. Advanced

training addresses complex scenarios, including multi-step analysis chains, API integration, and prompt

optimization for specialized tasks.

Organizations should not assume that general AI familiarity translates into effective security applications.

An analyst who uses AI for personal productivity may still struggle to apply it effectively to malware analysis

or threat intelligence synthesis. Security-specific training bridges this gap by demonstrating how AI

capabilities map to incident response workflows.

Practical Training Exercises

Hands-on exercises often provide the fastest route to effective learning. Consider the training scenarios

organized by skill level as shown in Table 49 . These exercises cover foundational, intermediate, and

advanced skills, helping analysts build confidence progressively.

These exercises work well in a lab environment where analysts can experiment without the

pressure of production time.

Table 49 | Suggested Training Exercises for AI-Assisted Incident Response

LEVEL EXERCISE

Foundational Provide analysts with a simple obfuscated script and have them develop prompts that

successfully decode it, comparing different prompt approaches and their results

Foundational Give analysts a set of log entries containing an obvious attack pattern and have them

craft prompts that identify the malicious activity

Foundational Have analysts generate an executive summary from a provided technical incident

report, then critique the AI output for accuracy and completeness

LEVEL EXERCISE

Intermediate Present a more complex malware sample requiring multi-stage analysis, where

analysts practice breaking the problem into sequential prompts

Intermediate Provide sanitized case notes from a real incident and have analysts generate a draft

incident report, then compare results across the team

Intermediate Have analysts create detection rules from threat intelligence reports, verifying the

rules against known-good and known-bad samples

Advanced Challenge analysts to analyze an unfamiliar log format, developing prompts that help

them understand the structure and identify anomalies

Advanced Present a scenario requiring integration of multiple data sources (logs, network

captures, memory artifacts) and have analysts develop an analysis workflow using AI

assistance at appropriate stages

Advanced Have analysts attempt to make AI produce incorrect analysis through adversarial

prompting, building intuition for verification requirements

Cross-Training Considerations

AI training should not be isolated to a specialized AI team. When only certain analysts understand AI

capabilities, the organization cannot utilize these tools consistently across all incidents. Cross-training

ensures that AI assistance is available regardless of which analyst is assigned to a case.

Consider pairing experienced AI users with analysts who are developing their skills. This mentorship

approach accelerates learning while distributing knowledge across the team. Senior analysts can share

effective prompts, demonstrate troubleshooting techniques, and help newer team members develop

intuition for when AI assistance adds value.

Technical understanding of AI models is important, but equally critical is developing the

creativity and openness to experimentation and failure that drives learning.

Structured AI training improves the organization’s overall incident response capability. Teams that build

straightforward as reasoning capabilities continue to improve. Analysts should periodically revisit prompts

that require extensive structure to determine whether simpler approaches now produce equivalent results.

Agent tool integration standards, such as MCP, are maturing, making AI integration with security tools more

accessible. Broader platform support and easier deployment will reduce the implementation burden for

MCP-connected workflows. Organizations currently unable to justify custom integration development may

find that turnkey solutions become available as the ecosystem matures. Commercial solutions will continue

to emerge that embed AI capabilities into existing security platforms, reducing the need for custom

development.

Security-focused models trained specifically for cybersecurity tasks may offer improved performance for

incident response applications.  Specialized models such as Cisco’s Foundation-sec-8b are purpose-built to

understand cybersecurity language and workflows, with claims of reduced hallucination and improved

performance on security benchmarks compared to general-purpose models of similar size. [9]

These small

language models (SLMs) may provide cost-effective alternatives to large general-purpose models for specific

security tasks in minimally resourced local hosting environments, with the trade-off of reduced versatility

outside their training domain.

The fundamental principles, however, remain stable:

• AI accelerates analysis but does not replace human judgment.

• Verification remains essential regardless of model capability.

• Organizational policies should govern what data can be shared with AI platforms.

• Documentation should reflect how conclusions were reached.

Attackers are adopting AI to accelerate their operations. Defenders who utilize AI effectively can maintain

or improve response times despite increasing attack sophistication. The goal is to identify practical AI

applications that reduce the time and effort required to protect organizational assets.

Analysts who develop fluency with AI tools, understanding both their capabilities and limitations, will be

increasingly valuable as these technologies become standard elements of security operations. The

competitive advantage goes not to teams that adopt AI first, but to teams that integrate AI thoughtfully

while maintaining the verification rigor and analytical skepticism that separate good incident response from

performance theater. Experimentation, practice, and continuous learning position teams to utilize AI effectively as capabilities continue to advance.

17 Incident Response for

Ransomware

RANSOMWARE INTRODUCTION

Ransomware represents one of the most disruptive and financially damaging incident types that

organizations face today.  This chapter addresses ransomware-specific considerations within the broader

DAIR model established in Part 2: A Dynamic Approach to Incident Response . Organizations responding to

ransomware should reference the relevant sections in Part 2 for comprehensive guidance on each response

activity, using this chapter to supplement that foundation with ransomware-specific considerations.

In this section, we’ll examine current ransomware attack trends and financial impact, distinguish between

the different categories of ransomware operations, and explore how multi-vector extortion campaigns

extend extortion pressure beyond encryption.

Ransomware Attack Trends

Ransomware (including data extortion threats) remains one of the most significant cybersecurity threats

facing organizations across all sectors. The number of data leak events, including claims of successful

attacks, has risen steadily from 2022 through the end of 2025.  Chainalysis' 2026 Crypto Crime Report notes

a 50% year-over-year increase in data leak site postings between 2024 and 2025 ( Figure 178 ). Although

victims paid ransom in fewer than 30% of reported cases in 2025, the frequency of ransomware and data

extortion events continues to increase. [1]

Even when the ransom itself is not paid, the overall financial

impact of ransomware incidents remains substantial, including the costs of business interruption, forensic

investigation, legal fees, regulatory penalties, and reputational damage.

Figure 178 | Chainalysis 2026 Crypto Crime Report

“In 2025, ransomware actors received more than $820 million in on-chain payments (an 8% decline

year-over-year (YoY) from $892 million, our updated 2024 estimate. The 2025 total is likely to approach

or exceed $900 million as we attribute more events and payments, just as our 2024 total grew from our

initial $813 million estimate this time last year.

Source: 2026 Crypto Crime Report, Chainalysis

Modern ransomware has evolved from simple encryption schemes into sophisticated multi-stage extortion

operations. The overlap between ransomware and broader cyber extortion has blurred the boundaries of

what constitutes a ransomware attack, with many campaigns now focusing primarily on data theft rather

than encryption.

Initial access methods have evolved in response to improvements in defender capabilities and endpoint

protection. Remote access mechanisms remain a persistent threat vector, with Remote Desktop Protocol

(RDP) and Remote Monitoring and Management (RMM) tools frequently appearing in ransomware

investigations. Credential attacks against exposed authentication endpoints, such as VPN services, remain

common, particularly against organizations that lack consistent multi-factor authentication requirements.

Phishing and related attacks (voice phishing, SMS phishing, etc.) remain a valuable tactic for adversaries to

harvest credentials and establish initial access. These stolen credentials are often used to subsequently

access VPN concentrators, cloud services, remote desktop systems, or other remote access portals.

Stolen credentials used for initial access may have been compromised weeks or months

before the attack, often on mobile devices, personal computers, or other hosts outside the

response team’s telemetry. The credential theft itself may have occurred entirely outside

the victim organization’s environment, leaving no evidence in organizational logs.

SIDEBAR: THE UNTRACEABLE CREDENTIAL PROBLEM

One of the most frustrating findings in ransomware investigations is identifying that attackers used

valid credentials for initial access, and yet having no idea where, when, or how those credentials were

compromised.

This happens often. The response team will identify the first authenticated session from the attacker,

trace it to a VPN or remote access portal, and confirm that the attacker used a legitimate username

and password. But the trail ends there. The credential may have been harvested months earlier

through phishing, stolen by infostealer malware on a personal device, purchased from an

underground marketplace, or obtained through any number of other means that leave no evidence in

the victim organization’s logs.

This uncertainty has practical implications:

Investigation scope : Without knowing how credentials were compromised, responders cannot

confidently close the initial access vector. The organization may implement multi-factor

authentication (MFA) on VPN access, but if credentials were stolen through a phishing campaign

targeting cloud services, additional exposure may remain.

Lessons learned limitations : Given the relevance of  Attacker-in-the-Middle (AitM) attacks that can

negate the effectiveness of MFA implementations, simple implement MFA everywhere  advice is no

longer adequate. Since AitM attacks may occur outside an organization’s security team’s purview, it is

now even more difficult to learn from successful credential-harvesting attacks.

Stakeholder communication: Executives and boards often want to know how did they get in? and how

do we prevent it from happening again?  Honest answers sometimes require acknowledging that the

initial access vector cannot be determined definitively.

When root cause analysis cannot identify the source of the credential compromise, organizations

should focus on controls that reduce the value of stolen credentials, regardless of how they were

obtained: MFA everywhere, conditional access policies, privileged access management, and

monitoring for anomalous authentication patterns. Accepting some uncertainty about initial access is

preferable to false confidence based on incomplete evidence.

Some ransomware campaigns operate without traditional command-and-control infrastructure, relying

instead on legitimate Remote Monitoring and Management (RMM) tools such as ScreenConnect, AnyDesk,

or TeamViewer for remote access. These tools can blend into enterprise environments, making detection

more difficult because the same software may be used without malicious intent by IT support teams or end

users.

The use of Initial Access Brokers (IABs) has professionalized the initial compromise phase of ransomware

operations. IABs specialize in gaining access to victim networks and then sell that access to ransomware

affiliates. This division of labor means that the time between initial compromise and ransomware

deployment can extend to weeks or months as affiliates conduct reconnaissance, escalate privileges, and

position themselves for maximum impact.  Because IABs often use stealthy techniques to maintain access

and disclose credential details only when selling access, Cyber Threat Intelligence (CTI) resources may lack

insight into the specific credentials available for an extended period.

Figure 179 | BreachStars Forum Credential Sales Post

Ransomware operators have increasingly focused on virtual infrastructure and backup systems as primary

targets. Hypervisors running VMware ESXi or similar platforms represent high-value targets because

compromising a single hypervisor can impact dozens of virtual machines. Backup servers, storage systems,

and underlying remote lights-out management (LOM) systems are targeted specifically to eliminate

recovery options before encryption begins.

Attack Differentiation

Ransomware attacks fall into several distinct categories, each requiring different response considerations.

Human-Operated Ransomware (HumOR)

Human-operated ransomware attacks are often the most sophisticated form of ransomware. Skilled

operators or affiliates actively navigate the victim network, conducting reconnaissance, escalating

privileges, and moving laterally before deploying encryption payloads. Attackers make real-time decisions

about which systems to target, how to disable security controls, and when to execute the final encryption

phase. Extended dwell times allow attackers to identify and exfiltrate high-value data, disable backup

systems, and position themselves to encrypt as much of the environment as possible.

In HumOR attacks, the increased use of AI and Large Language Models (LLMs) by threat actors is lowering

the technical barrier to entry. Tasks that previously required skilled operators, including writing convincing

social engineering lures, analyzing complex identity platform permission inheritance, identifying high-value

targets, and adapting tooling to specific environments, can now be accelerated and automated using AI. This

allows ransomware affiliates with limited technical expertise to execute campaigns that previously

demanded experienced operators, effectively expanding the pool of actors capable of conducting

sophisticated, hands-on-keyboard attacks. The practical impact on defenders is an acceleration of

ransomware campaign volume and scope without a corresponding increase in attacker skill.

Automated or Mass-Distributed Ransomware

Automated or mass-distributed ransomware campaigns prioritize volume over the precision often

associated with HumOR attacks. Automated delivery mechanisms, such as malicious email attachments or

exploit kits, infect as many systems as possible. The ransomware executes immediately upon delivery

without the reconnaissance and lateral movement characteristic of HumOR attacks. Recovery from

automated ransomware is often simpler because the scope of compromise is limited to systems directly

manipulated through the delivery mechanism.

Encryptionless Extortion

Encryptionless extortion attacks are a growing trend where attackers focus on data theft without deploying

encryption. The threat of data exposure becomes the primary coercive pressure rather than operational disruption

from encrypted systems. Some groups have shifted entirely to this model, recognizing that data theft alone

can generate ransom payments without the technical complexity of reliable encryption and decryption.

Response to encryptionless extortion emphasizes breach notification workflows, data classification to

understand exposure, and regulatory compliance considerations.

Pseudo-Ransomware and Wipers

These attacks appear to be ransomware but offer no viable path to data recovery. Attackers may demand

ransom payments, but either never intended to provide decryption keys or use destructive techniques that

make recovery impossible regardless of payment. Responders should consider the possibility that apparent

ransomware may actually be a wiper, particularly when the ransom note lacks typical negotiation details or

when early decryption attempts fail despite valid keys.

SIDEBAR: RANSOMWARE-AS-A-SERVICE (RAAS) - LOCKBIT’S AFFILIATE

OPERATION

Two significant evolutions have shaped the modern ransomware landscape: the rise of Human-

Operated Ransomware (HumOR) and the Ransomware as a Service (RaaS) business model.

RaaS has democratized ransomware attacks by providing turnkey solutions to affiliates who lack the

technical capability to develop their own ransomware. In this model, operators develop and maintain

the ransomware payload, infrastructure, and negotiation platforms. Affiliates conduct the actual

attacks, from initial access through data exfiltration and ransomware deployment. Revenue is

typically shared between operators and affiliates, with splits varying by operation but often favoring

affiliates who take on the operational risk of conducting attacks.

The May 2025 breach of LockBit’s affiliate panel provided extensive insight into the inner workings of

a mature RaaS operation. [2]

An unknown attacker defaced LockBit’s infrastructure and leaked a

MySQL database dump containing the complete backend of their affiliate program. The leaked data

revealed an operation structured like a legitimate software business, with tiered affiliate

management, standardized tooling, and formalized revenue sharing.

Figure 180 | LockBit Data Breach Defacement [104]

The affiliate panel provided a self-service platform that allowed affiliates to generate customized

ransomware payloads for Windows, Linux, and ESXi environments. Each build was logged with

victim-specific configurations, including encryption keys, target domains, and notes on the victim’s

estimated revenue to calculate ransom demands. The database contained 1,183 ransomware builds

targeting 631 unique organizations over a five-month period.

Figure 181 | LockBit RaaS Database Schema

LockBit’s affiliate management system categorized users with tags such as "verified," "pentester,"

"newbie," and "scammer," allowing operators to track affiliate reputation and performance. New

affiliates paid approximately $777 USD for panel access. The seventy-five registered affiliates operated

under a consistent 20/80 revenue split, with operators retaining 20% of each ransom payment. Top-

performing affiliates developed distinct negotiation styles, ranging from professional, businesslike

approaches to calculated coercion and intimidation.

The leaked negotiation logs revealed standardized playbooks that affiliates followed when engaging

victims. Across 208 victim conversations containing over 4,400 messages, affiliates consistently

demonstrated decryption capability by decrypting sample files before discussing payment. Ransom

demands ranged from $3,800 to $4.5 million USD, depending on the victim’s size and industry.

Despite the volume of attacks, less than 10% of negotiations resulted in payment, suggesting that

many victims either restored from backups or accepted data loss rather than paying.

Multi-Vector Extortion Campaigns

Early ransomware families focused almost exclusively on encrypting data and demanding payment for

decryption. Modern groups have evolved into broader extortion operations that apply pressure for payment

across multiple channels simultaneously. In these multi-vector campaigns, encryption is only one part of a

broader strategy that may include data theft, data leaks, distributed denial-of-service (DDoS) attacks, and

direct harassment of executives, employees, customers, or regulators, as shown in Table 50. These tactics

all have potentially significant negative impacts on the organization, and can be combined in various ways to

increase pressure for payment and maximize the attacker’s coercive pressure.

Table 50 | Ransomware Extortion Strategies

ATTACK TECHNIQUE DESCRIPTION

Encryption Core tactic of ransomware to disrupt operations and pressure payment for

decryption keys.

Data Theft Attackers exfiltrate sensitive data, sometimes in conjunction with data encryption,

using the threat of public exposure as coercive pressure for payment.

Data Leaks Attackers publish stolen data on dark web leak sites or send targeted notifications

to customers, partners, or regulators to increase pressure for payment or threaten

reputational damage.

DDoS Attacks Attackers may launch DDoS attacks against the victim’s public-facing

infrastructure to extort payment, threatening prolonged service disruption if

demands are not met.

Harassment Direct contact with executives, employees, customers, or regulators through

phone calls, emails, or social media, used to apply additional pressure for payment

or to threaten reputational damage.

From an incident response perspective, this changes the problem from systems are encrypted  to the

organization is being coerced on several fronts simultaneously.  Encryption may be complete, partial, or

absent; the real coercive pressure often comes from the attacker’s ability to threaten business relationships,

regulatory exposure, and public reputation in a combined assault, as shown in Figure 182.

Figure 182 | Multi-Vector Extortion Campaign Tiers

Multi-vector extortion has several practical implications for organizations:

• Preparation should explicitly account for extortion beyond encryption, including data classification and

mapping for rapid impact assessment, understanding legal and regulatory obligations for potential leaks,

and establishing communication strategies for customers, partners, and regulators.

• Detection efforts need to address both technical and information impacts: determining what data was

accessed or exfiltrated is as important as understanding which systems were encrypted.

• Scoping should evaluate business impact across operational disruption, data exposure, and reputational

risk.

• Response actions frequently require close coordination with legal, communications, and executive

leadership to balance technical containment with the timing and content of public and private

communications.

Recognizing ransomware as one component of a broader extortion attack helps teams frame decisions

appropriately. It also underscores the need for response playbooks, tabletop exercises, and policies that

integrate technical, legal, and business perspectives to build a comprehensive defense strategy.

Modern ransomware response extends beyond restoring encrypted systems.

Organizations should prepare for coordinated pressure across technical, legal,

reputational, and regulatory fronts simultaneously.

In the sections that follow, we’ll address ransomware-specific considerations within each waypoint of the

DAIR model with recommendations for organizations working to improve their response capabilities.

PREPARE

Preparation is the most effective phase for reducing ransomware impact. Organizations with robust

preparation can recover more quickly, limit business disruption, and avoid the worst outcomes that

ransomware can inflict. Investments made before an incident occurs pay dividends when a response

becomes necessary.

This bears repeating: Preparation is the most effective phase for reducing ransomware

impact. Response efforts following ransomware incidents are complex, time-consuming,

and costly. Investing the time and resources to prepare thoroughly before an incident

occurs is the best way to limit the damage ransomware can cause.

General incident response preparation is covered in Prepare Activity. This section addresses ransomware-

specific preparation considerations that supplement baseline incident response readiness.

In this section, we’ll work through the preparation areas most relevant to ransomware: establishing crisis

communications capabilities and applying threat intelligence to anticipate attacker behavior. We’ll also

examine opportunities for employee training to recognize social engineering, steps to harden identity and

tier-0 systems against the privileged access that ransomware operators rely on, and approaches for

architecting backups to survive an attacker who has gained privileged admin credentials.

Crisis Communications and Public Relations

Ransomware incidents generate immediate and sustained communication demands that few organizations

are prepared to handle. Organizations should establish crisis communications capabilities before an

incident occurs, either through an internal communications team with incident response experience or

through a retainer agreement with an external crisis communications firm. Waiting until ransomware is

actively encrypting systems to identify a PR partner or draft a holding statement leaves the organization

reactive when controlled messaging matters most.

The speed at which information escapes organizational control during ransomware incidents is a recurring

problem. When ransom notes appear on hundreds or thousands of systems simultaneously, employees

across every department become aware of the attack within minutes. Social media posts, messages to

friends and family, and direct contacts with journalists can put the incident into public view long before the

response team has assessed the situation or leadership has approved any messaging. Organizations that lack

pre-approved holding statements and designated spokespersons find themselves reacting to media

coverage rather than shaping the narrative.

A crisis communications plan for ransomware should address:

• Pre-drafted holding statements that can be quickly adapted to specific circumstances.

• Designating spokespersons authorized to communicate externally on behalf of the organization.

• Establishing internal communication channels and procedures to keep employees informed and

reinforce that only authorized personnel should discuss the incident publicly.

• Escalation procedures that define when and how to engage external communications support.

• Social media monitoring to identify leaks and public discussion early.

• Coordination protocols between technical response teams, legal counsel, and communications staff.

These preparations allow organizations to respond to communication demands quickly and consistently

rather than improvising under pressure.

THE VALUE OF A GOOD HOLDING STATEMENT

A holding statement is a brief, pre-approved message that acknowledges a situation is under

investigation without committing to details that are not yet known or have not cleared legal review.

In crisis communications, the holding statement serves as the organization’s first public word when

news breaks, but facts are still being gathered. Rather than silence, which often invites speculation

and unmanaged disclosure, a holding statement gives the organization a voice in the conversation

before the full picture is clear.

Holding statements do not need to be complete or situation-specific to be useful. A statement

developed during preparation will lack the context of an actual incident. The preparation process is

an opportunity to work through questions the organization will face under pressure: What will be said

first? Who approves the message? How will the situation be characterized without overstating or

understating impact? Working through these questions before an incident allows communications

teams, legal counsel, and leadership to reach alignment without the urgency of an active campaign

and the risk that employees or the press will define the narrative first.

Even template language with placeholder details, such as "We are aware of a technical issue affecting

some of our systems and are actively investigating," provides meaningful value during the first hours

of response. It gives designated spokespersons something to work with immediately that aligns with

the organization’s needs and policies, and limits the negative impact of silence or unapproved

messaging that can occur when employees or the press fill the communication void with speculation.

CTI for Ransomware

Cyber threat intelligence helps organizations prepare for ransomware by identifying current threats,

understanding attacker tactics, and recognizing gaps in defensive visibility and capability. Effective CTI

enables proactive defense by surfacing information about how ransomware groups operate before they

target the organization.

CTI for ransomware preparation should prioritize the use of tactics, techniques, and procedures (TTPs) over

generic indicators of compromise (IOCs) for detection and threat hunting. Ransomware payloads are

frequently customized for each victim organization, with custom binaries containing hardcoded ransom

notes specific to the target. File hashes and other payload-specific IOCs have limited value for proactive

defense because the indicators change with each attack. This is exemplified in the LockBit RaaS operation

discussed earlier, where each affiliate-generated build produced unique binaries for each victim, as shown

in Listing 140. TTPs, by contrast, remain more consistent across campaigns and provide durable foundations

for detection and hunting.

Listing 140 | LockBit RaaS Database Victim Build Statistics

mysql> SELECT DATABASE();

+--------------+

| DATABASE()   |

+--------------+

| paneldb_dump |

+--------------+

1 row in set (0.00 sec)

mysql> SELECT COUNT(*) AS "Total Builds", COUNT(DISTINCT company_website) AS "Unique Orgs" FROM

builds;

+--------------+-------------+

| Total Builds | Unique Orgs |

+--------------+-------------+

|         1183 |         631 |

+--------------+-------------+

1 row in set (0.01 sec)

Consider a common tactic: ransomware groups consistently target backup-deletion mechanisms in their

campaigns to eliminate recovery options, using tools like vssadmin, wbadmin, and bcdedit. Building detection

capabilities around the unexpected execution of these commands is more valuable than tracking specific

malware hashes that change with each attack tool build.

Ransomware payloads are customized for each victim, making file hashes and other

payload-specific IOCs short-lived. Focus detection engineering on attacker behaviors and

techniques that remain consistent across campaigns.

Important CTI sources for ransomware intelligence include:

• Government advisories from CISA, FBI, and international partners that provide detailed technical

analysis of active ransomware groups.

• Industry-specific ISACs that share threat information relevant to particular sectors.

• Commercial threat intelligence feeds that track ransomware group activity, infrastructure, and evolving

techniques.

• Open-source intelligence from security researchers, vendor blogs, and community threat tracking

projects.

Ransomware operators rapidly adapt their tactics in response to defensive improvements. Where

conventional IOCs remain valuable for broad threat awareness, TTP-focused CTI provides more actionable

insights for ransomware defenses.

Employee Training and Awareness

Employee training is a critical defense against social engineering and phishing attacks that often initiate

ransomware campaigns. Most ransomware infections begin with human interaction, whether clicking a

malicious link, opening a malicious attachment, or responding to a convincing impersonation attempt.

Effective training helps employees recognize important indicators of phishing attempts:

• Urgent or emotionally manipulative language designed to bypass careful consideration.

• Claims of dire consequences for not responding immediately.

• Requests for personal information, credentials, or financial data.

• Untrusted or shortened URLs that obscure the actual destination.

• Slight misspellings in email addresses or domain names (e.g., "amazan.com" instead of "amazon.com").

• Unexpected communications that do not align with normal business processes.

AI-generated content has improved the quality of phishing campaigns, making grammatical and stylistic

errors less reliable as indicators. Attackers without native-language skills or cultural knowledge can now

generate convincing messages that would previously have contained obvious tells. Training should

emphasize verification procedures and reporting mechanisms rather than relying solely on employees to

identify sophisticated deception.

Help desk impersonation has emerged as a particularly effective social engineering technique. Employees

should understand organizational policies regarding remote support sessions, particularly whether help

desk staff will ever request the installation of remote access tools or ask for credentials. Organizations

should clearly communicate that legitimate support staff will not request password disclosure or installation

of unfamiliar software.

Training programs should emphasize regular, ongoing engagement rather than annual compliance

exercises. Training programs are not effective when they are not engaging or when employees view them as

formalities that they click through as quickly as possible. Simulated phishing campaigns should test

recognition and reporting behavior to obtain data on resilience to these attacks and practices to follow

organizational policies.

Metrics that track reporting rates, click rates, and time-to-report help security teams identify which

departments or roles need additional attention. Clear reporting mechanisms that employees understand are

valuable when they encourage prompt escalation of suspicious activity. Feedback loops that inform

employees about the outcomes of their reports reinforce vigilance and build a security-conscious culture.

When employees report suspicious emails or activity, respond promptly with

acknowledgment and next steps. Users who report potential threats should feel that their

actions are valued and lead to meaningful outcomes. When reported incidents are not

followed up on, users often become discouraged from reporting in the future.

Identity, Access, and Tier-0 Protection

Ransomware operators rarely begin by deploying an encryptor on a random workstation. In modern

campaigns, threat actors attempt to take control of the organization’s identity and administration layer so

they can push ransomware everywhere, destroy recovery options, and resist containment efforts. Domain

controllers, identity providers (IdPs), remote management platforms, virtualization consoles, and backup

servers become the distribution vehicles for broad ransomware deployment.

Preparing for ransomware requires treating these components as tier-0 assets and defending them

accordingly. The goal is to make it substantially harder for attackers to obtain persistent, global

administrative control, and to ensure that the organization can still operate if its primary identity systems

are disrupted or untrusted.

Domain controllers, identity providers, backup servers, and virtualization platforms are the

systems attackers use to push ransomware everywhere at once. Protecting these tier-0

assets limits the attacker’s ability to achieve widespread encryption with greater ease.

Important preparations include:

• Hardening domain controllers, IdPs, and key admin platforms such as remote management tools,

virtualization platforms, and backup servers. These systems should have minimal internet exposure,

tight network segmentation, and aggressive patching practices.

• Separating administrative roles and credentials so that no single account has broad, standing privileges

across the entire organization. Use distinct admin accounts for different roles, avoid shared domain

admin accounts, and implement just-in-time privilege elevation where possible.

• Implementing strong MFA for all privileged and remote access, with preference for phishing-resistant

methods for high-value accounts.

• Monitoring for identity and privilege anomalies as early-warning indicators of compromise, including

unexpected changes to admin group membership, new high-privilege accounts, unusual logon patterns,

and modifications to IdP or federation configurations.

• Maintaining documented and tested break-glass accounts and procedures that remain usable if your

Single Sign-On (SSO)/IdP or primary directory is unavailable or cannot be trusted. These break-glass

options should use separate credentials, be stored and accessed under strong control, and be exercised

during tabletop exercises and technical tests.

When identity, access, and tier-0 systems are well protected, ransomware operators must work much

harder to reach the point where they can deploy encryptors broadly. Strong identity hygiene also improves

detection and scoping (through better visibility into privileged changes) and gives the organization more

options during containment and recovery.

Backups

Backups serve as the primary recovery mechanism for ransomware incidents, yet many organizations

discover during an attack that their backups cannot fulfill that role. Modern ransomware campaigns

explicitly target backup infrastructure, hypervisors, and storage snapshots before deploying encryption,

recognizing that eliminating recovery options increases the likelihood of ransom payment.

THE CRUSHING DISAPPOINTMENT OF ENCRYPTED BACKUPS

Few moments in ransomware response are more demoralizing than discovering that the backups an

organization invested in and relied upon are also encrypted, deleted, or otherwise unusable.

This discovery typically occurs during the frantic early hours of response. Leadership asks the

obvious question: "Can we restore from backups?" IT staff access the backup console, only to find

ransom notes in the backup repository, or discover that the backup server itself is encrypted, or

realize that the most recent clean backup is months old because attackers deleted all accessible

backups before encryption began.

The emotional impact is significant. Staff who assured leadership that "we have good backups" must

now explain why those backups cannot deliver. The organization’s primary recovery path has

evaporated, and the remaining options are all substantially worse: paying the ransom, rebuilding from

scratch, or recovering from inadequate backups.

This scenario is painfully common. Modern ransomware operators specifically target backup

infrastructure because they understand its importance. Attackers with privileged access credentials

can often access backup systems, delete or encrypt backup data, and disable backup jobs without

triggering alerts. Organizations that treat backup systems as IT infrastructure rather than as critical

security assets find themselves without recovery options.

The solution is not simply "better backups." The solution is a backup architecture designed under the

assumption that attackers will have privileged network access. Immutable storage, air-gapped copies,

separate authentication for backup administration, and backup integrity monitoring all address the

reality that attackers specifically target backup systems.

Organizations should validate backup resilience through tabletop exercises that include the scenario:

"The attacker has domain admin credentials. Can they destroy our backups?" If the honest answer is

yes, backup architecture requires investment before an incident forces that discovery under worse

circumstances.

Ransomware-Resistant Backup Strategies

Effective backup strategies for ransomware resilience assume that attackers will have privileged access to

the production environment. The question is not whether backups exist, but whether those backups can

survive an attacker with domain administrator or other privileged credentials.

Start with the direction of data flow. Pull-based backup architectures, where backup systems retrieve data

from production, are more resilient than push-based models. When production systems push to backup

storage, a compromised system can overwrite or delete existing backups. Pull-based systems initiate

connections from the backup infrastructure, limiting what compromised production systems can reach.

Network isolation reinforces this protection. Backup infrastructure should be accessible only through

dedicated management networks or specialized agents, not directly reachable from potentially

compromised production systems. Attackers who compromise a workstation or even a domain controller

should not have a network path to backup storage.

Immutability provides protection even when attackers reach backup systems.  Write-once-read-many

(WORM) configurations and immutability guarantees prevent modification or deletion regardless of

credential compromise. An attacker who gains access to the backup console cannot delete immutable

backups before the retention period expires. Storage-layer snapshots maintained with retention policies

separate from backup software provide additional recovery points that application-level attacks cannot

reach. Snapshot-based backup approaches also support rapid restoration by accommodating faster

recovery of virtual machines or volumes, though their storage capacity requirements make them more

costly than traditional backup methods.

Air-gapped or offline copies represent the strongest protection. At least one backup copy should be

physically disconnected from networks, eliminating any possibility of remote compromise. Removable

storage libraries or systems that are powered off except during scheduled backup windows provide this

protection.

Identity separation can also limit the blast radius of credential compromise. Backup system access managed

through credentials separate from production IdP means that domain administrator credentials alone

cannot reach backup infrastructure data. Separate identity providers, dedicated local accounts, or third-

party authentication systems create this separation.

If domain administrator credentials can access backup systems, attackers with those

credentials can destroy backups before encrypting production systems. Separate backup

authentication from production identity providers to limit the access opportunity from a

compromised domain administrator account.

Hypervisor-level protection adds another layer for virtualized environments. VM snapshots and replication

managed at the hypervisor layer with separate administrative access survive attacks that compromise guest

operating systems. Some backup platforms also support replica-from-backup capabilities, where virtual

machine replicas are created directly from backup data rather than from running source systems. [3]

This

approach allows organizations to spin up critical workloads from backup data when source systems are

unavailable or untrusted, accelerating recovery of priority systems while the primary environment is being

rebuilt. Cross-cloud storage with external identity extends these protections to cloud environments,

preventing compromised on-premises credentials from reaching off-site backups authenticated through

separate identity providers.

Not all systems are equally important, and backup strategies should reflect that. Prioritizing backup

coverage and restoration testing for mission-critical systems ensures the most important workloads have

verified recovery paths before less critical systems are addressed. Attempting to restore everything

simultaneously during ransomware recovery is rarely feasible and often counterproductive. Identifying the

priority order for system recovery in advance allows teams to focus their efforts on the areas with the

highest business impact.

The 3-2-1-1-0 Backup Rule

The traditional 3-2-1 backup rule has served as a baseline for data protection, but comprehensive

preparation to defend against ransomware threats often requires an expanded strategy. The 3-2-1-1-0 rule

extends the original framework with two additions that directly address modern attack patterns: [4]

• 3 copies of data (production plus two backups).

• 2 different media types (preventing single-technology failures).

• 1 off-site copy (protecting against physical or logical site-wide events).

• 1 immutable or air-gapped copy that cannot be modified or deleted regardless of credential

compromise.

• 0 errors in backup recovery verification, confirmed through automated or scheduled restoration

testing.

The first addition, an immutable or air-gapped copy, addresses the threat that ransomware operators

specifically target backup infrastructure with compromised credentials. A backup that cannot be altered or

destroyed through network access or administrative privilege provides a recovery path that survives even a

complete domain compromise.

The second addition, zero recovery errors, shifts backup validation from assumption to verification.

Ransomware incidents compress decision timelines, and discovering that backups do not restore properly

during an active attack eliminates the primary recovery option at the worst possible moment.  Organizations

should regularly test restoration procedures, measure actual recovery times against Recovery Time

Objectives (RTO), and verify data completeness against Recovery Point Objectives (RPO). Automated

recovery verification tools can perform these checks on a scheduled basis, confirming that backups are

complete and restorable before an incident forces the question.

Ransomware recovery timelines are often substantially longer than organizations expect.

Unlike a single-system failure, ransomware can encrypt hundreds of systems

simultaneously, creating a restoration scope that can take days or weeks to work through,

even with clean backups available. Extended recovery times increase organizational

pressure to pay ransom, which is exactly why attackers target backup infrastructure in the

first place. Organizations should measure actual restoration times during testing and use

those measurements, not theoretical estimates, when setting recovery expectations with

stakeholders.

Backups Are Your Last Line of Defense

Finally, it’s important to recognize that backups function as insurance rather than prevention. Organizations

cannot rely on backup-based recovery as their primary ransomware strategy. Defense-in-depth, early

detection, and effective response remain essential even with robust backup capabilities.

VERIFY/TRIAGE

General guidance on verification and triage activities is covered in Verify and Triage Activities . This section

addresses ransomware-specific considerations for verification and triage.

In this section, we’ll examine the indicators that confirm ransomware activity, distinguish encryption-based

attacks from data theft and pure extortion, communicate uncertainty effectively to decision-makers, and

plan resources for the extended response that ransomware incidents typically require.

Ransomware Verification Indicators

Ransomware verification often occurs under compressed timelines because encryption spreads rapidly, and

additional delay can increase the impact on the organization. Unlike verification for other incident types

where analysts can take time to gather context, ransomware verification frequently happens while the

attack is still active.

Start by identifying the specific indicators that distinguish ransomware from other threats. Encrypted files

with modified extensions, ransom notes appearing across file systems, and mass file modification events in

rapid succession all point toward ransomware rather than data theft or espionage. System logs showing

widespread service disruptions, failed backup operations, or unexpected shadow copy deletions on

Windows systems further support the classification of ransomware.

Analysts should aim for early identification of the ransomware family during verification. Ransom notes

often contain identifying information, including group names, contact addresses, and payment portal URLs.

Services such as ID Ransomware allow analysts to upload ransom notes or encrypted file samples to identify

the ransomware variant. Early family identification allows responders to research known decryption

options, understand typical attacker behavior patterns, and anticipate what evidence sources may be

available.

PROTECT VICTIM IDENTIFIERS IN RANSOM NOTES

Ransom notes may include a unique victim identifier that grants access to a chat portal where the

ransomware group communicates with the victim, as shown in the example in Figure 183 . Anyone

who possesses this identifier can log in to the negotiation portal, and ransomware groups generally

cannot distinguish the victim organization from a third party using the same credentials. [5]

When employees photograph ransom notes on their screens and share them on social media, or when

responders include unsanitized ransom notes in incident reports distributed beyond the response

team, that victim identifier becomes accessible to journalists, security researchers, law enforcement,

and other threat actors. Third parties who access the negotiation portal can disrupt active

negotiations by sending messages, revealing the victim’s willingness to pay (or not pay), or provoking

the ransomware group into retaliatory action.

Figure 183 | Ransom Note with Victim Identifier

The Conti ransomware group made this risk explicit in 2021 when they announced that any victim

whose negotiation details leaked to journalists would have their stolen data published immediately,

regardless of whether negotiations were in progress. After screenshots from the JVCKenwood

negotiation appeared in media reports, Conti terminated the negotiation and disclosed the stolen

data to the public. [6]

Other groups have adopted similar policies, treating leaked negotiation details as

grounds for ending discussions and accelerating data publication.

Organizations should establish clear guidance during incident response: ransom notes and

negotiation details should be treated as confidential and shared only with authorized members of the

response team, legal counsel, and law enforcement. Employees who encounter ransom notes on their

systems should be instructed to report internally through established channels and avoid

photographing, forwarding, or posting ransom note content. Screenshots shared for investigative

purposes should have victim identifiers, chat URLs, and file paths redacted before distribution.

Treat ransom notes as confidential. Victim identifiers in ransom notes grant access to

negotiation portals, and leaked identifiers have caused ransomware groups to terminate
