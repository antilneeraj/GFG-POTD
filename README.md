<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Adding Ones<br><br>

```python
class Solution:
    def update(self, a, n, updates, k):
        temp = 0
        for i in range(k):
            a[updates[i]-1] += 1
    
        for i in range(n):
            a[i] += temp
            temp = a[i]
```
