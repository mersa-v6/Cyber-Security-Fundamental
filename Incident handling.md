# Untitled

# **Incident handling**

- **Definition**
    
    action whenever a computer or network security incident occurs 
    
    **incident** ⇒ events with negative consequences 
    
    **events** ⇒ 
    
    - system crashes ⇒ no avalibility
    - packet floods ⇒ ddos
    - Unauthorized use of system privileges
    - Unauthorized access to sentitive data
    - execution of destructive malware
- **Process**
    - **cyber kill chain → life sycle of hackers**
        - reconnaissance  = باخد فكره
        - weaponization  = اختيار النقط الضعيفه في النظام
        - delivery  = توصيل المالوير  الي الضحيه
        - exploitation = تنفيذ الاختراق
        - installation = تثبيت المالوير او ايجاد باب خلفي للهاكر عشان يقدر ياكسس النظام في اي وقت
        - command & control = استخدام النظام  المخترق في اختراق انظمه اخري
        - action on objectives  =الهدف من الاختراق زي التسريب مثلا
    - **life sycle of incident handeling**
        - preparation  تحضير
        - Identification  التعريف
        - containment   الاحتواء
        - eradication الاستئصال
        - recovery الاحتواء والتعافي
        - Lesson learned [ post incident activity ]   نشاط ما بعد الحادث
    
    **بعد معرفنا طريقه الهجوم والدفاع نبدا نفصل الدفاع** 
    
    - **Preparation**
        
        هي اول مرحله وبيكون فيها تجهيز ال soc 
        
        - employees / awereness →    تحضير الموظفين وتوزيع التاسكات ومعرفه مهارات كل الناس
        - documentation  / policy / warning banners → ايه هي الرولز و البوليسي الي هنمشي عليها وايه هي الاجرائات الي بنمشي عليها ولما يحصل مشكله هنتصرف ازاي
        - Response plan / strategy  → هنعمل ايه في حاله ان حصل اختراق او خلل
        - defensive measures / tools → ايه هي الاجهزه والسوفتوير الي شغالين بيه
    - **Identification**
        
        **Identification** involves detecting and determining an incident has occurred. This includes:
        
        - Monitoring → Continuously monitor networks, systems, and logs for signs of suspicious activity.
        - Detection Tools → use intrusion detection systems (IDS), antivirus software, and other monitoring tools.
        - Incident Reporting → enable employees to report suspected security incidents.
    - **containment**
        
         aims to limit the damage of the incident and prevent it from spreading
        
        - Short-term Containment → Implement immediate actions to isolate the affected systems (e.g., disconnecting from the network).
        - Long-term Containment → Apply more permanent measures (e.g., temporary fixes, patching vulnerabilities) to keep the threat isolated while preparing for eradication.
    - **Eradication**
        
        يعني بنبص علي اصل الموضوع من فين اي هي جزور المشكله 
        
        Eradication involves finding and removing the cause of the incident. Steps include:
        
        - identifying Root Cause → Determine how the incident occurred and its source.
        - Removing Malware → Delete malware, close vulnerabilities, and clean infected systems.
        - System Validation → Ensure that all malicious artifacts are removed and the system is free from the threat.
    - **Detection and Analysis**
        
        this step is includes everything related to detecting an incident
        
        - means of detection → sensors [FW , IDS ,Agents , Logs , etc..] يعني مصدر الانسيدينت كان ايه هل حد من التيم هو الي طلعها ولا من الفايروال وهكذا
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