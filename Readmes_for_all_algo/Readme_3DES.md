# Triple DES (3DES)

## Introduction

Triple DES (3DES) is an enhancement of the DES algorithm, designed to improve security by applying DES three times with either two or three keys. It increases the effective key length to 112 or 168 bits, making it resistant to brute-force attacks.



## How 3DES Works

### Encryption

1. **Key Setup:** Select two or three 56-bit keys.
2. **Triple DES Operation (EDE Mode):**
   - First Encryption: Encrypt plaintext with Key1.
   - Decryption Step: Decrypt result with Key2.
   - Second Encryption: Encrypt result with Key1.
3. Final output is the ciphertext.

### Decryption

Reverses the encryption steps:

1. Decrypt with Key1.
2. Encrypt with Key2.
3. Decrypt with Key1.

## Limitations

- Computationally intensive compared to DES.
- Being replaced by AES for modern systems.
