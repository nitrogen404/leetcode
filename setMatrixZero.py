def setMatrixZero(matrix):
    COLS = len(matrix[0])
    ROWS = len(matrix)
    isFirstRowZero = False
    
    for r in range(ROWS): # determining where 0s exist
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    isFirstRowZero = True
    
    
    for r in range(1, ROWS): # sets all rows to 0
        if matrix[r][0] == 0:
            matrix[r] = [0 for _ in range(COLS)]
    
    for c in range(COLS):
        if matrix[0][c] == 0:
            for r in range(1, ROWS):
                matrix[r][c] = 0
    
    if isFirstRowZero:
        matrix[0] = [0 for _ in range(COLS)]
    
    return matrix

    
print(setMatrixZero([
                     [0,1,2,0],
                     [3,4,5,2],
                     [1,3,1,5]  
                     ]))