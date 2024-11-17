# Rivest-Shamir-Adleman (RSA)

## Introduction

RSA is an asymmetric cryptographic algorithm developed in 1977. It is widely used for secure data transmission, digital signatures, and key exchanges. RSA's security relies on the difficulty of factoring large composite numbers.

---

## Features

- Asymmetric encryption with public/private key pairs.  
- Provides secure digital signatures and key exchange.  
- Based on computational hardness assumptions.  

---

## How RSA Works

### Key Generation:

1. Select two large prime numbers `p` and `q`.  
2. Compute `n = p * q`.  
3. Calculate Euler's Totient `phi(n) = (p - 1) * (q - 1)`.  
4. Choose a public exponent `e` such that `1 < e < phi(n)` and `gcd(e, phi(n)) = 1`.  
5. Compute the private key `d` such that `(d * e) % phi(n) = 1`.  

The public key is the pair `(n, e)`, and the private key is `d`.  

---

### Encryption:

1. Convert the plaintext to an integer `m`, where `0 <= m < n`.  
2. Compute the ciphertext `c = (m^e) % n`.  

---

### Decryption:

1. Compute the plaintext as `m = (c^d) % n`.  
2. Convert `m` back to plaintext.  

---

## Properties of RSA

1. **Public and Private Keys:**  
   - Public key `(n, e)`: Used for encryption.  
   - Private key `d`: Used for decryption.  

2. **Mathematical Hardness:**  
   - Security relies on the difficulty of factoring the large composite number `n`.  

3. **Flexibility:**  
   - Supports encryption, decryption, and digital signatures.  

---

## Applications

- Secure communication and key exchange in protocols like SSL/TLS.  
- Digital signatures for verifying data integrity and authenticity.  
- Secure email transmission (e.g., PGP).  

---

## Summary

RSA is one of the most widely used public-key cryptosystems. It ensures data confidentiality, integrity, and authenticity through mathematical operations. Its security depends on the infeasibility of factoring large composite numbers, making it a cornerstone of modern cryptography.  
