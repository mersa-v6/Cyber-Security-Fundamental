# Intrusion Detection Systems (IDS)
IDS is a device or software application that monitors a network or systems for malicious activity or policy violations [ الانتهاكات ] . Any detected activity or violation is typically reported to an administrator or collected centrally using a security information and event management (SIEM) system.
### **Types of IDS**

[](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/3_Security%20devices%20and%20Tools/IPS%20%26%20IDS.md#types-of-ids)

-   **Network-based IDS (NIDS)**:

> Monitors network traffic for suspicious activity [ نشاط مشبوه ] .
> Deployed at strategic points in the network .

-   **Host-based IDS (HIDS)**

> Monitors the activities of a specific host.
> Can detect unauthorized file changes, policy violations, etc.

-   **Signature-based IDS**

> Uses predefined rules and known attack patterns (signatures) to detect threats.
> Effective against known threats but not against new, unknown threats.

-   **Anomaly-based IDS**

> Establishes a baseline of normal behavior and detects deviations from this baseline.
> Can detect unknown threats but might generate more false positives.
> 
![enter image description here](https://cdn.prod.website-files.com/5ff66329429d880392f6cba2/623d912f786507381fb32bca_IPS%20at%20work.jpg)
___
**IDSs do not substitute firewalls.** They support firewalls by providing a further layer of security protecting the network from mainstream and well-known attack vectors.
---
