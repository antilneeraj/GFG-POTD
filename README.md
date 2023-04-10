<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Maximum Intersecting Lines<br><br>

```python
from collections import defaultdict

class Solution:
    def maxIntersections(self, lines, N):
        mp = defaultdict(int)
        for x in lines:
            st = x[0]
            end = x[1] + 1
            mp[st] += 1
            mp[end] -= 1

        sorted_keys = sorted(mp.keys())
        ans = 0
        curr = 0
        for key in sorted_keys:
            curr += mp[key]
            ans = max(ans, curr)

        return ans
```
