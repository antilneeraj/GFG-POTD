<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Find k-th smallest element in given n ranges<br><br>

```python
from typing import List

class Solution:
    def kthSmallestNum(self, n: int, ranges: List[List[int]], q: int, queries: List[int]) -> List[int]:
        ranges.sort()
        ans = []
        for query in queries:
            last = -1
            found = False
            for i in range(n):
                start, end = ranges[i]
                if last < end and last >= start:
                    t = end - last
                    if t >= query:
                        ans.append(last + query)
                        found = True
                        break
                    last = end
                    query -= t
                elif last < start:
                    t = end - start + 1
                    if t >= query:
                        ans.append(start + query - 1)
                        found = True
                        break
                    last = end
                    query -= t
            if not found:
                ans.append(-1)
        return ans
```
