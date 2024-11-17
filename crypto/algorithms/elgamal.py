import random


def is_prime(n, k=128):
    """
    Miller-Rabin Primality Test to check if a number is prime.
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_safe_prime(bits):
    """
    Generate a safe prime number (p = 2q + 1, where q is also prime).
    """
    while True:
        q = random.getrandbits(bits - 1)
        q |= (1 << bits - 2) | 1
        if is_prime(q):
            p = 2 * q + 1
            if is_prime(p):
                return p


class ElGamal:
    @staticmethod
    def generate_keys(bits=256):
        """
        Generate public and private keys for ElGamal encryption.
        """
        p = generate_safe_prime(bits)
        g = 2  # For safe primes, 2 is often a primitive root
        x = random.randrange(2, p - 2)  # Private key
        y = pow(g, x, p)  # Public key
        public_key = (p, g, y)
        private_key = (p, g, x)
        return public_key, private_key

    @staticmethod
    def encrypt(plaintext, public_key):
        """
        Encrypt plaintext using the public key.
        """
        p, g, y = public_key
        m = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')
        if m >= p:
            raise ValueError("Message too large for the key size.")

        k = random.randrange(2, p - 2)
        c1 = pow(g, k, p)
        s = pow(y, k, p)
        c2 = (m * s) % p
        return [c1, c2]

    @staticmethod
    def decrypt(ciphertext, private_key):
        """
        Decrypt ciphertext using the private key.
        """
        c1, c2 = ciphertext
        p, g, x = private_key
        s = pow(c1, x, p)
        s_inv = pow(s, -1, p)  # Modular inverse
        m = (c2 * s_inv) % p
        plaintext_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
        return plaintext_bytes.decode('utf-8')
