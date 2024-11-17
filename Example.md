## AES
### 1. Encrypt
- Input(hex): ABCDEF0123456789
- Key(hex): 1234567890123456
- Output: 5ea2b287fbc602d8d54e092573ed9ac2

### 2. Decrypt
- Cipher: 431b0757a49524bf26a55460dc97fe54
- Key(hex): 1234567890123456
- Plaintext(hex): A1B2C3D4F5A6B7C8

## DES
### 1. Encrypt
- Input(hex): ABCDEF0123456789
- Key(hex): 1234567890123456
- Output: 3430490B3DEAE4C2

### 2. Decrypt
- Cipher: 967F72CB4C224104
- Key(hex): 1234567890123456
- Plaintext(hex): A1B2C3D4F5A6B7C8

## Triple DES
### 1. Encrypt
- Input(hex): ABCDEF0123456789
- Key1(hex): 1234567890123456
- Key2(hex): ABCDEFABCDEFABCD
- Output: B8D452B703E49215

### 2. Decrypt
- Cipher: 2CD1AEBF75F4639C
- Key1(hex): 1234567890123456
- Key2(hex): ABCDEFABCDEFABCD
- Plaintext(hex): A1B2C3D4F5A6B7C8

## Blowfish
### 1. Encrypt
- Input(hex): 0123456789ABCDEF
- Key(hex): 746573746B6579
- Output: 32cf10ae3caf826a8

### 2. Decrypt
- Cipher: 1be3adeda53c67d5b
- Key(hex): 746573746B6579
- Plaintext(hex): 0x2123456123456abcd

## RC4
### 1. Encrypt
- Input: 0123456789ABCDEF
- Key: 746573746B6579
- Output: 914aae3b786b5fd733f26a3f0667fabb

### 2. Decrypt
- Cipher: AREYOUSUREDUDE?
- Key: 746573746B6579
- Plaintext: 0x2123456123456abcd

## RSA
- Should Work fine
# ElGamal
- There is an issue with elgamal frontend but code working fine in backend. You can check it using thunderclient or postman.

# MD5, SHA-256, SHA-512 works fine with any text input as far as we have tested.