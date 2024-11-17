# Advanced Encryption Standard (AES)
> NOTE: In our implementation we have implemented AES 128 and have not implemented any modes of operation. They are for future work.
## Introduction

AES (Advanced Encryption Standard) is a symmetric key encryption algorithm widely used 
to secure sensitive data. It operates on fixed block sizes of 128 bits and supports 
key lengths of 128, 192, or 256 bits. AES is the successor of DES (Data Encryption 
Standard) and is known for its strength and efficiency.

## Features

- Symmetric block cipher with a fixed block size of 128 bits
- Supports key lengths of 128, 192, and 256 bits
- Highly secure and resistant to known cryptanalytic attacks
- Suitable for both software and hardware implementations
- Widely used in TLS, VPNs, disk encryption, and other secure protocols

## How AES Works

1. **Key Expansion:**  
   - The provided encryption key is expanded into a series of round keys 
     (10, 12, or 14 keys, depending on the key length).  
   - Each round key is derived from the original key using the Rijndael key schedule, 
     which involves byte substitution, rotation, and XOR with round constants.

2. **Initial Round (Pre-processing):**  
   - The plaintext block is XORed with the first round key.  

3. **Main Rounds (10, 12, or 14 depending on key length):**  
   - Each round consists of the following transformations:  
     - **SubBytes:** Replace each byte with a corresponding value from the S-box.  
     - **ShiftRows:** Perform a circular shift of rows in the state matrix.  
     - **MixColumns:** Perform a linear transformation on each column 
       to enhance diffusion (not applied in the final round).  
     - **AddRoundKey:** XOR the state with the current round key.  

4. **Final Round:**  
   - Similar to the main rounds, but skips the **MixColumns** step.  

5. **Output:**  
   - The final state matrix is converted back into a 128-bit ciphertext.

## AES Modes of Operation

AES is typically used in various modes of operation to encrypt data larger than 128 bits.  
Common modes include:  
- **ECB (Electronic Codebook):** Simple but insecure for repeated patterns.  
- **CBC (Cipher Block Chaining):** Introduces randomness using an initialization vector (IV).  
- **CTR (Counter):** Converts AES into a stream cipher for faster encryption.  
- **GCM (Galois/Counter Mode):** Combines encryption and authentication for data integrity.  

## Summary

AES is the gold standard for encryption due to its balance of security and performance. 
With its efficient design and ability to operate on different key lengths, it is 
a preferred choice for securing sensitive information worldwide.
