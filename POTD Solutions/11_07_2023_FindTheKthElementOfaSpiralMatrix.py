class Solution:
    def findK(self, a, n, m, k):
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        direction = 0
        count = 0
    
        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    count += 1
                    if count == k:
                        return a[top][i]
                top += 1
                direction = 1
    
            elif direction == 1:
                for i in range(top, bottom + 1):
                    count += 1
                    if count == k:
                        return a[i][right]
                right -= 1
                direction = 2
    
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    count += 1
                    if count == k:
                        return a[bottom][i]
                bottom -= 1
                direction = 3
    
            else:
                for i in range(bottom, top - 1, -1):
                    count += 1
                    if count == k:
                        return a[i][left]
                left += 1
                direction = 0
    
        return -1 
