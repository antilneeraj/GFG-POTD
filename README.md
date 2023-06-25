<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Unique rows in boolean matrix<br><br>

```python
from typing import List

class Solution:
    def uniqueRow(self, row, col, matrix):
        final = []
        for i in range(row):
            if matrix[i] not in final:
                final.append(matrix[i])
        
        return final
```
