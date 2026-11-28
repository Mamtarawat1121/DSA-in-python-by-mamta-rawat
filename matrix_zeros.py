# brute force 

def mark_infinity(matrix,row,col):
    r = len(matrix), c= len(matrix[0])
    for i in range(0,r):
        if matrix[i][col]!=0:
            matrix[i][col] = float("inf")
    for j in range(0,c):
        if matrix[row][j]!=0:
            matrix[row][j] = float("inf")        