rowIndex = 3
# Output: [1,3,3,1]
triangle = [[1],[1,1]]

if rowIndex ==0:
    print([1])
elif rowIndex ==1:
    print(triangle)
else:
    for i in range(2,rowIndex+1):
        tempList =[1]
        for j in range(1,i):
            tempList.append(triangle[i-1][j-1]+triangle[i-1][j])
        tempList.append(1)
        triangle.append(tempList)
    print(triangle[rowIndex])
