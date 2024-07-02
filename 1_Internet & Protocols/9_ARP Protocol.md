# Address Resolution Protocol (ARP)
- When a packet is sent over the Internet from one device to another, it needs to know the IP and MAC address of the destination to send it properly.

- The host needs to know the MAC addresses of other network nodes,and it can learn them by using the **Address Resolution Protocol (ARP)**

- **The MAC** address is also known as the data link layer, which establishes and terminates a connection between two physically connected devices so that data transfer can take place. The IP address is also referred to as the network layer or the layer responsible for forwarding packets of data through different routers. ARP works between these layers.

  **You can check the ARP cache of your host**
  ```sh
  PS C:\Users>  arp -a
  ```
  
  

![enter image description here](https://www.fortinet.com/content/dam/fortinet/images/cyberglossary/what-is-arp.jpg)
## What Are the Types of ARP?

There are different versions and use cases of ARP. Let us take a look at a few.

### Proxy ARP

Proxy ARP is a technique by which a proxy device on a given network answers the ARP request for an IP address that is not on that network. The proxy is aware of the location of the traffic's destination and offers its own MAC address as the destination.

### Gratuitous ARP

Gratuitous ARP is almost like an administrative procedure, carried out as a way for a host on a network to simply announce or update its IP-to-MAC address. Gratuitous ARP is not prompted by an ARP request to translate an IP address to a MAC address.

### Reverse ARP (RARP)

Host machines that do not know their own IP address can use the Reverse Address Resolution Protocol (RARP) for discovery.

### Inverse ARP (IARP)

Whereas ARP uses an IP address to find a MAC address, IARP uses a MAC address to find an IP address.

## What is address resolution protocol's relationship with DHCP and DNS? How do they differ?

ARP is the process of connecting a dynamic IP address to a physical machine's MAC address. As such, it is important to have a look at a few technologies related to IP.

As mentioned previously, IP addresses, by design, are changed constantly for the simple reason that doing so gives users security and privacy. However changes on IP addresses should not be completely random. There should be rules that allocate an IP address from a defined range of numbers available in a specific network. This helps prevent issues, such as two computers receiving the same IP address. The rules are known as DHCP or [Dynamic Host Configuration Protocol ]

IP addresses as identities for computers are important because they are needed to perform an internet search. When users search for a domain name or Uniform Resource Locator (URL), they use an alphabetical name. Computers, on the other hand, use the numerical IP address to associate the domain name with a server. To connect the two, a Domain Name System (DNS) server is used to translate an IP address from a confusing string of numbers into a more readable, easily understandable domain name, and vice versa.


## What Is ARP Spoofing/ARP Poisoning Attack?

ARP spoofing is also known as ARP poison routing or ARP cache poisoning. This is a type of malicious attack in which a cyber criminal sends fake ARP messages to a target LAN with the intention of linking their MAC address with the IP address of a legitimate device or server within the network. The link allows for data from the victim's computer to be sent to the attacker's computer instead of the original destination.

ARP spoofing attacks can prove dangerous, as sensitive information can be passed between computers without the victims' knowledge. ARP spoofing also enables other forms of cyberattacks, including the following:

### Man-in-the-Middle (MTM) Attacks

A man-in-the-middle (MITM) attack is a type of eavesdropping in which the cyberattacker intercepts, relays, and alters messages between two parties—who have no idea that a third party is involved—to steal information. The attacker may try to control and manipulate the messages of one of the parties, or of both, to obtain sensitive information. Because these types of attacks use sophisticated software to mimic the style and tone of conversations—including those that are text- and voice-based—a MITM attack is difficult to intercept and thwart.

A MITM attack occurs when malware is distributed and takes control of a victim's web browser. The browser itself is not important to the attacker, but the data that the victim shares very much is because it can include usernames, passwords, account numbers, and other sensitive information shared in chats and online discussions.

Once they have control, the attacker creates a proxy between the victim and a legitimate site, usually with a fake lookalike site, to intercept any data between the victim and the legitimate site. Attackers do this with online banking and e-commerce sites to capture personal information and financial data.

### Denial-of-Service Attacks

A denial-of-service (DoS) attack is one in which a cyberattacker attempts to overwhelm systems, servers, and networks with traffic to prevent users from accessing them. A larger-scale DoS attack is known as a distributed denial-of-service (DDoS) attack, where a much larger number of sources are used to flood a system with traffic.

These types of attacks exploit known vulnerabilities in network protocols. When a large number of packets are transmitted to a vulnerable network, the service can easily become overwhelmed and then unavailable.

### Session Hijacking

Session hijacking occurs when a cyberattacker steals a user's session ID, takes over that user's web session, and masquerades as that user. With the session ID in their possession, the attacker can perform any task or activity that user is authorized to do on that network.

Authentication occurs when a user tries to gain access to a system or sign in to a restricted website or web service. The session ID is stored in a cookie in the browser, and an attacker engaged in session hijacking will intercept the authentication process and intrude in real time.

