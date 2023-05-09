MOD = 10**9 + 7

class Solution:
    def countStrings(self, N):
        matrix = [[1, 1], [1, 0]]
        res = self.matrixPower(matrix, N + 1)
        return res[0][0]

    def multiplyMatrices(self, a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] = (result[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD
        return result

    def matrixPower(self, a, n):
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = self.multiplyMatrices(result, a)
            a = self.multiplyMatrices(a, a)
            n //= 2
        return result