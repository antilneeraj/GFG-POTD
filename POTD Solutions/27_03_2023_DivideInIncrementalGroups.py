class Solution:
    def countWaystoDivide(self, N, K):
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, K+1):
                if i < j:
                    dp[i][j] = 0
                elif j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
        return dp[N][K]