class MD5:
    def __init__(self):
        self.T = [
            0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
            0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
            0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
            0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
            0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
            0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
            0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
            0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
        ]

        self.SHIFT_AMOUNTS = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]

    def F(self, x, y, z): return (x & y) | (~x & z)
    def G(self, x, y, z): return (x & z) | (y & ~z)
    def H(self, x, y, z): return x ^ y ^ z
    def I(self, x, y, z): return y ^ (x | ~z)

    def left_rotate(self, x, amount):
        x &= 0xFFFFFFFF
        return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

    def compute(self, message):
        message_bytes = list(message.encode('utf-8'))

        # Padding
        original_bit_length = len(message_bytes) * 8
        message_bytes.append(0x80)
        while len(message_bytes) % 64 != 56:
            message_bytes.append(0)
        message_bytes += [original_bit_length & 0xFF, (original_bit_length >> 8) & 0xFF,
                          (original_bit_length >> 16) & 0xFF, (original_bit_length >> 24) & 0xFF,
                          0, 0, 0, 0]

        A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

        # Process the message in 512-bit chunks
        for i in range(0, len(message_bytes), 64):
            chunk = message_bytes[i:i + 64]
            X = [
                (chunk[j] | (chunk[j + 1] << 8) | (chunk[j + 2] << 16) | (chunk[j + 3] << 24))
                for j in range(0, 64, 4)
            ]

            AA, BB, CC, DD = A, B, C, D

            # Main loop
            for j in range(64):
                if 0 <= j < 16:
                    f = self.F(B, C, D)
                    g = j
                elif 16 <= j < 32:
                    f = self.G(B, C, D)
                    g = (5 * j + 1) % 16
                elif 32 <= j < 48:
                    f = self.H(B, C, D)
                    g = (3 * j + 5) % 16
                else:
                    f = self.I(B, C, D)
                    g = (7 * j) % 16

                temp = D
                D = C
                C = B
                B = (B + self.left_rotate(A + f + X[g] + self.T[j], self.SHIFT_AMOUNTS[j])) & 0xFFFFFFFF
                A = temp

            A = (A + AA) & 0xFFFFFFFF
            B = (B + BB) & 0xFFFFFFFF
            C = (C + CC) & 0xFFFFFFFF
            D = (D + DD) & 0xFFFFFFFF

        #  (A, B, C, D in little-endian)
        result = sum((x << (32 * i)) for i, x in enumerate([A, B, C, D]))
        return ''.join(f'{(result >> (8 * i)) & 0xFF:02x}' for i in range(16))



def generate_md5(message):
    md5_instance = MD5()
    return md5_instance.compute(message)
