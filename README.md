<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Transpose of Matrix<br><br>

```python
class Solution:
    def transpose(self, matrix, n):
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```
