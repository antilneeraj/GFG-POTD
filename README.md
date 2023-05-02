<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Cake Distribution Problem<br><br>

```python
class Solution():
    def isPoss(self, sweetness, mid, k):
        sum_val = 0
        cnt = 0
        for s in sweetness:
            sum_val += s
            if sum_val >= mid:
                cnt += 1
                sum_val = 0
        return cnt >= k + 1    
    
    
    def maxSweetness(self, sweetness, n, k):
        sum_val = 0
        min_sweetness = float('inf')
        for s in sweetness:
            sum_val += s
            min_sweetness = min(min_sweetness, s)
        
        l = min_sweetness
        h = sum_val
        ans = 0
        
        while l <= h:
            mid = (l + h) // 2
            if self.isPoss(sweetness, mid, k):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        
        return ans
```
