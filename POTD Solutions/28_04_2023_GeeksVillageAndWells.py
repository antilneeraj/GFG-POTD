from typing import List, Tuple
from collections import deque

class Solution:
    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append((i,j))
                    ans[i][j] = 0
        
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        
        while q:
            temp = q.popleft()
            i, j = temp[0], temp[1]
            for k in range(4):
                newi = i + x[k]
                newj = j + y[k]
                if 0 <= newi < n and 0 <= newj < m and c[newi][newj] != 'N' and ans[newi][newj] == -1:
                    ans[newi][newj] = ans[i][j] + 1
                    q.append((newi, newj))
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'N' or c[i][j] == '.':
                    ans[i][j] = 0
                elif ans[i][j] != -1:
                    ans[i][j] *= 2
        
        return ans
