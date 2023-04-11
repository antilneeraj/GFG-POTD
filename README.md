<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Maximum Length<br><br>

```python
class Solution:
    def solve(self, a, b, c):
        if a > (2 * (b + c) + 2) or b > (2 * (a + c) + 2) or c > (2 * (b + a) + 2):
            return -1
        return a + b + c
```
