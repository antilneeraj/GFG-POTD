<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Unequal Arrays<br><br>

```python
class Solution:
    def solve(self, N, A, B):
        # code here
        sum = 0
        # make two lists for storing and separating odd and even elements
        x = [[], []]
        y = [[], []]
        # iterate over A and B arrays
        for i in range(N):
            sum += A[i] - B[i]
            if A[i] % 2 == 0:
                x[0].append(A[i])
            else:
                x[1].append(A[i])
            if B[i] % 2 == 0:
                y[0].append(B[i])
            else:
                y[1].append(B[i])
    
        # not possible to convert
        if sum != 0 or len(x[0]) != len(y[0]):
            return -1
    
        ans = 0
    
        # sort list one by one and take the difference.
        for i in range(2):
            x[i].sort()
            y[i].sort()
    
            for j in range(len(x[i])):
                ans += abs(x[i][j] - y[i][j]) // 2
    
        return ans // 2
```
