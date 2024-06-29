# DHCP Protocol 
TOPIC : 
- [What is](#) 
- [Static ip](#1.Static%20ip) 
- [Dynamic ip](#2.Dynamic%20ip)
- [DORA Steps](#DORA) 
# What is
> DHCP = Dynamic host configration protocol
> 
- **DHCP** is a network management protocol used to dynamically assign IP addresses and other network configuration parameters to devices on a network, enabling them to communicate effectively.
 - **Automatic IP Assignmen**t: DHCP automates the process of IP address allocation, reducing the need for manual configuration.
  - **Efficient IP Management**: Helps in efficient utilization of IP addresses, avoiding conflicts and errors.

    `every Computer on Network Has to  have an ip address from two way:`
    # 1.Static ip
Where user     assigns a computer or device with ip address manually 
    
![enter image description here](https://www.open.edu/openlearn/pluginfile.php/1399956/mod_oucontent/oucontent/72266/55f4befe/3ee3a4db/3-2-7.small.jpg)
|**Ip address**| **192.168.1.104**|
|--|--|
|**subnet mask**  | **255.255.255.0** |
|**Default getway** |**192.168.1.1**|
|**Preferred DNS** |**1.1.1.1**|
|**Akternate DNS** |**8.8.8.8**|

# 2.Dynamic ip 
> Every device on the network will ask the DHCP server to obtain an IP address
![enter image description here](https://onlinecomputertips.com/wp-content/uploads/2021/10/bothip1.jpg)
With Dora Process 
# DORA
**D** = Discover
**O** = offer 
**R** = request 
**A** = Acknowledament 

1 .**DHCP Discover**   A client device sends a broadcast message (DHCPDISCOVER) to discover available DHCP servers.
2.   **DHCP Offer** DHCP servers respond with a DHCPOFFER message, offering an IP address and other network settings.
3. **DHCP Request** The client responds with a DHCPREQUEST message, indicating acceptance of the offered parameters.
4. **DHCP Acknowledge** The DHCP server sends a DHCPACK message, confirming the lease of the IP address and other settings.
