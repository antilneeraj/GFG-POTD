<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Bus Conductor<br><br>

```python
class Solution:
    def findMoves(self,n,chairs,passengers):
        chairs.sort()
        passengers.sort()
        ans = 0
        for i in range(n):
            ans += abs(chairs[i] - passengers[i])
        return ans
```
