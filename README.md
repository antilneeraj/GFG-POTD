<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Make the array beautiful<br><br>

```python
from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        n = len(arr)
        lst = []
        for i in range(n):
            if len(lst) != 0 and ((lst[-1] < 0 and arr[i] >= 0) or (lst[-1] >= 0 and arr[i] < 0)):
                lst.pop()
            else:
                lst.append(arr[i])
        return lst
```
