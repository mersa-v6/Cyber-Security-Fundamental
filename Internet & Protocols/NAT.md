# Network Address Translation (NAT) 
Network Address Translation (NAT) is a service that enables private IP networks to use the internet . NAT translates private IP addresses in an internal network to a public IP address before packets are sent to an external network.
![enter image description here](https://orhanergun.net/uploads/blog/thumbnail/network-address-translation-definition.jpg)
 ### How does NAT (Network Address Translation) work?

NAT is typically implemented on a router, a device that connects two networks. When a device on the private network sends data to a device on the public network, the router intercepts the data and replaces the source IP address with its own public IP address. The router then sends the data to the destination device.

When the destination device sends data back to the router, the router intercepts this data and replaces the public IP address with the original source IP address. The router then sends the data to the original source device. This process is transparent to the devices on both networks.

## WHY
1.  **IP address conservation:** By enabling multiple devices to share a single IP address, NAT helps conserve IP address space. This is especially important for organizations that have been assigned a limited number of IP addresses by their ISP.
2.  **Improved security:** NAT can provide a measure of security by hiding the internal network from the outside world. This can be useful for preventing attacks that target specific IP addresses or for preventing devices on the internal network from being accessed directly from the internet. NAT can also help prevent devices on the internal network from accessing malicious or unwanted websites.
3.  **Better speed:** NAT can improve communication speed by reducing the number of packets that need to be routed through the network. This is because NAT eliminates the need for each device on the internal network to have its own unique IP address.
4.  **Flexibility:** NAT can also be used to provide flexibility in network design, which is particularly useful for organizations that want to change their network configuration without changing their IP addresses. Organizations may want to change their network configuration to improve security or performance or to add new devices to the network.
5.  **Multi-homing:** NAT can be used to allow devices on a private network to connect to multiple public networks, a network configuration practice called multi-homing. This can be valuable for organizations that want to connect to multiple ISPs or that want to provide [failover](https://www.fortinet.com/lat/resources/cyberglossary/failover) in case one of the ISPs goes down. Multi-homing with NAT provides connection redundancy and increases uptime by allowing traffic to be routed through multiple ISPs.
6.  **Cost savings:** NAT reduces the number of IP addresses an organization needs, which can save them money on IP address licenses and other associated costs.
7.  **Easier network administration:** NAT makes it easier to manage a network by reducing the number of IP addresses that need to be assigned. This benefits organizations with a large fleet of devices and those that want to reduce the amount of time and effort required to manage their networks.

## Types of Network Address Translations (NAT)

There are three network address translation types:

### Static NAT

In static NAT, every internal IP address is mapped to a unique external IP address. This is one-to-one mapping. When outgoing traffic arrives at the router, the router replaces the destination IP address with the mapped global IP. When the return traffic comes back to the router, the router replaces the mapped global IP address with the source IP address.

Static NAT is mostly used in servers that need to be accessible from the internet, such as web servers and email servers.

### Dynamic NAT

In dynamic network address translation, internal IP addresses are mapped to a pool of external IP addresses. This is one-to-many mapping. When the outgoing traffic arrives at the router, the router replaces the destination IP address with a free global IP address from the pool. When the return traffic comes back to the router, the router replaces the mapped global IP address with the source IP address.

Dynamic NAT is mostly used in networks that need outbound internet connectivity.

### Port Address Translation (PAT)

PAT is a type of dynamic NAT that maps multiple internal IP addresses to a single external IP address via port numbers. This is many-to-one mapping. When a computer connects to the internet, the router assigns it a port number that it then appends to the computer's internal IP address, in turn giving the computer a unique IP address. When a second computer connects to the internet, it gets the same external IP address but a different port number.

PAT is mostly used in home networks.


