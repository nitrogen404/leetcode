class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    
                    for col in range(cols):
                        if matrix[r][col] != 0:
                            matrix[r][col] = 'a'
                    
                    for row in range(rows):
                        if matrix[row][c] != 0:
                            matrix[row][c] = 'a'

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 'a':
                    matrix[r][c] = 0
         
