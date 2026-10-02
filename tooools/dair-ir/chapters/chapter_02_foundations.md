# Chapter 2: Introduction to Modern Incident Response

Identification

Sam’s first step was to examine Jordan’s workstation. He connected remotely and checked for any running processes matching the names Jordan had described.

Listing 20 | Process Check on Jordan’s Workstation

sam@jm-workstation ~
$ ps -ef | grep -E "ms|ssupd|gilded"
sam        21847   21832  0 10:14 pts/1    00:00:00 grep --color=auto -E ms|ssupd|gilded
$ ls -la /opt/gilded/
ls: cannot access '/opt/gilded/': No such file or directory 1
$ ss -natp | grep -E "8080|9150"
$ 2
1 The SDK directory had been removed.
2 There are no processes listening on the ports.

Clean. No running processes, no SDK directory, no listening ports. Jordan had done a thorough job of removing the immediate threat. Sam noted this in his ticket and moved on to checking system logs for historical evidence. Listing 21 | System Log Review sam@jm-workstation ~

$ journalctl --since "6 days ago" | grep -i "gilded\|ssupd\|ms.*8080" Apr 07 16:34:02 jm-workstation bash[18449]: Started /bin/bash ./gilded-sdk-update --upgrade Apr 07 16:34:03 jm-workstation ms[18450]: listening on 127.0.0.1:8080 Apr 07 16:34:04 jm-workstation ssupd[18451]: opening SOCKS listener on 0.0.0.0:9150 1 Apr 07 16:41:18 jm-workstation systemd[1]: Stopped target session scope for jm (18449)

Apr 07 16:41:18 jm-workstation systemd[1]: Stopped target session scope for jm (18450)

Apr 07 16:41:18 jm-workstation systemd[1]: Stopped target session scope for jm (18451) 2
[...]
1 The ssupd process opened a SOCKS listener on port 9150
2 All three processes terminated at 16:41, consistent with Jordan’s killall command
The logs confirmed Jordan’s account. Three processes started at 16:34, all terminated at 16:41 when Jordan
killed them. Sam noted the seven-minute window between the start and termination of the process. He also
noted the SOCKS listener on port 9150, which was consistent with Tor proxy behavior. It was an interesting

detail for anonymized outbound network activity, but not the focus of his primary investigation. Sam checked the network logs for Jordan’s workstation during the seven-minute window. Listing 22 | Network Log Review

sam@jm-workstation ~

$ journalctl --since "Apr 07 16:34" --until "Apr 07 16:42" | grep -i "connect\|network\|tcp"
Apr 07 16:34:08 jm-workstation ssupd[18451]: connection established to guard relay
Apr 07 16:34:14 jm-workstation ssupd[18451]: circuit built
Apr 07 16:34:22 jm-workstation ssupd[18451]: SOCKS connection from 127.0.0.1:44892
Apr 07 16:34:24 jm-workstation curl[18465]: connected to 127.0.0.1:9150
[...]
There was some network activity during that window, but nothing currently active. Sam verified that no

outbound connections were currently established to unusual destinations. The workstation’s network activity looked normal for a developer machine: package repository connections, API traffic to cloud services, and standard browser activity. Containment

With no active malicious processes and no current network indicators, Sam assessed the containment

status. Jordan had already terminated the processes and removed the SDK. The workstation was operational and showed no signs of ongoing compromise. Sam documented his containment assessment: the threat was no longer active on the workstation, and no

additional containment actions were required at this time. He recommended that Jordan avoid reinstalling the Gilded Freight SDK until the vendor could be contacted about the suspicious components. Eradication

For eradication, Sam recommended a full malware scan of Jordan’s workstation using the organization’s

endpoint protection platform. The scan completed without findings, which was consistent with Jordan having already removed the SDK directory and all associated files. Sam checked common persistence locations to confirm nothing had been left behind.

Listing 23 | Persistence Check

sam@jm-workstation ~

$ crontab -l -u jm
no crontab for jm 1
$ ls -la /etc/systemd/system/ | grep -i "gilded\|ssupd\|ms"
$ ls -la ~/.config/autostart/ 2>/dev/null
ls: cannot access '~/.config/autostart/': No such file or directory 2
1 No scheduled tasks for Jordan’s user account
2 No autostart entries
No cron jobs, no systemd services, no Linux desktop autostart entries. The eradication was complete as far

