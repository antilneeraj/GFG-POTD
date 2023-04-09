<h1 align="center">Today's GFG-POTD {Problem Of The Day}</h1>

### Title - Special Digits<br><br>

```python
max_size = 10**5 + 10
fact = [0] * max_size
mod = 10**9 + 7

def power(n, x):
    ans = 1
    while x > 0:
        if x & 1:
            ans = (ans * n) % mod
            x -= 1
        else:
            n = (n * n) % mod
            x >>= 1
    return ans % mod

def checker(n, c, d):
    s = str(n)
    for i in s:
        if int(i) != c and int(i) != d:
            return False
    return True

def ncr(n, r):
    ans = fact[n]
    ans = (ans * power(fact[r], mod - 2)) % mod
    ans = (ans * power(fact[n - r], mod - 2)) % mod
    return ans % mod

class Solution:
    def bestNumbers(self, N, A, B, C, D):
        fact[0] = fact[1] = 1
        for i in range(2, N + 5):
            fact[i] = (i * fact[i - 1]) % mod

        ans = 0
        for i in range(N + 1):
            sum = i * A + (N - i) * B
            if checker(sum, C, D):
                ans = (ans + ncr(N, i)) % mod

        return ans
```
