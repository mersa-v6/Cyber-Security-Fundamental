# Network in Virtual machine
**Network adapter**
- [Bridged](#Bridged)
- [Nat](#Nat)
- [Host-only](#Host-only)
# Bridged
![enter image description here](https://websistent.com/wp-content/uploads/2010/10/vmware-custom-network-adapter-vmnetcfg-300x253.png)
**The Internet treats VMs as an independent device with an IP and Mac address.  This is more secure in case the device is hacked from the network.**

**Advantages:**

-   The VM gets an IP address from the same DHCP server as the host, making it fully accessible from other machines on the network.
-   It allows the VM to communicate with any device on the physical network, just like the host.

**Use Cases:**

-   Suitable for scenarios where the VM needs to be treated as a fully independent device on the network.
-   Useful for services that need to be accessed by other devices on the network, like web servers or databases.
# Nat


 NAT creates a private network for the VM where the VM gets an IP address that is not directly visible on the external network.
    The VM accesses external networks through the host’s IP address via NAT.

Advantages:

    Provides an additional layer of security by isolating the VM from the external network.
    Easy to set up without requiring changes to the network infrastructure.

Use Cases:

    Ideal for situations where the VM needs to access the internet or external networks without being accessed from those networks.
    Suitable for client applications or when testing internet connectivity.

![enter image description here](https://www.virten.net/wp-content/uploads/2013/03/vm-nat.jpg) 
# Host-only
Host-only networking creates a private network between the host and the VMs.
    The VM can communicate only with the host and other VMs configured in the same host-only network.

Advantages:

    Provides a completely isolated network for testing and development.
    No exposure to external networks or the internet, enhancing security.

Use Cases:

    Suitable for environments where VMs need to communicate only with the host and each other.
    Ideal for isolated development and testing environments or for simulating private networks.
---
---
Additional Considerations

    Performance: Bridged networking may have better performance for network-intensive applications compared to NAT.
    Security: Host-only networking offers the highest level of isolation, while Bridged can expose the VM to the same vulnerabilities as the host.
    Configuration: Bridged networking might require configuration of network infrastructure (like routers and switches), whereas NAT and Host-only are simpler to set up.

Understanding these networking modes and choosing the appropriate one is crucial for setting up VMs to meet specific requirements for connectivity, security, and performance.
