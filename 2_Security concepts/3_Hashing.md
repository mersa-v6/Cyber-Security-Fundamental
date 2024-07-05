# Hashing 
Hashing is the process of converting data into a unique string of fixed-length characters known as a hash value or digest. Hashing is used in many security applications to ensure data integrity, identity verification, etc. Here's a detailed explanation:
___
1. ### **The concept of hashing:**

Hashing is a mathematical process that takes an input (such as a file, message, or password) and produces a fixed-length value that expresses this input. This value is called "hash value" or "digest". The basic characteristics of hashing are:

- **Generating a unique value :** Any small change in the input leads to a large change in the hash value.
- **Length consistency :**  The length is constant regardless of the size of the entrance.
- **Difficulty in returning :** The original entry from the hash value cannot be restored easily.
---

2. ### **Basic characteristics of Hashing:**

 - **Deterministic:** The same entry always gives the same hash value.
 - **Quick Computation:** Generating the hash value is very fast.
 - **Avalanche Effect:** Any small change in the entry leads to a large change in the hash value.
 - **Pre-image Resistance:** It is very difficult to find the original entry just from the hash value.
 - **Collision Resistance:** It is very difficult to find two different entries with the same hash value.
 ---

3. ###  Hashing applications:

 Storing passwords: Passwords are stored in the database in the form of hash values ​​instead of plain text.
 Digital signatures: Hash values ​​are used to create digital signatures to verify the authenticity and integrity of data.
 Data integrity: Hash values ​​are used to verify that data has not been changed during transmission.
 
 ---

4. ###  Examples of Hashing algorithms:

 **MD5 (Message Digest Algorithm 5):** Produces a hash value with a length of 128 bits. Not currently recommended due to security issues.
 **SHA-1 (Secure Hash Algorithm 1):** Produces a hash value with a length of 160 bits. Not currently recommended due to security issues.
 **SHA-256 (Secure Hash Algorithm 256):** Produces a hash value with a length of 256 bits. Part of the SHA-2 family and more secure than MD5 and SHA-1.
 SHA-3: A newer, more secure algorithm, adopted as a standard in 2015.

---
5. ###  How does Hashing work:

 **Data entry:** Original data (such as a text file) is entered.
 **Application of the algorithm:** Applying the hashing algorithm to the data to produce the hash value.
 **Use of hash value:** The hash value is used for various purposes such as verifying data integrity or verifying identity.

---
6. ### Example of using hashing in passwords:

When a user registers a new password, it is passed through the hashing algorithm to produce a hash value that is stored in the database. When the user tries to log in, the entered password is passed through the same algorithm and the resulting hash value is compared with the stored value. If they match, the password is considered correct.
