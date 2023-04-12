<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Maximum Length<br><br>

```python
from typing import List

class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        arr.sort()  # sort the entire array
        
        ans = 0
        j = n // 2
        for i in range(n // 2):
            while j < n and arr[i] >= 5 * arr[j]:
                j += 1
            ans += j - n // 2
        
        return ans
```
