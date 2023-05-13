<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Bit Magic<br><br>

```python
from typing import List

class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        Operations = 0
        i = 0
        j = n - 1
        while i < j:
            if(arr[i] != arr[j]):
                Operations += 1
            i += 1
            j -= 1
        ans = str(Operations/2 + Operations%2)
        return ans[:ans.index(".")] if "." in ans else ans
```
