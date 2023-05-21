class Solution:
    def findMoves(self,n,chairs,passengers):
        chairs.sort()
        passengers.sort()
        ans = 0
        for i in range(n):
            ans += abs(chairs[i] - passengers[i])
        return ans
