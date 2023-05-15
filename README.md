<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Count Total Setbits<br><br>

```python
class Solution:
    def countBits(self, N : int) -> int:
        ans = 0
        i = 1
        n = N
        while n != 0:
            temp = (N + 1) // (i * 2)
            ans += temp * i
            temp = (N + 1) // i
            if temp % 2 == 1:
                ans += (N + 1) % i
            i *= 2
            n >>= 1
        return ans
```
