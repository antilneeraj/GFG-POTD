class Solution:
    def isWordExist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.help(board, word, i, j, 0):
                    return True
        return False
    
    def help(self, b, w, i, j, length):
        if length == len(w):
            return True
        
        if i < 0 or j < 0 or i >= len(b) or j >= len(b[0]):
            return False
        
        if b[i][j] != w[length]:
            return False
        
        b[i][j] = '*'  # mark it as visited so that it cannot be used again in the path
        
        result = (
            self.help(b, w, i-1, j, length+1) or  # up
            self.help(b, w, i+1, j, length+1) or  # down
            self.help(b, w, i, j-1, length+1) or  # left
            self.help(b, w, i, j+1, length+1)     # right
        )
        
        b[i][j] = w[length]  # revert the mark to restore the board
        
        return result
