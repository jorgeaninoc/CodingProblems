def zeroMatrix(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                positions.append((i,j,len(matrix),len(matrix[i])))

    for i,j,r,c in positions:
        for x in range(c):
            matrix[i][x] = 0
        for y in range(r):
            matrix[y][j] = 0
    return matrix

m = [[1,1,1,1],[1,1,1,1],[1,0,1,1]]
print(zeroMatrix(m))