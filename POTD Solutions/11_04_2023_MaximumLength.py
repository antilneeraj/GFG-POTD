class Solution:
    def solve(self, a, b, c):
        if a > (2 * (b + c) + 2) or b > (2 * (a + c) + 2) or c > (2 * (b + a) + 2):
            return -1
        return a + b + c
