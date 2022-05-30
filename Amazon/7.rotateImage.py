matrix = [[1,2,3],[4,5,6],[7,8,9]]
n= len(matrix[0])
# take transpose of the matrix
for i in range(n):
    for j in range(i,n):
        matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
print(matrix)
# then flip horizontally
for i in range(n):
    for j in range(n//2):
        matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
print(matrix)