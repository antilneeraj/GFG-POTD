<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Smaller Sum<br><br>

```python
from typing import List

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        cp = arr.copy()
        cp.sort()
        
        dit = {}
        pre_sum = 0
        
        for elem in cp:
            if elem not in dit:
                dit[elem] = pre_sum
            
            pre_sum += elem
        
        ans = [] 
        for i in range(n):
            ans.append(dit[arr[i]])
            
        return ans
```
