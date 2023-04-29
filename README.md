<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - FInd Number<br><br>

```python
class Solution:
    def findNumber(self, N : int) -> int:
        curr, ans = 1, 0
        arr = [9, 1, 3, 5, 7]
        while N:
            ans = arr[N%5] * curr + ans
            if N%5 == 0:
                N = N//5 - 1
            else:
                N = N//5
            curr = curr * 10
        return ans
```
