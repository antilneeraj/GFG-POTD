from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, A : List[int]) -> int:
        dp = [[0, 0] for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = A[0]
        
        for i in range(1, N):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + A[i]
        
        return max(dp[N-1][0], dp[N-1][1])
