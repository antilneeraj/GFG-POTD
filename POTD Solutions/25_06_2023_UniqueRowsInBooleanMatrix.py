from typing import List

class Solution:
    def uniqueRow(self, row, col, matrix):
        final = []
        for i in range(row):
            if matrix[i] not in final:
                final.append(matrix[i])
        
        return final
