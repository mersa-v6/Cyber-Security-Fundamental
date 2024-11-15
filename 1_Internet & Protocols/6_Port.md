# Port Scanning
**So In First , What is Port ? ..........**
When you want to leave your house, you will use the door. and if someone wants to enter your house, he will enter through the door, and you are allowed him to enter or not.

 Now , **Port** do the same job as a house **door** 
 > **but with some different roles :**
 *  Each port is associated with a specific process or service .
 * Ports allow computers to easily differentiate between different kinds of traffic
 * port is **virtual point** where network connections start and end
 * Ports are software-based and managed by a computer's operating system

> **Lets go back to the First example , We Must Protect the door of the house from anyone we don't want to enter our house**


**Important ports**  also must be hidden from a user who does not have permission to access it

***[Firewall](#)  is the first man ,who prodect the ports from any unauthorized access , for example windows defender or iptables  in linux system***

 **Firewall :** is a security system that blocks or allows network traffic based on a set of security rules. Firewalls usually sit between a trusted network and an untrusted network; often the untrusted network is the Internet. For example, office networks often use a firewall to protect their network from online threats.
 
*  Some attackers try to send **malicious traffic** to random ports in the hopes that those ports have been left "**open**," meaning they are able to receive traffic. This action is somewhat like a car thief  walking down the street and trying the doors of parked vehicles, hoping one of them is unlocked. For this reason, Firewalls should be configured to **block network traffic** directed at most of the available ports.
 
* Properly configured firewalls block traffic to all ports by default except for a few predetermined ports known to be in common use. For instance,  **ports 25 (email)**, **80 (web traffic)**, **443 (web traffic**), and a few others, allowing internal employees to use these essential services, then block the rest of the **65,000+ ports.**

### What is Most popular Ports and Protocols
1. **Ports 20 and 21**: File Transfer Protocol (FTP). FTP is for transferring files between a client and a server.
2. **port 22** : The port is used for Secure Shell (SSH) communication and allows remote administration access to the VM.
3. **Port 53**: Domain Name System (DNS). DNS is an essential process for the modern Internet; it matches human-readable domain names to machine-readable IP addresses, enabling users to load websites and applications without memorizing a long list of IP addresses.
4. **Port 80:** Hypertext Transfer Protocol (HTTP). HTTP is the protocol that makes the World Wide Web possible.
5. **Port 123**: Network Time Protocol (NTP). NTP allows computer clocks to sync with each other, a process that is essential for encryption.
6. **port 161 :** Port 161 is the default port on network devices to which SNMP queries are sent during the discovery and monitoring processes.
7. **Port 179**: Border Gateway Protocol (BGP). BGP is essential for establishing efficient routes between the large networks that make up the Internet (these large networks are called autonomous systems). Autonomous systems use BGP to broadcast which IP addresses they control.
8. **Port 443**: HTTP Secure (HTTPS). HTTPS is the secure and encrypted version of HTTP. All HTTPS web traffic goes to port 443. Network services that use HTTPS for encryption, such as DNS over HTTPS, also connect at this port.
9. **Port 587**: Modern, secure SMTP that uses encryption.
10.**Port 3306** : is the default port for the classic MySQL protocol ( port ), which is used by the mysql client, MySQL Connectors, and utilities such as mysqldump and mysqlpump . 
**port 3389** : Remote Desktop Protocol (RDP) is a Microsoft proprietary protocol that enables remote connections to other computers, typically over TCP port 3389. It provides network access for a remote user over an encrypted channel.
---
### The 3 State of ports :
1. **Open** 
2. **Closed** 
3. **Filtered** =  mean the port is open but it's Filtered by Firewall 
