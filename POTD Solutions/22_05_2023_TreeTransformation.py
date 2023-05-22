from typing import List


class Solution:
    def solve(self, N : int, p : List[int]) -> int:
        con = [0] * N
        for i in range(1, N):
            con[i] += 1
            con[p[i]] += 1
    
        ans = 0
        for x in con:
            if x == 1:
                ans += 1
    
        return N - ans - 1
