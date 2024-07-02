# Internet Protocol [ IP ]
**Tobic**
- [what is ip](#ip) 
- [ip Structure](#%20ip%20Structure)
- [what is mask](#what%20is%20musk)
- [Classful ](#Classful)
 - [LAN IP](#LAN%20IP)
- [WAN IP](#WAN%20IP) 
- [Custom mask](#Custom%20mask)
- [IPv6](#IPv6)
# what is ip
> How can we identify Computers on the Internet?

- An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.
- IP addresses are the identifier that allows information to be sent between devices on a network: they contain location information and make devices accessible for communication.
# ip Structure
- An IP address is a string of numbers separated by periods
- IP addresses are expressed as a set of four numbers — an example address might be `192.168.1.1` Each number in the set can range from 0 to 255. So, the full IP addressing range goes from `0.0.0.0` to `255.255.255.255`

- so   `32 bits`  -> `4 bytes` ->  `4 octets` 

**ip Consists of two parts**
1. Network domain (also called prefix)
2. host domain (also called suffix) 
for example IN `192.168.1.1` The prefix is `192.168.1` and the suffix is `.1`
# what is mask
**The network part (prefix) determine with the mask** 
**IP** `192.168.1.1`
**mask** `255.255.255.0`
> the mask determine with two way .. 

1. Classful
2. Class less 
# Classful
-   Class A    `255.0.0.0`
-   Class B    `255.255.0.0`
-   Class C    `255.255.255.0`
-   Class D    `multicast`
-   Class E     `for research`


![enter image description here](https://lh5.googleusercontent.com/FBRkEtffZNcj18UjQOZvv7XXiHv-n13H0YoNa9gRTtyTrm_ZKWcOC2fxY4nfFFE7xrIH-glFY-XJewwcmcoepCDWtPA1XqFj_RJbWVwLGkm53ISBlMoAfZBOfltvTe1NKYmo2tBWYZo_vvqT057sS68)
![enter image description here](https://lh5.googleusercontent.com/xjWmcUWttMTYJfEQJU7kO-BPlrPESZd16ygQgRuecRTK6N_st0RmLFqaPD3FW0ZPTVD2ujrJrV56D5HBYiomrMTtQws83Qw9-z4MIJ_bCdgcRf883DBBH9qI4npBsdR263tVBaPOc7SXkc05aOpiKfI)
# LAN IP
- **LAN IP is an attempt to reduce the number of IPs available on the Internet due to the increase in users and the lack of available IPs.**

- **This term appeared with the development of routers, which only take a unique IP address while the rest of the devices in the network take local ip address.**

# WAN IP
- **Now let us imagine that the global Internet is a large group of routers.**

- **Each router in these WAN has a completely different IP address from the others .**

- **Now we have a private address and a public address. The public address is owned by the router and is the one that goes out to the Internet to request the servers**

- **The private address is distributed by the router to all devices on the network.** 

### Let's say simple example for this process
**1. Now we imagine that there is a computer inside the LAN network that wants to go to the Google server
2. The computer sends the request to the router by IP `192.168.1.105`
3. The router takes this request and goes out to the global Internet ( WAN ) via its unique IP, which is `227.22.94.12`
4. The router goes to talk to the Google server, receives a response, and goes to the small LAN again.
5. search for ip `192.168.1.105` and send the request to it**
# Custom mask
**now we can create a custom mask to LAN **

**From equation** `2^h-2`
**where** `h` = number of hosts 
**and** `2^h` = number of ips that i need or more

***for example*** 

- I need to create LAN contain 1000 devices:
`2^h ~ 1000 `
`2^10 = 1024`
so I will write 10 zeros on right and complete the remaining 32 with one 
`11111111.11111111.11111100.00000000`
Convert a binary number to a decimal number and we get the subnet 
`255.255.252.0`
> note : the ip 127.0.0.1 is for loopback 
# IPv6
- IPv6 is the newest version of internet protocol formulated by the IETF, which helps identify and local endpoint systems on a computer network and route online traffic while addressing the problem of IPv4 address depletion due to prolonged internet use worldwide. This article explains how IPv6 works, its key features, and the challenges to expect during IPv6 implementation. 

-  **Consists of**  `128 bit`  `16 bytes`   `16 octets`and Displayed in hexadecimal
    -   2001:0db8:0000:0000: 0000:7a6e: 0680:9668
 ![enter image description here](https://www.fcc.gov/sites/default/files/ipv6-image1.jpg)![enter image description here](https://www.cisco.com/c/en/us/solutions/ipv6/overview/jcr:content/Grid/category_atl/layout-category-atl/blade_1808181160/bladeContents/spotlight.img.png/1629225728148.png)
