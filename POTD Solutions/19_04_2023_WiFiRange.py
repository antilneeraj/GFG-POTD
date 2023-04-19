class Solution:
    def wifiRange(self, n, s, x):
        v = []
        for i in range(n):
            if s[i] == '1':
                v.append(i)
        for i in range(len(v)-1):
            if v[i+1] - v[i] - 1 > 2*x:
                return False
        if v[0] > x:
            return False
        if n-1-v[-1] > x:
            return False
        return True
