# ElGamal Encryption Algorithm

## Introduction

ElGamal is an asymmetric key encryption algorithm used for secure communication.  
It is based on the Diffie-Hellman key exchange principle and operates over cyclic groups.  
ElGamal offers both encryption and digital signature capabilities. It provides security  
through the difficulty of solving the discrete logarithm problem.

---

## Features

- Asymmetric encryption: separate public and private keys.  
- Based on the discrete logarithm problem.  
- Provides both encryption and digital signature capabilities.  
- Used in cryptographic protocols like PGP and GPG.  
- Suitable for securing sensitive communications.  

---

## How ElGamal Works

### 1. Key Generation:
- Select a large prime number `p` and a generator `g` of the cyclic group `(1, 2, ..., p-1)`.  
- Choose a private key `x`, where `x` is a random integer in the range `[1, p-2]`.  
- Compute the public key as `y = g^x mod p`.  
- The public key is `(p, g, y)`, and the private key is `x`.  

---

### 2. Encryption:
To encrypt a message `M` where `M` is in the range `[1, p-1]`:
1. Choose a random integer `k`, where `k` is in the range `[1, p-2]`.  
2. Compute `c1 = g^k mod p`.  
3. Compute `c2 = (M * y^k) mod p`.  
4. The ciphertext is the pair `(c1, c2)`.  

---

### 3. Decryption:
To decrypt the ciphertext `(c1, c2)` using the private key `x`:
1. Compute the shared secret `s = c1^x mod p`.  
2. Compute the modular inverse of `s`, denoted as `s_inv mod p`.  
3. Recover the original message as `M = (c2 * s_inv) mod p`.  

---

### 4. Security:
- The security of ElGamal relies on the computational difficulty of solving the discrete logarithm problem.  
- The encryption randomness (via `k`) ensures that even the same plaintext produces different ciphertexts.  

---

## Properties of ElGamal

1. **Randomness:**  
   - Every encryption involves a random value `k`, making ciphertexts unique even for repeated plaintexts.  

2. **Public and Private Keys:**  
   - Public key `(p, g, y)`: Used for encryption.  
   - Private key `x`: Used for decryption.  

3. **Mathematical Operations:**  
   - ElGamal operates over modular arithmetic with cyclic groups to ensure computational hardness.  

---

## Applications

- Used in hybrid cryptosystems for secure message transmission.  
- Provides digital signatures in cryptographic protocols.  
- Commonly used in PGP (Pretty Good Privacy) and other security standards.  

---

## Summary

ElGamal is a robust asymmetric encryption system offering encryption and digital signatures.  
Its reliance on the discrete logarithm problem ensures strong security for cryptographic applications.  
However, it requires larger key sizes for equivalent security compared to RSA or ECC.  
