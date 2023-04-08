from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        n = len(arr)
        lst = []
        for i in range(n):
            if len(lst) != 0 and ((lst[-1] < 0 and arr[i] >= 0) or (lst[-1] >= 0 and arr[i] < 0)):
                lst.pop()
            else:
                lst.append(arr[i])
        return lst
