# Secure Hash Algorithm 512 (SHA-512)

## Introduction

SHA-512 is part of the SHA-2 family, producing a 512-bit hash value. It is designed for high-security applications and is widely used for digital signatures and data integrity verification.

## Features

- Produces a fixed 512-bit hash value
- High collision resistance
- Suitable for high-security protocols

## How SHA-512 Works

1. **Pre-processing:**
   - Pad the message to make its length congruent to 896 mod 1024.
   - Append the message length as a 128-bit value.
2. **Processing:**
   - Split the padded message into 1024-bit blocks.
   - Initialize eight 64-bit hash values.
   - For each block:
     - Generate 80 message schedule words.
     - Perform 80 rounds of compression.
3. **Final Hash:**
   - Concatenate the eight hash values to produce a 512-bit hash.
