# Data Encryption Standard (DES)

## Introduction

The Data Encryption Standard (DES) is a symmetric-key block cipher developed in the 1970s by IBM and later adopted as a federal standard by NIST. DES operates on 64-bit blocks of data using a 56-bit key. While once widely used, it has been largely replaced by more secure algorithms like AES due to its vulnerability to brute-force attacks.

## Features

- Symmetric-key encryption
- Operates on 64-bit data blocks
- Uses a 56-bit key
- 16 rounds of Feistel network

## How DES Works

### Encryption

1. **Initial Permutation (IP):** Rearranges the 64-bit plaintext block.
2. **Key Generation:** Generates 16 round keys from the 56-bit key.
3. **Feistel Network:**
   - Splits data into Left (L) and Right (R) halves.
   - Processes R using expansion, XOR, substitution (S-boxes), and permutation (P-box).
   - Swaps L and R halves after each round.
4. **Final Permutation (FP):** Produces the ciphertext.

### Decryption

Reverses the encryption steps, using the round keys in reverse order.

## Limitations

- Vulnerable to brute-force attacks.
- Not secure for modern cryptographic needs.
