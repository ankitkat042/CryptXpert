# Secure Hash Algorithm 256 (SHA-256)

## Introduction

SHA-256 is a cryptographic hash function from the SHA-2 family, producing a 256-bit hash. It is widely used for data integrity verification and in blockchain technologies like Bitcoin.

## Features

- Produces a fixed 256-bit hash value
- One-way and collision-resistant
- Used in SSL/TLS, Bitcoin, and digital certificates

## How SHA-256 Works

1. **Pre-processing:**
   - Pad the message to make its length congruent to 448 mod 512.
   - Append the message length as a 64-bit value.
2. **Processing:**
   - Split the padded message into 512-bit blocks.
   - Initialize eight 32-bit hash values.
   - For each block:
     - Generate 64 message schedule words.
     - Perform 64 rounds of compression.
3. **Final Hash:**
   - Concatenate the eight hash values to produce a 256-bit hash.
