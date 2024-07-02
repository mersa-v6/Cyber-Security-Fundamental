# **IPS & IDS**

## IDS and IPS is a layer 7 Device

## أنظمة كشف التسلل (IDS)

### Intrusion Detection System (IDS)

**IDS** is a device or software application that monitors [ يراقب  ] a network or systems for malicious activity or policy violations [ الانتهاكات ] . Any detected activity or violation is typically reported to an administrator or collected centrally using a security information and event management (SIEM) system.

### **Types of IDS**

- **Network-based IDS (NIDS)**:

> Monitors network traffic for suspicious activity [ نشاط مشبوه ] .
> 
> 
> Deployed at strategic points in the network .
> 
- **Host-based IDS (HIDS)**

> Monitors the activities of a specific host.
> 
> 
> Can detect unauthorized file changes, policy violations, etc.
> 
- **Signature-based IDS**

> Uses predefined rules and known attack patterns (signatures) to detect threats.
> 
> 
> Effective against known threats but not against new, unknown threats.
> 
- **Anomaly-based IDS**

> Establishes a baseline of normal behavior and detects deviations from this baseline.
> 
> 
> Can detect unknown threats but might generate more false positives.
> 

## أنظمة منع التسلل (IPS)

Intrusion prevention systems (IPS) perform intrusion detection and then go one step ahead and stop any detected threats. 

اختصاراً لـ Intrusion Prevention System أو نظام منع التطفل ويسمي أيضاً نظام الكشف عن التسلل ومنعه وهو نظام يتم وضعه في الشبكة لمنع أي هجوم أو تسلل محتمل بناءً علي  الخصائص المعطاه للـ Host و الـ Signatures، علي عكس الـ IDS يقوم الـ IPS بإتخاذ الإجراءات اللازمة فيقوم بجمع المعلومات عنها والإبلاغ عنها ومحاولة منع ومعالجة تلك التهديدات وإيقافها.

**أنواع الـ IPS:**

1. **Network-based intrusion prevention system (NIPS):** يقوم بمراقبة الشبكة بالكامل وتحليل الـ Traffic وكشف المشبوه منه ومنعه.
2. **Host-based intrusion prevention system (HIPS):** يعمل علي مراقبة الـ Traffic الخاص بجهاز معين وتحليله وكشف المشبوه منه ومحاولة التصدي له.
3. **Network behavior analysis (NBA):** يفحص الـ Traffic الخاص بالشبكة لتحديد وكشف التهديدات التي تسبب تدفقات عالية في الشبكة كـ [**هجوم حجب الخدمة**](https://root-x.dev/blog/article/dos_attack)، وأشكال مختلفة من الـ Malwares وأنتهاكات السياسة.
4. **Wireless intrusion prevention system (WIPS):** يقوم بمراقبة الـ Traffic للشبكة اللاسلكية.

**الأستنتاج:**

1. الـ IDS لا يتم وضعه في مسار الـ Traffic فيقوم بأكتشاف التهديد والإبلاغ عنه والتنبيه لكي يتم منعه.
2. الـ IPS يتم وضعه في مسار الـ Traffic فيقوم بالكشف عنه والإبلاغ ومحاولة التصدي له أو تغيير محتواه وإسقاط الهجمات الضارة.
3. يمكن أن تعمل كلاً من أنظمة IPS و IDS معاً لتحقيق حماية كافية للتصدي للهجمات والتسلل الضار.

![0d3rt195.bmp](https://raw.githubusercontent.com/3laaMersa/Cyber-Security-Fundamental/main/img/0d3rt195.bmp)

![Untitled](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/Untitled%205.png)

# **AntiVirus**

> also known as anti-malware, is A solution that detects and prevent the different types of malware
types e.g trojan, Worm, Ransomware, etc.. based on signatures
> 

The Antivirus is works based on signature databases.
This signature is files Hash, malware code characters.
This database is periodically updated by the antivirus vendor.
The antivirus scan every file on the machine against this database.
Once file is detected the file will be removed

**Antivirus Limitation**

Easy to bypass by changing the code characters.
Not dealing with the Zero-day malware

