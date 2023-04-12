from typing import List

class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        arr[:n//2] = sorted(arr[:n//2])  # sort left half
        arr[n//2:n] = sorted(arr[n//2:n])  # sort right half
        
        ans = 0
        j = n // 2
        for i in range(n // 2):
            while j < n and arr[i] >= 5 * arr[j]:
                j += 1
            ans += j - n // 2
        
        return ans
