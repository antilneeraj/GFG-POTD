from collections import deque

class Solution:
    def nearestSmallestTower(self, arr):
        n = len(arr)
        left, right = deque(), deque()
        res = [-1] * n

        for i in range(n):
            while left and arr[left[-1]] >= arr[i]:
                left.pop()

            if left:
                res[i] = left[-1]

            left.append(i)

        for i in range(n-1, -1, -1):
            while right and arr[right[-1]] >= arr[i]:
                right.pop()

            if right:
                if res[i] != -1:
                    if abs(res[i] - i) == abs(right[-1] - i):
                        if arr[res[i]] > arr[right[-1]]:
                            res[i] = right[-1]
                    elif abs(res[i] - i) > abs(right[-1] - i):
                        res[i] = right[-1]
                else:
                    res[i] = right[-1]

            right.append(i)

        return res
