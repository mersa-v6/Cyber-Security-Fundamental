
# TCP — Transmission Control Protocol
TCP stands for Transmission Control Protocol. It is one of the core protocols of the Internet protocol suite (TCP/IP) and operates at the transport layer of the network stack. TCP provides reliable, connection-oriented communication between devices over IP-based networks.

![enter image description here](https://media.geeksforgeeks.org/wp-content/uploads/20230417045622/OSI-vs-TCP-vs-Hybrid-2.webp)
## TCP Headers

TCP headers are the additional information added to the beginning of each TCP segment to facilitate data transmission 

   **Source Port (16 bits):**
    Specifies the source port number, which identifies the application or process sending the TCP segment.
    
   **Destination Port (16 bits):**
    Indicates the destination port number, which identifies the application or process intended to receive the TCP segment.
   
   **Sequence Number (32 bits):**
    Contains a sequence number assigned to the first byte of data in the TCP segment. It helps in ordering the segments at the receiver’s end.
    
   **Acknowledgment Number (32 bits):**
    Specifies the next sequence number the sender of the TCP segment expects to receive, acknowledging the receipt of data up to that point.
    
   **Control Flags (6 bits):**
    These flags control various aspects of TCP operation. The commonly used flags include:
   - SYN (Synchronize): Used to initiate a TCP connection.
   - ACK (Acknowledgment): Confirms the receipt of data.
   - FIN (Finish): Signals the end of data transmission and initiates **connection termination.**
    - RST (Reset): Used to reset the connection when there are irrecoverable errors
    
   **Checksum (16 bits):** Contains an error-checking value calculated over the entire TCP segment, including the header and data. It helps in detecting any errors during transmission.
   ![enter image description here](https://www.pynetlabs.com/wp-content/uploads/2024/01/tcp-header-format.jpeg)
  ##  how TCP works
  Suppose you are browsing a web server using TCP. Here is a step-by-step explanation of how a TCP connection occurs:
  **1. Connection Establishment:**
 - Your web browser  Send a connection request to the web server.  
- The web server responds by acknowledging the request and agreeing to establish a connection.  
- This three-way handshake ensures synchronization and sets up initial parameters for communication.

![enter image description here](https://www.ionos.co.uk/digitalguide/fileadmin/DigitalGuide/Schaubilder/EN-tcp-verbindungsabbau.png)
**2. Data Segmentation:**
- The file you want to browsing is divided into smaller segments or packets. Let’s say the file is divided into 10 packets labeled from 1 to 10.

**3. Reliable Delivery:**
- The client starts sending the packets to the server.
- For each packet sent, the client waits for an acknowledgment (ACK) from the server.
- Upon receiving each packet, the server sends an ACK to the client to confirm successful receipt.
- If the client doesn’t receive an ACK within a certain timeframe, it re-transmits the packet.

**4. Flow Control:**
- The server manages its buffer space and signals the client about the available space.
- If the client receives a limited ACK window size, it adjusts the rate of packet transmission to match the available buffer space on the server.

**5. Connection Termination:**
- Once all the packets are successfully received, the client and server initiate a connection termination process.
- They exchange messages to ensure the completion of data transfer and agree to close the connection.
- The four-way handshake concludes the communication.
#  UDP — User Datagram Protocol
UDP stands for User Datagram Protocol. It is a connectionless, lightweight transport layer protocol within the Internet protocol suite. UDP is a simple, best-effort protocol that offers low overhead and minimal error checking, making it suitable for scenarios where speed and efficiency are prioritized over reliability.

![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXcUHIt1LfF80cfIoNEa3g-DAAqeGbXcwmdw&s)
## Features of UDP

1.  **Connectionless Communication:** UDP is a connectionless protocol, meaning that it does not establish a dedicated connection before transmitting data. It allows sending individual packets (datagrams) from the source to the destination without any prior synchronization or negotiation.
2.  **Fast and Lightweight:** UDP is designed for speed and efficiency. It operates with less protocol-related processing, making it faster and more suitable for applications that require real-time data transmission, such as audio/video streaming or real-time gaming.
3.  **Unreliable Delivery:** UDP does not guarantee the delivery of packets or the order in which they are received. It does not provide acknowledgment or retransmission mechanisms for lost or corrupted packets. Therefore, reliability and error-checking must be handled at the application layer if needed.
4.  **Datagram Size Limit:** UDP has a maximum datagram size limit, which depends on the underlying network infrastructure. It allows applications to send a fixed-size payload without fragmentation.

UDP is suitable for scenarios where low overhead, speed, and real-time communication are crucial, and the loss of some packets is acceptable. It is commonly used in applications like DNS (Domain Name System) lookups, VoIP (Voice over IP) calls, video streaming, online gaming, and other situations where timely delivery is more important than reliability.

## UDP Headers

UDP Headers are a set of fields included at the beginning of each UDP packet (datagram). The UDP header provides essential information for the UDP protocol to function correctly. Here are the main fields typically found in a UDP header:

1.  **Source Port (16 bits):**  
    Specifies the source port number, which identifies the application or process sending the UDP packet.
2.  **Destination Port (16 bits):  
    **Indicates the destination port number, which identifies the application or process intended to receive the UDP packet.
3.  **Length (16 bits):  
    **Represents the length of the UDP packet, including the header and the data, measured in bytes.
4.  **Checksum (16 bits):** Contains an error-checking value calculated over the entire UDP packet, including the header and data. It helps in detecting any errors during transmission, although UDP does not have built-in error correction mechanisms.

The UDP header is relatively simple compared to the TCP header since UDP is a lightweight, connectionless protocol. It includes the necessary information to identify the source and destination ports and the length of the packet. The checksum field allows for error detection, although error correction must be handled at the application layer if needed.

## Understanding how UDP works via an example

Suppose you want to send a message from one device (sender) to another device (receiver) using UDP. Here’s a step-by-step explanation of how the UDP communication would occur:

**1. Sender Preparation:**  
- The sender prepares the message to be sent.  
- The sender specifies the IP address and port number of the receiver to ensure the message reaches the intended destination.

**2. Message Packaging:**  
- The sender encapsulates the message within a UDP packet, also known as a datagram.  
- The sender includes the source port number and the destination port number of the receiver in the UDP header.  
- The sender calculates a checksum value based on the contents of the UDP packet, which can be used by the receiver to check for transmission errors.

**3. Packet Transmission:**  
- The sender transmits the UDP packet containing the message over the network.  
- UDP does not establish a connection before sending the packet, so it can be sent directly to the receiver without any prior synchronization.

**4. Receiver Reception:**  
- The receiver listens for incoming UDP packets on its designated port.  
- When the UDP packet arrives, the receiver extracts the message from the packet.  
- The receiver uses the source port number to identify the sender of the message.

**5. Message Processing:**  
- The receiver processes the message based on its application requirements.  
- UDP does not guarantee the order of packet delivery or reliability, so the receiver handles any necessary error detection or reordering at the application layer.
- ---

![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg0jdmAL7n0ybEKVbnQ6xWxAEPg-7y67-kjQ&s)

