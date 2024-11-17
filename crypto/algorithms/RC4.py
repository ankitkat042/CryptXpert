class RC4:
    def __init__(self, key: bytes):
        self.key = key
        self.S = self._ksa()

    def _ksa(self):
        key_length = len(self.key)
        S = list(range(256))
        j = 0

        for i in range(256):
            j = (j + S[i] + self.key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]  # Swap values in S

        return S

    def _prga(self):
        S = self.S[:]
        i = 0
        j = 0

        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # Swap values in S
            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, plaintext: bytes) -> bytes:
        keystream = self._prga()
        return bytes([p ^ next(keystream) for p in plaintext])

    def decrypt(self, ciphertext: bytes) -> bytes:
        return self.encrypt(ciphertext)  # RC4 is symmetric


# # Example Usage
# if __name__ == "__main__":
#     # Key and plaintext (both in bytes)
#     key = b"Key"
#     plaintext = b"Plaintext"
#     rc4 = RC4(key)
#     ciphertext = rc4.encrypt(plaintext)
#     print("Ciphertext (hex):", ciphertext.hex())
#     decrypted_text = rc4.decrypt(ciphertext)
#     print("Decrypted Text:", decrypted_text.decode())
