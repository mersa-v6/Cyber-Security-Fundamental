# **DNS 53**

> Domain Name Server (system)
> 

بما ان الاجهزه مش بتفهم غير لغه الارقام فكنا محتاجين بروسيس او برتوكول ف النص يترجم الارقام الي اسماء يسهل حفظها 

Protocol Type: Layer7 Protocol (Application Layer)
Purpose: Name to IP conversion
Structure: Hierarchical
Founder: Paul V. Mockapetris
Carrier Protocol: TCP, UDP
Port: TCP53 (for Zone Transfer), UDP53 (for DNS Queries)
Protocol Model Type: Client/Server Model

### Domain Name Types

FQDN → Fully Qualified Domain Name: Contains full name of a Host. It is
terminated by NULL string. e.g. [www.example.com](http://www.atechacademy.com/)

PQDN → Partially Qualified Domain Name: Starts from a node but doesn’t
reach Root. It is NOT terminated by NULL string e.g. www.example

---

### DNS Servers

- **dns Resolver →**

> This is for [ ISP ] Internet Service Provider companies, and this is what connects me to the dns name server
> 
- **Root name server →**

> It is 13 DNS distributed around the whole world. When someone buys a new domain, one of them is saved, and consequently the rest are automatically saved because they are one exact copy of each other.
> 
- **TLD name server ( top level domain ) →**

> What is TLD, Top level domain is a end of any domain you can see , for example [ .com , .org , .net , .gov , .info , .edu , ....] , each TLD server have all information about the TLD his own
> 
- **Authoritative name server →**

> Provide responses to queries for specific domains, containing the definitive information about domain names and their associated IP addresses.
Example: A company's DNS server hosting records for their domain (e.g., [example.com](http://example.com/)).
> 

### **DNS record**

First, if we say [example.com](http://example.com/) that is the domain
If we say [sub.example.com](http://sub.example.com/) then this is the subdomain

so what is DNS records? 

- A → Identify the IP address for Know host name (subdomains)
- AAAA → same as A record but it for IPv6
- mx → Mail servers for exchanging mail messages between sites and each other, sites and users
- cname → lets say it a subdomain alternative  to subdomain [ alias ] , for example we can open the same website from two subdomains

for ex :

 [youtube.google.com](http://youtoup.com)  is cname for → [youtube.com](http://youtoup.com) 

---

## **what is the actually process :**

now when the user open the browser and write [example.com](http://example.com) → browser send query to the OS to ask it if he cache this domain for any ip ?

if yes the process end here if not we move to next step….

> Note → The browser usually cache any field you have previously requested in files in the operating system for a specified period to speed up the process when requested again.
> 

what is the next step ? the OS used Port 53 to send request to the Resolver dns to ask him if he cache the ip for this domain name if yes the  process end here if not we move to next step…..

the Resolver dns send query to root dns to ask him for the ip for TLD server for this domain [in thes case → .com] and the root send tld ip for resolver …

the resolver send qeury to the TLD server and TLD search for ip of this domain and send it to resolver …

now resolver cache this ip and his domain for feture use and send the ip for the OS …

OS cache this ip and his domain for feture use also and open the domain in browser for the user .

![Untitled](https://github.com/3laaMersa/Cyber-Security-Fundamental/blob/main/img/Untitled.png)

### example DNS Servers :

1.1.1.1 → cloudflare

8.8.8.8 → google 
