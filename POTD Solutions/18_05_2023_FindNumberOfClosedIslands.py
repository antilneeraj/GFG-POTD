class Solution:
    def help(self, arr, i, j, N, M):
        if i < 0 or j < 0 or i == N or j == M or arr[i][j] == 0:
            return
        arr[i][j] = 0
        self.help(arr, i + 1, j, N, M)
        self.help(arr, i - 1, j, N, M)
        self.help(arr, i, j + 1, N, M)
        self.help(arr, i, j - 1, N, M)
    
    def closedIslands(self, matrix, N, M):
        ans = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0 or i == N - 1 or j == M - 1:
                        self.help(matrix, i, j, N, M)
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    ans += 1
                    self.help(matrix, i, j, N, M)
        return ans
