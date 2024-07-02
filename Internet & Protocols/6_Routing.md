# Routing
- Network routing is the process of selecting a path across one or more networks.
- **A router is a commonly utilized Layer 3 device**
-  routing selects the paths for Internet Protocol (IP) packets to travel from their origin to their destination. These Internet routing decisions are made by specialized pieces of network hardware called routers.
![enter image description here](https://cf-assets.www.cloudflare.com/slt3lc6tev37/5biqo5wm6nM8GSmiNyiAnl/b6b5c9befeda6ba99b4380d84953de18/routing-diagram.svg)
> Routers refer to internal **routing tables** to make decisions about how to route packets along network paths.
* A routing table records the paths that packets should take to reach every destination that the router is responsible for

**How to see the Routing Table :**
- in windows:

```shell
PS C:\Users> route print
```
- in linux :
```sh
┌──(mersa_v6㉿mersav6)-[~]
└─$  ip route
```


### What are the main routing protocols?
- **IP:** The Internet Protocol (IP) specifies the origin and destination for each data packet. Routers inspect each packet's IP header to identify where to send them.
- **BGP:** The Border Gateway Protocol (BGP)  routing protocol is used to announce which networks control which IP addresses
- **OSPF:** The Open Shortest Path First (OSPF) protocol is commonly used by network routers to dynamically identify the fastest and shortest available routes for sending packets to their destination.
- **RIP:** The Routing Information Protocol (RIP) uses "hop count" to find the shortest path from one network to another
## What is a router?

A router is a piece of network hardware responsible for forwarding packets to their destinations. Routers connect to two or more IP networks or subnetworks and pass data packets between them as needed. Routers are used in homes and offices for setting up local network connections. More powerful routers operate all over the Internet, helping data packets reach their destinations.

### routing table
![enter image description here](https://cdn.ttgtmedia.com/rms/onlineimages/routing_table-f.jpg)
