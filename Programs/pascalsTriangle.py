numRows= 5
# result = []
# for i in range(numRows):
#     templist=[]
#     for j in range(i+1):
#         if j==0 or j==i: 
#             templist.append(1)
#         else:
#             templist.append(result[i-1][j-1] + result[i-1][j])
#     result.append(templist)
# print(result)


triangle =[[1],[1,1]]

if(numRows==1): print [[1]]
if(numRows==2): print(triangle) # we cant make 2nd row from first row so hats why we are hard-coding it
    
for i in range(2,numRows):
        templist=[1]
        for j in range(1,i):
            templist.append(triangle[i-1][j-1]+ triangle[i-1][j])
        templist.append(1)
        triangle.append(templist)
print(triangle) 