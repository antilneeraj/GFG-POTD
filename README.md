<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Cutting Binary Strings<br><br>

```python
class Solution:
    def cuts(self, s):
        ch = list(s)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 0  # rep ""
        
        for i in range(1, n + 1):
            j = i - 1
            if ch[j] == '0':
                dp[i] = -1  # not poss
            else:
                dp[i] = -1
                curr_ans = float("inf")
                to_dec = 0
                for k in range(i):
                    if ch[j - k] == '1':  # then only weightage counts
                        to_dec += 1 << k
                        if Solution.pow_of_5(to_dec) and dp[j - k] != -1:
                            curr_ans = min(1 + dp[j - k], curr_ans)
                if curr_ans != float("inf"):
                    dp[i] = curr_ans
        return dp[n]

    def pow_of_5(n):
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 5 != 0:
            return False
        else:
            return Solution.pow_of_5(n // 5)
```
