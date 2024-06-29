# **FireWall**

> Firewall is a network security system that monitors and controls incoming and outgoing network traffic based on
predetermined security rules. A firewall typically establishes a barrier between a trusted network and an
untrusted network, such as the Internet.
> 

> software and hardware  firewall with us called Network-based Firewall
> 

- **Key Concepts and Terms**
    - **Rules and Policies**: Define what traffic is allowed or blocked.
    - **Zones**: Logical segments within a network that help in applying specific security policies.
    - **DMZ (Demilitarized Zone)**: [ كمنطقه عازله بين الشبكه الداخليه والانترنت ]  A physical or logical subnet that separates an internal local area network (LAN) from other untrusted networks.
    - **NAT (Network Address Translation)**: Translates private IP addresses to public IP addresses and vice versa.
- **Firewall Types**
    - **Software Firewall**
        - is a piece of software installed on a persenal computer’s system in order to prdtect it from unauthorized access
        - software Firewall → host-based firewall مخصص لحمايه جهاز واحد
        - software and hardware
        - windows defender Firwall
        - iptables / nftables for linux
        - macOS firewall
    - **Packet-filtering firewalls**
        
        > is a layer 3 firewall System used to control network access by monitoring
        and controlling outgoing and incoming packets and allowing them to pass or Deny based on the source and
        destination IP addresses, protocols and ports.
        > 
        - low security
        - النوع دا بيجمع كل الباكيت وبيستخرج منها شويه حجات زي
        - ipsender و ال port number
        - بيعمل كدا حسب حاجه اسمها Also Known as Access Control List (ACL)
        - النوع دا ارخص واسهل فايروال وغالبا بيكون موجود في الراوترات بتاعت البيت
        - مشكلته انه بيركز مع الاي بي و البورت فقط بدون فحص الداتا نفسها → مبيراجعش السيشن
        - **summary**
            - **Function**: Inspect packets and either accept or reject them based on predefined rules.
            - **Pros**: Simple and fast.
            - **Cons**: Limited in functionality; cannot inspect the payload of packets.
        
    - **Stateful inspection firewalls.**
        
        > is a layers 3 and 4 firewall System that individually tracks sessions of network connections to control network access
        by monitoring and controlling outgoing and incoming packets
        > 
        - من اكبر مميزاته انه بيتعامل مع السيشن فبيقدر يجمع الباكيت ويشوف هل هي تخص نفس السيشن ولا في باكيت جايه من مصدر مختلف
        
        **How Stateful Firewall Works ?**
        
        Stateful Firewall depend on firewall's state table Concept to track the sessions, for TCP it will check the initial request
        for a connection (SYN) against its Rule, If permitted This will initiate an entry in the firewall's state table, If the
        destination host returns a packet (SYN-ACK) state table reflects this. For UDP it track state by only using the source
        and destination address and source and destination port numbers
        
        - **summary**
            - **Function**: Monitor the state of active connections and make decisions based on the context of the traffic.
            - **Pros**: More secure than packet-filtering; can track the state of connections.
            - **Cons**: More complex and resource-intensive.
    - **Application-level gateways (a.k.a. proxy, WAF)**
        - **proxy**
            
            > A proxy firewall is a network security device that serves as an intermediary between user requests and the resources they access, filtering messages and data exchange at the application layer.
            > 
            - increases security levels but can affect functionality and speed
            - **Function**: Act as an intermediary between end users and the web servers they access.
            - **Pros**: Can inspect the payload of packets; provide additional security features like content filtering.
            - **Cons**: Can introduce latency; more complex to manage
            
            ![joinhq0b.bmp](https://raw.githubusercontent.com/3laaMersa/Cyber-Security-Fundamental/main/img/joinhq0b.bmp)
            
            Type of Proxy → Forward proxy [ بتاع الشركات ] | Anonmous proxy [ بتاع الهاكرز ] | Reverse Proxy [ know as waf ]
            
            ![Untitled](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/Untitled%202.png)
            
            ![Untitled](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/Untitled%203.png)
            
            ### Proxy and SSL interception
            
            ![Untitled](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/Untitled%202.png)
            
        - **WAF**
            
            **Web Application Firewall explained**
            
            > A WAF creates a shield between a web app and the Internet; this shield can help mitigate many common attacks.
            > 
            
            > A WAF or web application firewall helps protect web applications by filtering and monitoring HTTP traffic between a web application and the Internet. It typically protects web applications from attacks such as cross-site forgery, cross-site-scripting (XSS), file inclusion, and SQL injection, among others.
            > 
            
            > A WAF is a protocol **layer 7** defense (in the OSI model), and is not designed to defend against all types of attacks. This method of attack mitigation is usually part of a suite of tools which together create a holistic defense against a range of attack vectors.
            > 
            
            ![x7ftgrsr.bmp](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/x7ftgrsr.bmp)
            
            WAF modes → Learning mode , Active mode , Passive Mode 
            
    - **Unified Threat Management (UTM) Firewalls**:
        - **Function**: Consolidate multiple security services, such as firewall, VPN, antivirus, and intrusion prevention, into a single device.
        - **Pros**: Simplified management; cost-effective.
        - **Cons**: Potential for performance issues if all services are enabled.
    - **Next-Generation Firewalls (NGFWs)**:
        - **Function**: Combine traditional firewall technology with additional features like application awareness, intrusion prevention, and advanced threat protection.
        - **Pros**: Comprehensive security features; capable of deep packet inspection.
        - **Cons**: Expensive; can be resource-intensive.
    
- **Firewall Configuration**
    - Rule Creation
    
    > قواعد السماح: تحديد حركة المرور المسموح لها بالمرور عبر جدار الحماية.
    قواعد الرفض: تحديد حركة المرور المحظورة.
    ترتيب القواعد: تتم معالجة القواعد عادةً من الأعلى إلى الأسفل؛ يتم تطبيق المباراة الأولى.
    > 
    - Default Policies
    
    > الرفض الافتراضي: يتم حظر كل حركة المرور ما لم يتم السماح بها صراحةً (مستحسن).
    السماح الافتراضي: يُسمح بجميع حركة المرور ما لم يتم رفضها صراحةً (غير مستحسن).
    > 
    - Zone Configuration
    
    > إنشاء مناطق مثل الداخلية والخارجية والمنطقة المجردة من السلاح.
    تطبيق قواعد محددة على حركة المرور بين المناطق.
    > 
    - Logging and Monitoring
    
    > تمكين التسجيل لتتبع حركة المرور المسموح بها والمحظورة.
    مراقبة السجلات بحثًا عن علامات النشاط المشبوه.
    > 
- **Tools and Technologies**
    
    Firewall Management Tools: Tools like **FireMon**, **AlgoSec**, and **Tufin** help in managing firewall rules, policies, and compliance.
    SIEM Integration: Integrate firewalls with Security Information and Event Management (SIEM) systems to correlate firewall logs with other security events.
    Automation: Use automation tools to manage and update firewall rules, especially in dynamic environments like cloud infrastructure.
    

Example of Firewall Rules

```
1. Allow HTTP/HTTPS traffic from the internal network to the internet.
2. Allow DNS queries from the internal network to the DNS server.
3. Allow SSH access from the internal network to specific servers.
4. Deny all incoming traffic from the internet to the internal network.
5. Log all dropped packets.
```
