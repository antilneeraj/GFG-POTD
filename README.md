<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Maximum Identical Bowls<br><br>

```python
from typing import List

class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        sum = 0
        for x in arr:
            sum += x
        while N > 0:
            if sum % N == 0:
                return N
            
            N -= 1

        return 0   
```
