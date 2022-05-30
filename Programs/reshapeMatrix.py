# mat= [[1,2,3,4],[5,6,7,8]]
mat=[[1,2],[3,4]]
r= 2
c=2
# print(mat[1][1])
# resultMatrix = [[0]*r]*c
# print(resultMatrix)
exisitngCols = (len(mat)) # will give number of existing columns
exisitngRows = int(c/len(mat)) #2
# for i in range(len(mat)):
#     for j in range(c/len(mat)): # c/exisitng cols will give remaining number of elements i.e rows elements:

# for i in range(0,exisitngCols-1):
# # for i in range(1):
#     # print(len(mat[i]))
#     # for j in range(exisitngRows):
#         # print(mat[j])
#         # resultMatrix[j] = "".join(str(mat[j]))
#     a,*others, b= mat[i]

#     resultMatrix[i] = a
#     resultMatrix[i+1] = b

#     print(a)
#     print(b)
    # print(i) # 0,1,2,3
    # for j in range(r):
    #     print(j)
    #     # print(j[0])
    #     resultMatrix[j]=mat[j]
# print(resultMatrix)
# a,*others,c= [4,2,6]
# print(others)
resultMatrix = []
# for i in range(len(mat)):
#     for j in mat[i]:
#         resultMatrix.append(j)
# for k in resultMatrix:

# resultMatrix[0] = resultMatrix
# print(list(resultMatrix))

# print(len(mat))
# for i in mat:
#     for j in i:
#         resultMatrix.append(j)
#         # print(i)
#         # print(j)

# print(resultMatrix)
# for i in resultMatrix:
#     for j in range(r):
m= len(mat)
n= len(mat[0])
count=0
row=[]
if m*n == r*c:
    for i in mat:
        for j in i:
            count+=1

            if len(row) ==c-1:
                print(row)
                row.append(j)
                resultMatrix.append(row)
                print(resultMatrix)
                row= []
                count=0
            else:
                row.append(j)

        # return resultMatrix


            # print(f'i is {i} , j is {j}')
            # resultMatrix.append(j)
            
print(resultMatrix)
        # return resultMatrix


            # resultMatrix.append(j)
            