<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Game Of Subsets<br><br>

```python
from typing import List

class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
        self.mp = [0] * 31
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(2, 31):
            if i % 4 == 0 or i % 9 == 0 or i == 25:
                continue
            mask = 0
            for j, p in enumerate(primes):
                if i % p == 0:
                    mask |= 1 << j
            self.mp[i] = mask

    def pow(self, n):
        ans, m = 1, 2
        while n != 0:
            if n & 1 == 1:
                ans = (ans * m) % self.mod
            m = (m * m) % self.mod
            n >>= 1
        return ans

    def goodSubsets(self, n : int, arr : List[int]) -> int:
        one = 0
        dp = [0] * 1024
        cnt = [0] * 31
        dp[0] = 1
        for i in arr:
            if i == 1:
                one += 1
            elif self.mp[i] != 0:
                cnt[i] += 1
        for i in range(31):
            if cnt[i] == 0:
                continue
            for j in range(1024):
                if j & self.mp[i] != 0:
                    continue
                dp[j | self.mp[i]] = (dp[j | self.mp[i]] + dp[j] * cnt[i]) % self.mod

        ans = sum(dp) % self.mod - 1
        if one != 0:
            ans = (ans * self.pow(one)) % self.mod
        return ans
```
