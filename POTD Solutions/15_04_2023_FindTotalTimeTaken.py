from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        curr = 0
        taken = {}
        
        for i in range(n):
            if arr[i] not in taken:
                taken[arr[i]] = curr
            else:
                curr = max(curr, taken[arr[i]] + time[arr[i]-1])
                taken[arr[i]] = curr
            curr += 1
        
        return curr - 1
