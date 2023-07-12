class Solution:
    def power(self, N, R):
        MOD = 1000000007
        result = 1
        while R > 0:
            if R % 2 == 1:
                result = (result * N) % MOD
            N = (N * N) % MOD
            R //= 2
        return result
