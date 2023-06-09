from typing import List


class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        curr = 0
        taken = {
            arr[0]: True
        }
        
        for i in range(1, n):
            arri=arr[i]
            if(arri in taken):
                curr+=time[arri-1]
            else:
                curr+=1
            
            taken[arri] = True
        
        return curr
