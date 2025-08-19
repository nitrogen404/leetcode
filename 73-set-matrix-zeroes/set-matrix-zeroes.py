class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        COLS = len(matrix[0])
        ROWS = len(matrix)
        isFirstBlockZero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        isFirstBlockZero = True
        
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                matrix[r] = [0 for _ in range(COLS)]
        
        for c in range(COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0
        
        if isFirstBlockZero:
            matrix[0] = [0 for _ in range(COLS)]

        