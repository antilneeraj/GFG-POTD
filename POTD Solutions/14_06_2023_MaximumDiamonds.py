import heapq

class Solution:
    def maxDiamonds(self, A, N, K):
        heap = []
        for num in A:
            heapq.heappush(heap, -num)

        arr = []
        while K != 0:
            max_num = -heapq.heappop(heap)
            arr.append(max_num)
            max_num //= 2
            heapq.heappush(heap, -max_num)
            K -= 1

        return sum(arr)
