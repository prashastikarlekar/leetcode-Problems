# if its in 0th row, it shouldn't be in 0th column
# input =[["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

input =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# rowDict={}
# # rows
# # for i in range(9):
# #     dict[input[i]] =1
# # print(dict)
# # count =1
# currentIndex =0
# for i in input:
#     # index=[]

#     for j in i:
#         if j != ".":
#             print(j)
#             if j not in rowDict :
#                 index=[]
#                 indexOfj=i.index(j)
#                 # print(f'index of {j} is {indexOfj}')
#                 index.append(indexOfj)
#                 # print(f"j is {j} and its first array is {index}")
#                 rowDict[j] = index
#             else: # if key is already in rowDict, just append current index
#                 currentIndex = rowDict[j] # retrieve current index
#                 # print(f"current index of {j} is {currentIndex}")
#                 indexOfj = i.index(j)
#                 # print(f'index of {j} is {indexOfj}')
#                 currentIndex.append(indexOfj)
#                 rowDict[j]=currentIndex
#                 if len(currentIndex)!= len(set(currentIndex)): # if they are not equal, it implies they have duplicate values
#                     print(f"current index list is {currentIndex} and set is {(set(currentIndex))}, so False")
#                     # print("False")
# start =0
# stop =3
# for k in range(len(input)):
    
#     for l in range(k,3):
#         # print(f'i is {i} and l is {l}. element is {i[l]}',end ="   ")
#         print(input[k][l],end="         ")

    

# print(rowDict)

# ls =[3,2,1]

# lsSet = set(ls)
# print(ls)
# print(list(lsSet))
# if ls != list(lsSet):
#     print("Not equal")

newDict={}
for i in input:
    for j in i:
        if j!='.' and j not in newDict:
            indexes = []
            index = (input.index(i), i.index(j))
            indexes.append(index)
            newDict[j] = indexes

        elif j!='.' and j in newDict:
            currentIndex = newDict[j]
            index= (input.index(i), i.index(j))
            currentIndex.append(index)
            newDict[j] = currentIndex
print(newDict)
# for i in newDict:

for i in range(9):
    for j in range(9):
        print(input[i][j])
# check row (i,c)
# for i in range(9):
#     count = 0
#     if 

row_map ={}
column_map = {}
        
valid_coord = []
        
nums = ["1","2","3","4","5","6","7","8","9"]
valid =True
x =0
for row in input:
            y=0
            row_map[x] = []    
            for num in row:
                print("Row "+str(x)+ " Col: "+str(y))
                if(num in nums):
                    valid_coord.append((x,y))
                    if(y not in column_map):
                        column_map[y] =[]
                        
                    if(num in column_map[y]):
                        #invalid column
                        print False

                    column_map[y].append(num) 
                    
                    if(num in row_map[x]):
                        #invalid row    
                        return False
                    row_map[x].append(num)
                y+=1
            x+=1                    
        #rows & cols valid
return True



    

