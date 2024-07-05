# **Incident handling**

- **Definition**
    
    action whenever a computer or network security incident occurs 
    
    **incident** ⇒ events with negative consequences 
    
    **events examples** ⇒ 
    
    - system crashes ⇒ no avalibility
    - packet floods ⇒ ddos
    - Unauthorized use of system privileges
    - Unauthorized access to sentitive data
    - execution of destructive malware
- **Process**
    - **cyber kill chain → life sycle of hackers**
        - **reconnaissance**  = It is the stage of collecting information about the organization or company that the hacker wants to penetrate, for example, examining ports, determining the operating system, and collecting subdomains.
        
        - **weaponization**  = determine the vulnerability in target 
        - **delivery**  = Trying to deliver the payload to the server or the targeted victim
        - **exploitation** = Executing the malware
        - **installation** = Installing malware or creating a back door for the hacker so that he can establish the system at any time
        - **command & control** = Using the hacked system to hack other systems
        - **action on objectives** = Implementing the goal of the hack, such as leaking data
          
    - ## now what about life sycle of incident handeling
        - preparation  تحضير
        - Identification  التعريف
        - containment   الاحتواء
        - eradication الاستئصال
        - recovery الاحتواء والتعافي
        - Lesson learned [ post incident activity ]   نشاط ما بعد الحادث
    
  **After we know the method of attack and defense, we begin to separate the defense**
    
    - **Preparation**
        
        It is the first stage in which the SOC is prepared 
        
        - **employees / awereness** →    Preparing employees, distributing tasks, and knowing the skills of all people
        - **documentation  / policy / warning banners** → What are the rolls and police that we will follow, and what are the procedures that we will follow, and when a problem occurs, how will we deal with them? What are the rolls and police that we will follow, and what are the procedures that we will follow, and when a problem occurs, how will we deal?
        - **Response plan / strategy**  → What will we do if there is a hack or malfunction?
        - **defensive measures / tools** → What devices and software are exist in organization 
    - **Identification**
        
        **Identification** involves detecting and determining an incident has occurred. This includes:
        
        - **Monitoring** → Continuously monitor networks, systems, and logs for signs of suspicious activity.
        - **Detection Tools** → use intrusion detection systems (IDS), antivirus software, and other monitoring tools.
        - **Incident Reporting** → enable employees to report suspected security incidents.
    - **containment**
        
         aims to limit the damage of the incident and prevent it from spreading
        
        - Short-term Containment → Implement immediate actions to isolate the affected systems (e.g., disconnecting from the network).
        - Long-term Containment → Apply more permanent measures (e.g., temporary fixes, patching vulnerabilities) to keep the threat isolated while preparing for eradication.
    - **Eradication**
        
  let's look at the origin of the issue, where is the root of the problem        
        Eradication involves finding and removing the cause of the incident. Steps include:
        
  - identifying Root Cause → Determine how the incident occurred and its source.
    - Removing Malware → Delete malware, close vulnerabilities, and clean infected systems.
    - System Validation → Ensure that all malicious artifacts are removed and the system is free from the threat.
    - **Detection and Analysis**
        
        this step is includes everything related to detecting an incident
        
        - means of detection → sensors [FW , IDS ,Agents , Logs , etc..] what was the source of the Incident? Was it from Team that produced it, or from the firewall, and so on?
    - **Recovery**
        
        **Recovery** focuses on restoring and validating system functionality after eradication. This includes:
        
        - **Restoration →**  Restore affected systems and data from clean backups.
        - **System Testing→**  Verify that systems are functioning normally and are secure.
        - **Monitoring→**  Continue to monitor systems for any signs of the incident recurring.
    - **Lessons Learned**
        
        **Lessons Learned** is the process of reviewing and analyzing the incident to improve future responses. This involves:
        
        - **Incident Review →** Conduct a post-incident review meeting with the incident response team and stakeholders.
        - **Documentation →** Document the details of the incident, including causes, responses, and recovery efforts.
        - **Recommendations →**  Provide recommendations to improve security measures and incident response processes.
        - **Update Plans →** Update the incident response plan and other relevant policies based on the lessons learned.
