<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Unique Number of Occurrencees<br><br>

```python
from typing import List

class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        frequencies = dict()
        for i in arr:
            if(i not in frequencies): frequencies[i] = 0
            frequencies[i]+=1
        frequencies=frequencies.values()
        return len(set(frequencies))==len(frequencies)
```
