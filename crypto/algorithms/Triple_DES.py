
class DES:
    def __init__(self, key):
        """
        Initialize the DES object with a given key.
        """
        self.key = key
        self.rkb = []  # Round keys in binary
        self.rk = []   # Round keys in hexadecimal
        self.__generate_all_keys()

    # Permutation and shift tables
    __keyp = [57, 49, 41, 33, 25, 17, 9,
              1, 58, 50, 42, 34, 26, 18,
              10, 2, 59, 51, 43, 35, 27,
              19, 11, 3, 60, 52, 44, 36,
              63, 55, 47, 39, 31, 23, 15,
              7, 62, 54, 46, 38, 30, 22,
              14, 6, 61, 53, 45, 37, 29,
              21, 13, 5, 28, 20, 12, 4]

    __shift_table = [1, 1, 2, 2,
                     2, 2, 2, 2,
                     1, 2, 2, 2,
                     2, 2, 2, 1]

    __key_comp = [14, 17, 11, 24, 1, 5,
                  3, 28, 15, 6, 21, 10,
                  23, 19, 12, 4, 26, 8,
                  16, 7, 27, 20, 13, 2,
                  41, 52, 31, 37, 47, 55,
                  30, 40, 51, 45, 33, 48,
                  44, 49, 39, 56, 34, 53,
                  46, 42, 50, 36, 29, 32]

    __initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                      60, 52, 44, 36, 28, 20, 12, 4,
                      62, 54, 46, 38, 30, 22, 14, 6,
                      64, 56, 48, 40, 32, 24, 16, 8,
                      57, 49, 41, 33, 25, 17, 9, 1,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      61, 53, 45, 37, 29, 21, 13, 5,
                      63, 55, 47, 39, 31, 23, 15, 7]

    __exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
               6, 7, 8, 9, 8, 9, 10, 11,
               12, 13, 12, 13, 14, 15, 16, 17,
               16, 17, 18, 19, 20, 21, 20, 21,
               22, 23, 24, 25, 24, 25, 26, 27,
               28, 29, 28, 29, 30, 31, 32, 1]

    __per = [16, 7, 20, 21,
             29, 12, 28, 17,
             1, 15, 23, 26,
             5, 18, 31, 10,
             2, 8, 24, 14,
             32, 27, 3, 9,
             19, 13, 30, 6,
             22, 11, 4, 25]

    __sbox = [
        # S-box 1
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        # S-box 2
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        # S-box 3
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        # S-box 4
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        # S-box 5
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        # S-box 6
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        # S-box 7
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        # S-box 8
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]

    __final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41, 9, 49, 17, 57, 25]

    @staticmethod
    def __hex2bin(s):
        """
        Convert hexadecimal string to binary string, preserving leading zeros.
        """
        return bin(int(s, 16))[2:].zfill(len(s) * 4)

    @staticmethod
    def __bin2hex(s):
        """
        Convert binary string to hexadecimal string, preserving leading zeros.
        """
        hex_str = hex(int(s, 2))[2:].upper()
        # Pad with leading zeros to ensure correct length
        hex_len = len(s) // 4
        return hex_str.zfill(hex_len)

    @staticmethod
    def __bin2dec(binary_str):
        """
        Convert binary string to decimal integer.
        """
        return int(binary_str, 2)

    @staticmethod
    def __dec2bin(number):
        """
        Convert decimal integer to binary string.
        """
        return bin(number)[2:].zfill(4)

    @staticmethod
    def __permute(k, arr, n):
        """
        Rearrange bits of k according to the permutation table arr.
        """
        return ''.join([k[arr[i] - 1] for i in range(n)])

    @staticmethod
    def __shift_left(k, nth_shifts):
        """
        Shift bits of k to the left by nth_shifts.
        """
        return k[nth_shifts:] + k[:nth_shifts]

    @staticmethod
    def __xor(a, b):
        """
        Perform bitwise XOR between two binary strings.
        """
        return ''.join(['0' if a[i] == b[i] else '1' for i in range(len(a))])

    def __generate_all_keys(self):
        """
        Generate all round keys for encryption/decryption.
        """
        key = self.__hex2bin(self.key)
        key = self.__permute(key, DES.__keyp, 56)
        left, right = key[:28], key[28:]

        for i in range(16):
            left = self.__shift_left(left, DES.__shift_table[i])
            right = self.__shift_left(right, DES.__shift_table[i])
            combined_key = left + right
            round_key = self.__permute(combined_key, DES.__key_comp, 48)
            self.rkb.append(round_key)
            self.rk.append(round_key)

    def __encrypt_block(self, pt_bin, rkb):
        """
        Encrypt a single block of plaintext.
        """
        pt = self.__permute(pt_bin, DES.__initial_perm, 64)
        left, right = pt[:32], pt[32:]

        for i in range(16):
            right_expanded = self.__permute(right, DES.__exp_d, 48)
            xor_x = self.__xor(right_expanded, rkb[i])
            sbox_str = ''

            for j in range(8):
                row_bits = xor_x[j * 6] + xor_x[j * 6 + 5]
                col_bits = xor_x[j * 6 + 1:j * 6 + 5]
                row = self.__bin2dec(row_bits)
                col = self.__bin2dec(col_bits)
                val = DES.__sbox[j][row][col]
                sbox_str += self.__dec2bin(val)

            sbox_str = self.__permute(sbox_str, DES.__per, 32)
            result = self.__xor(left, sbox_str)
            left = result

            if i != 15:
                left, right = right, left

        combine = left + right
        cipher_text = self.__permute(combine, DES.__final_perm, 64)
        return cipher_text

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using DES algorithm.
        """
        pt_bin = self.__hex2bin(plaintext)
        cipher_bin = self.__encrypt_block(pt_bin, self.rkb)
        cipher_hex = self.__bin2hex(cipher_bin)
        return cipher_hex

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using DES algorithm.
        """
        ct_bin = self.__hex2bin(ciphertext)
        rkb_rev = self.rkb[::-1]
        plain_bin = self.__encrypt_block(ct_bin, rkb_rev)
        plain_hex = self.__bin2hex(plain_bin)
        return plain_hex

class TripleDES:
    def __init__(self, key1, key2):
        """
        Initialize the TripleDES object with two keys.
        """
        self.key1 = key1
        self.key2 = key2
        self.des1 = DES(key1)
        self.des2 = DES(key2)

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using 3DES algorithm.
        """
        # First Encryption with key1
        cipher1 = self.des1.encrypt(plaintext)
        # Decryption with key2
        cipher2 = self.des2.decrypt(cipher1)
        # Second Encryption with key1
        cipher3 = self.des1.encrypt(cipher2)
        return cipher3

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using 3DES algorithm.
        """
        # First Decryption with key1
        plain1 = self.des1.decrypt(ciphertext)
        # Encryption with key2
        plain2 = self.des2.encrypt(plain1)
        # Second Decryption with key1
        plain3 = self.des1.decrypt(plain2)
        return plain3