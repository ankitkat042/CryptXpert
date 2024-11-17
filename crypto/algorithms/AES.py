'''
CSE546-Applied Cryptography
Assignment 4: AES Encryption
Group Members: Ankit Bisht(2021014), Ankit Kumar(2021015)
'''
S_BOX = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 
192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 
9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 
28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

IS_BOX = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 
84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 
248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 
26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]


class AES():
    def __init__(self, key, debug=False):
        assert len(key) == 16
        self.key = key
        self.debug = debug
        self.sBox = S_BOX
        self.isBox = IS_BOX



    def multiplyWithinGaloisField(self, a, b):
        mul = 0
        for _ in range(8):
            if b & 1:
                mul ^= a
            a <<= 1
            if a & 256:
                a ^= 283
            b >>= 1
        return mul

    def arrayToMatrix(self, array):
        return [[array[4 * j + i] for j in range(4)] for i in range(4)]
    
    def matrixToArray(self, matrix):
        array = [0 for _ in range(16)]
        for i in range(4):
            for j in range(4):
                array[4 * j + i] = matrix[i][j]
        return array
    
    def keyExpansion(self, key):
        roundKeys = [[ord(i) for i in key]]
        roundConstants = [(i, 0, 0, 0) for i in (1, 2, 4, 8, 16, 32, 64, 128, 27, 54)]
        for round in range(10):
            initVector = roundKeys[-1][-4:]
            initVector.append(initVector.pop(0))
            initVector = [self.sBox[i] for i in initVector]
            initVector = [initVector[i] ^ roundConstants[round][i] for i in range(4)]
            preRoundKey = roundKeys[-1].copy()
            roundKey = []
            for _ in range(4):
                word = [preRoundKey.pop(0) for _ in range(4)]
                initVector = [initVector[i] ^ word[i] for i in range(4)]
                roundKey.extend(initVector)
            roundKeys.append(roundKey)
        return roundKeys

    def substituteBlock(self, block):
        return [self.sBox[i] for i in block]

    def shiftRows(self, block):
        shiftRowIndex = (0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11)
        return [block[shiftRowIndex[i]] for i in range(16)]

    def inverseSubstituteBlock(self, block):
        return [self.isBox[i] for i in block]

    def inverseShiftRows(self, block):
        shiftRowIndex = (0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3)
        return [block[shiftRowIndex[i]] for i in range(16)]

    def mixColumns(self, block):
        mixColumnConstant = ((2, 3, 1, 1), (1, 2, 3, 1), (1, 1, 2, 3), (3, 1, 1, 2),)
        stateMatrix = self.arrayToMatrix(block)
        newStateMatrix = [[0] * 4 for _ in range(4)]
        newStateMatrix = [[(
            self.multiplyWithinGaloisField(mixColumnConstant[i][0], stateMatrix[0][j])
            ^ self.multiplyWithinGaloisField(mixColumnConstant[i][1], stateMatrix[1][j])
            ^ self.multiplyWithinGaloisField(mixColumnConstant[i][2], stateMatrix[2][j])
            ^ self.multiplyWithinGaloisField(mixColumnConstant[i][3], stateMatrix[3][j])
        ) for j in range(4)] for i in range(4)]
        return self.matrixToArray(newStateMatrix)

    def inverseMixColumns(self, block):
        mixColumnConstant = ((14, 11, 13, 9), (9, 14, 11, 13), (13, 9, 14, 11), (11, 13, 9, 14),)
        newStateMatrix = [[0] * 4 for _ in range(4)]
        stateMatrix = self.arrayToMatrix(block)
        for i in range(4):
            newStateMatrix[i] = [(
                self.multiplyWithinGaloisField(mixColumnConstant[i][0], stateMatrix[0][j])
                ^ self.multiplyWithinGaloisField(mixColumnConstant[i][1], stateMatrix[1][j])
                ^ self.multiplyWithinGaloisField(mixColumnConstant[i][2], stateMatrix[2][j])
                ^ self.multiplyWithinGaloisField(mixColumnConstant[i][3], stateMatrix[3][j])
            ) for j in range(4)]
        return self.matrixToArray(newStateMatrix)

    def addRoundKey(self, block, roundKeys, round):
        return [block[i] ^ roundKeys[round][i] for i in range(16)]
    
    def encrypt(self, plainText):
        # print(plainText)
        # assert len(plainText) == 16
        block = [ord(i) for i in plainText]
        roundKeys = self.keyExpansion(self.key)
        block = self.addRoundKey(block, roundKeys, 0)
        # print(plainText)
        for round in range(1, 11):
            block = self.substituteBlock(block)
            block = self.shiftRows(block)
            if round < 10:
                block = self.mixColumns(block)
            block = self.addRoundKey(block, roundKeys, round)
        return "".join(f"{hex(i)[2:].zfill(2)}" for i in block)

    def decrypt(self, cipherText):
        assert len(cipherText) == 32
        block = [int(cipherText[i:i + 2], 16) for i in range(0, 32, 2)]
        roundKeys = self.keyExpansion(self.key)
        roundKeys.reverse()
        block = self.addRoundKey(block, roundKeys, 0)
        for round in range(1, 11):
            block = self.inverseShiftRows(block)
            block = self.inverseSubstituteBlock(block)
            block = self.addRoundKey(block, roundKeys, round)
            if round < 10:
                block = self.inverseMixColumns(block)
        return "".join(chr(i) for i in block)

# if __name__ == "__main__":
#     aes = AES(sys.argv[3], True)
#     if sys.argv[1] == "encrypt":
#         print((f"plain text: {sys.argv[2]}"))
#         print((f"cipher text: {aes.encrypt(sys.argv[2])}"))
#     if sys.argv[1] == "decrypt":
#         print((f"cipher text: {sys.argv[2]}"))
#         print((f"plain text: {aes.decrypt(sys.argv[2])}"))