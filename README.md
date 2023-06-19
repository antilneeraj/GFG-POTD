<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Rearrange an array with O(1) extra space<br><br>

```python
class Solution:
    def arrange(self,arr, n): 
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
    
        for i in range(n):
            arr[i] = arr[i] // n
    
        return arr
```
