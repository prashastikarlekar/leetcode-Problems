# given an  input matrix, search a target value in the matrix
# given that matrix.length  = m and n = matrix[i].length 
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1,3]]
target = 3
m =  len(matrix)
print(f"length of m is {m}")
listOfElements = []
for i in range(m):
    print(matrix[i]) # i represents the row of the matrix
    for j in matrix[i]:
        print(j)
        listOfElements.append(j)
    print(f"list of elements is {listOfElements}")
    

# print(len(listOfElements))
for i in range(len(listOfElements)):
    if listOfElements[i] == target:
        print(f"True. the element is {listOfElements[i]}")

        break
    else:
         print("False")
# if listOfElements[i] == target:
#         print(f"True. the element is {listOfElements[i]}")
#         break
#     else:
#         print("False")