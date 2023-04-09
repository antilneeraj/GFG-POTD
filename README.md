<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Special Digits<br><br>

```python
mod = 10**9 + 7
hogya = False
factorial = [0] * 100001
mm = [0] * 100001

class Solution:
    def help(self):
        factorial[0] = 1
        for i in range(1, 100001):
            factorial[i] = (i * factorial[i-1]) % mod
        mm[100000] = self.power(factorial[100000], mod - 2)
        for i in range(99999, -1, -1):
            mm[i] = (mm[i+1] * (i+1)) % mod

    def power(self, x, y):
        res = 1
        x = x % mod
        while y > 0:
            if y & 1:
                res = (res * x) % mod
            y = y >> 1
            x = (x * x) % mod
        return res

    def help2(self, n, r):
        return (factorial[n] * mm[r] % mod * mm[n - r] % mod) % mod

    def bestNumbers(self, N, A, B, C, D):
        global hogya
        hai = False
        i = 0
        if A == B:
            sum = N * A
            while sum != 0:
                digit = sum % 10
                if digit == C or digit == D:
                    hai = True
                    break
                sum //= 10
            if hai:
                return 1
            return 0
        if hogya == False:
            self.help()
            hogya = True
        ans = 0
        while i <= N:
            sum = A * i + (B * (N - i))
            hai = False
            while sum != 0:
                digit = sum % 10
                if digit == C or digit == D:
                    hai = True
                    break
                sum //= 10
            if hai == True:
                ans += self.help2(N, i)
                ans %= mod
            i += 1
        return ans
```
