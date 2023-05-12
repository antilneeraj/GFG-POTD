from typing import List

class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        ans = 0
        length = 0
    
        for i in range(n):
            if arr[i] == 0:
                if length:
                    ans += 1
                length = 0
            else:
                length += 1
    
        if length == n:
            return -1
        if length:
            ans += 1
    
        return ans
