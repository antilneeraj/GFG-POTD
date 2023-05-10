<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Total Cuts<br><br>

```python
from typing import List

class Solution:
    def totalCuts(self, N: int, K: int, A: List[int]) -> int:
        right = [0] * N
        left = [0] * N
        left[0] = A[0]
        right[N-1] = A[N-1]

        for i in range(1, N):
            left[i] = max(left[i-1], A[i])

        for i in range(N-2, -1, -1):
            right[i] = min(right[i+1], A[i])
        
        ans = 0
        for i in range(N-1):
            if left[i] + right[i+1] >= K:
                ans += 1
        
        return ans
```
