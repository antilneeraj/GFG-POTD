<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Another Coin Change Problem<br><br>

```python
class Solution:
    def makeChanges(self, N, K, target, coins):
        memo = [[-1] * (target + 1) for _ in range(K + 1)]
        
        def dp(i, j, k):
            if i == 0:
                return j == 0 and k == 0
            
            if memo[k][j] != -1:
                return memo[k][j]
            
            x = dp(i - 1, j, k)
            y = 0
            if j >= coins[i - 1] and k >= 1:
                y = dp(i, j - coins[i - 1], k - 1)
            
            memo[k][j] = x + y
            return memo[k][j]
        
        return dp(N, target, K)
```
