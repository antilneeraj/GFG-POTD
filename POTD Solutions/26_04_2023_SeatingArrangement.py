from typing import List

class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        prevSit=None
        nextSit=None
        count=n
        for i in range(m):
            nextSit=seats[i+1] if i<m-1 else False
            if(not (prevSit or nextSit) and seats[i] != 1):
                count-=1
                prevSit=True
            else:
                prevSit=False
            if(seats[i] == 1):
                prevSit=True
            if(count == 0):
                break
        if(count==0):
            return True
        return False
        
