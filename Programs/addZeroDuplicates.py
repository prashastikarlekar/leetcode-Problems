# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
# arr1 = [1,0,2,3,0,4,5,0]
# copyArr=[]
# copyArr=[arr1[i] if arr1[i]!=0 else copyArr.extend([0]*2) for i in range(len(arr1))]
# # for i in range(len(arr1)):
# #     if arr1[i]!=0:
# #         copyArr.append(arr1[i])
# #     else:
# #         copyArr.extend([0]*2)
# #         # (copyArr.append(0))*2
# #         # copyArr.append(0)
# print(copyArr)

# cut= len(copyArr)-len(arr1)

# [copyArr.pop() for j in range(cut)]
arr1=[1,0,2,3]
copyarr=[]
copyarr= [copyarr.extend([0,0]) if i==0 else copyarr.append(i) for i in arr1]

for i in arr1:
    if i==0:        
        copyarr.extend([0,0])
    else:
        copyarr.append(i)
print(copyarr)
# if len()