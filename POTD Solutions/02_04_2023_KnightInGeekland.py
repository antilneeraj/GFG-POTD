from collections import deque

class Solution:
    def knightInGeekland(self, arr, start):
        n = len(arr)
        m = len(arr[0])
        
        dx = [-1, -2, -2, -1, 1, 2, 2, 1]
        dy = [-2, -1, 1, 2, 2, 1, -1, -2]

        visited = [[False]*m for _ in range(n)]
        queue = deque()
        queue.append((start[0], start[1]))
        visited[start[0]][start[1]] = True
        points = [0]*1001
        steps = 0

        while queue:
            qSize = len(queue)
            for i in range(qSize):
                x, y = queue.popleft()
                points[steps] += arr[x][y]
                for k in range(8):
                    currX = x + dx[k]
                    currY = y + dy[k]
                    if currX < 0 or currY < 0 or currX >= n or currY >= m or visited[currX][currY]:
                        continue
                    visited[currX][currY] = True
                    queue.append((currX, currY))
            steps += 1
    
        ans = 0
        maxi = float('-inf')
        for i in range(1001):
            curr = i
            totalpoints = 0
            while curr <= 1000:
                if points[curr] == 0:
                    break
                totalpoints += points[curr]
                curr += points[curr]
            points[i] = totalpoints
            if points[i] > maxi:
                maxi = points[i]
                ans = i
        
        return ans