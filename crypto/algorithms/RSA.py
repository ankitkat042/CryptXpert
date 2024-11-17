import random

class RSA:
    @staticmethod
    def is_prime(n, k=5):
        if n <= 1 or n == 4:
            return False
        if n <= 3:
            return True

        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        # Witness loop
        for _ in range(k):
            a = random.randrange(2, n - 1)
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

    @staticmethod
    def generate_prime_candidate(bits):
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1
        return p

    @staticmethod
    def generate_prime_number(bits):
        while True:
            p = RSA.generate_prime_candidate(bits)
            if RSA.is_prime(p):
                return p

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = RSA.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    @staticmethod
    def modinv(e, phi):
        gcd, x, _ = RSA.extended_gcd(e, phi)
        if gcd != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % phi

    @staticmethod
    def generate_keys(key_size=512):
        key_size = int(key_size)
        # Generate two distinct large primes p and q
        p = RSA.generate_prime_number(key_size // 2)
        q = RSA.generate_prime_number(key_size // 2)
        while q == p:
            q = RSA.generate_prime_number(key_size // 2)

        n = p * q  # Modulus
        phi = (p - 1) * (q - 1)  # Euler's totient function

        # Choose public exponent e
        e = 65537  # Common choice for e
        if RSA.gcd(e, phi) != 1:
            e = random.randrange(3, phi, 2)
            while RSA.gcd(e, phi) != 1:
                e = random.randrange(3, phi, 2)

        # Compute private exponent d
        d = RSA.modinv(e, phi)

        public_key = (e, n)
        private_key = (d, n)
        return str(public_key), str(private_key)

    @staticmethod
    def encrypt(plaintext, key):
        key = "".join(key)
        e, n = eval(key)
        plaintext_bytes = plaintext.encode('utf-8')
        plaintext_int = int.from_bytes(plaintext_bytes, byteorder='big')
        if plaintext_int >= n:
            raise ValueError("Plaintext too large for the key size.")
        ciphertext_int = pow(plaintext_int, e, n)
        return str(ciphertext_int)

    @staticmethod
    def decrypt(ciphertext_int, key):
        key = "".join(key)
        d, n = eval(key)
        plaintext_int = pow(ciphertext_int, d, n)
        plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big')
        plaintext = plaintext_bytes.decode('utf-8')
        return str(plaintext)
