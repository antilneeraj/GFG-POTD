<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Arranging the Array<br><br>

```python
class Solution:
    def Rearrange(self, n, arr):
        temp = []
        for i in range(n):
            if arr[i] < 0:
                temp.append(arr[i])
        for i in range(n):
            if arr[i] >= 0:
                temp.append(arr[i])
        for i in range(n):
            arr[i] = temp[i]
```
