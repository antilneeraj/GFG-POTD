<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Minimum Number<br><br>

```python
class Solution:
    def minimumNumber(self, n, arr):
        if n==1:
            return arr[0]
        if n==2:
            return abs(arr[0] - arr[1])
        else:
            return 1
```
