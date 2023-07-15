<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Delete Middle Element of a Stack<br><br>

```python
class Solution:
    def deleteMid(self, s, sizeOfStack):
        midIndex = (sizeOfStack + 1) // 2
        if midIndex == 0 or midIndex >= sizeOfStack:
            return s
        del s[midIndex-1]
        return s
```
