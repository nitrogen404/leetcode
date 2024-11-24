def rotateImage(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    for i in range(ROWS):
        for j in range(i + 1, ROWS):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(ROWS):
        matrix[i].reverse()
    return matrix

print(rotateImage([[1,2,3],[4,5,6],[7,8,9]]))
