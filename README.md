<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Prefix Suffix String<br><br>

```python
class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        mm = {}
        for x in s1:
            temp = ""
            for i in range(len(x)):
                temp += x[i]
                mm[temp] = True
            temp = ""
            for i in range(len(x)-1, -1, -1):
                temp = x[i] + temp
                mm[temp] = True
        ans = 0
        for x in s2:
            if x in mm:
                ans += 1
        return ans        
```
