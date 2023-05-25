<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Expression Add Operators<br><br>

```python
class Solution:
    def addOperators(self, S, target):
        ans = []
        if S is None or len(S) == 0:
            return ans
        self.helper(ans, "", S, target, 0, 0, 0)
        return ans
    
    def helper(self, ans, path, num, target, ind, p_val, prev):    
        if ind == len(num):
            if target == p_val:
                ans.append(path)
            return
    
        for i in range(ind, len(num)):
            cur = int(num[ind:i+1])
            if ind == 0:
                self.helper(ans, path + str(cur), num, target, i + 1, cur, cur)
            else:
                self.helper(ans, path + "+" + str(cur), num, target, i + 1, p_val + cur, cur)
                self.helper(ans, path + "-" + str(cur), num, target, i + 1, p_val - cur, -cur)
                self.helper(ans, path + "*" + str(cur), num, target, i + 1, p_val - prev + prev * cur, prev * cur)
            if num[ind] == '0':
                break 
```
