from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        S = sum(A)
        minNum=float('inf')
        
        for X in A:
            if(S<=N*X and X < minNum):
                minNum=X
        return minNum
