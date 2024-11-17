# Message Digest Algorithm 5 (MD5)

## Introduction

MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function 
that produces a 128-bit hash value. Although MD5 is considered cryptographically 
broken and unsuitable for security applications, it is still used for non-cryptographic 
purposes like checksums and data integrity verification.

## Features

- Produces a fixed 128-bit hash value  
- Fast computation  
- Widely used for checksums and data verification  
- Vulnerable to collisions and not recommended for cryptographic security  

## How MD5 Works

1. **Pre-processing:**  
   - Pad the message to make its length congruent to 448 mod 512.  
   - Append the original message length as a 64-bit value.  

2. **Processing:**  
   - Split the padded message into 512-bit blocks.  
   - Initialize four 32-bit registers (A, B, C, D).  
   - Perform 64 rounds of bitwise operations on each block using pre-defined constants 
     and functions.

3. **Final Hash:**  
   - Concatenate the resulting values of A, B, C, and D to produce a 128-bit hash.  
