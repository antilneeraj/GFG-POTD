MOD = int(1e9 + 7)

class Solution:
	def numOfWays(self, n, x):
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.help(n, x, 1, dp)

    def help(self, n, x, num, dp):
        if n == 0:
            return 1
        if num > n or n < 0:
            return 0
        if dp[n][num] != -1:
            return dp[n][num]
        temp = pow(num, x)
        dp[n][num] = (self.help(n - temp, x, num + 1, dp) + self.help(n, x, num + 1, dp)) % MOD
        return dp[n][num]