as Sam could determine. Recovery

The workstation was already operational. Jordan had been using it for four days without issue since

removing the SDK. No recovery actions were needed. Lessons Learned

Sam closed the ticket with a professional summary. He documented the timeline, processes involved, ports

used, and actions taken. His recommendations were reasonable: • Contact the Gilded Freight vendor about the suspicious SDK components

• Review the SDK procurement process to include security review before installation

• Consider adding the process names (ms, ssupd, gilded-sdk-update) to the endpoint detection watch list

Sam marked the ticket as resolved. The documentation was thorough, the analysis was sound, and each step

of the response process had been followed. By any standard checklist, the incident had been handled. What Remained

While Sam closed the ticket, Pyrix was downloading the latest quarterly customer data export from the

sample-customer-data S3 bucket. The EC2 instance he had launched using Jordan’s credentials was still running in the NovaRise AWS account, quietly staging files for exfiltration. Jordan’s SSH keys were still valid on three internal development servers. The production database credentials harvested from nfdev-01 were still active. Sam never searched for process names, network indicators, or activity on port 9150, or activity on any other

system in the environment. He never checked whether other developers had installed the same Gilded Freight SDK. He never examined AWS CloudTrail logs for unauthorized access using Jordan’s credentials. He never investigated whether the SSH keys on Jordan’s workstation had been used from an unexpected source. Figure 6 | NovaRise Breach Investigation Gaps

Sam’s response was not careless or the result of negligence. He followed a structured process, applied

reasonable judgment at each step, and documented his work. The problem was that Sam’s PICERL-based response playbook treated the workstation as the entire incident. Once the processes were gone and the scan came back clean, the process he was following told him the work was done. Nothing in Sam’s process prompted him to ask what the attacker accomplished during the unauthorized

access. Nothing prompted Sam to check whether Jordan’s credentials had been used elsewhere, or whether the same SDK had been installed on other developer machines. The response stayed on the workstation because the response model never required him to look beyond it. A process that moves from identification to recovery in a single forward pass assumes that the visible

indicators represent the full scope of the compromise. For many attacks (from straightforward to complex), that assumption leads to an inadequate response. By the time Sam closed the ticket, the attacker’s foothold had expanded well beyond the workstation where the investigation began and ended, and the organization was none the wiser. 2 Introduction

What makes incident response meaningful is not the tools we use or the novelty of a particular exploit. It’s

not the capabilities of a forensics platform, nor the promises of bulletproof endpoint protections. It’s not the sophistication of a threat intelligence feed, nor the assurances of a managed service provider. What makes incident response meaningful is that the choices we make under pressure directly shape

outcomes. An incomplete understanding of scope can lead to confident but incorrect assurances to leadership,

regulators, and customers about the extent of the attacker’s access. A containment action taken too early or too narrowly can reveal the response to an attacker before removing their access. A rushed eradication effort can leave behind persistence mechanisms that quietly restore access to systems. Miscommunication of a recovery plan can lead to costly downtime or data loss. In incident response, how responders act matters at least as much as what they respond to. This book aims

to help readers make better decisions in those moments. Rather than focusing on a catalog of tools or one-off case studies, this book examines the process of

incident response. It explores the strategies that distinguish effective, measured responses from reactive tasks in isolation. We will explore incident response models, understand their contributions and limitations, and examine how they fare against real-world adversaries that adapt and evolve. We will look at incidents in which organizations appeared to fix the problem, only to later discover that the attacker had never truly left. We will extract the patterns behind those failures and successes, and use them to build a dynamic, iterative response approach. The goal is not to provide a script to follow, but to help readers develop the skills and judgment to adapt

their response to each incident’s unique circumstances. We will focus on the mechanics of identification, verification, and triage. We will examine scoping, containment, eradication, and recovery. We will explore how to complete these activities in a way that reduces the likelihood of re-compromise and missed impact, while mitigating the overall impact on the organization. Each chapter detailing this process concludes with Step-by-Step sections that translate concepts into actionable procedures readers can apply immediately. The path ahead requires commitment. Incident response demands continuous learning, willingness to
