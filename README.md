<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Ticker Counter<br><br>

```python
from collections import deque

class Solution:
    def distributeTicket(self, N: int, K: int) -> int:
        arr = deque(range(1, N + 1))
        iturn = True
        count = 0

        while len(arr) > 0:
            if count < K:
                if iturn:
                    lastElem = arr.popleft()
                else:
                    lastElem = arr.pop()
                count += 1

            if count == K:
                count = 0
                iturn = not iturn

        return lastElem

```
