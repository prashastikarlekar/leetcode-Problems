from itertools import repeat
# from typing import final
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times
#  as it shows in both arrays and you may return the result in any order.

# nums1= [4,9,5]
# nums2 = [9,4,9,8,4]
nums1=[1,2,2,1]
nums2=[2]
result=[]
# for n1 in range(len(nums1)):
#     for n2 in range(len(nums2)):
#         if nums1[n1] == nums2[n2]:
#             result.append(nums1[n1])
#             break
# print(result)
 
# for num in range(len(nums1)):
    
map1 = {}
map2 = {}
for num in nums1:
    if num in map1:
            # count = map1[num] # retrieve us key ki value, i.e current count of the number present in map
            count = map1[num]
            map1[num] =count+1
    else:
            map1[num] = 1
    
for num in nums2:
    if num in map2:
            count = map2[num]
            map2[num] = count+1
    else:
            map2[num] =1
# print(map1)
for key in map1.keys():
    if key in map2.keys():
            finalCount = min(map1[key],map2[key])
            result.extend(repeat(key,finalCount))
print(result)        
    
#     if nums1[n1] in nums2 :
#         result.append(nums1[n1])
#     if n1< len(nums1):
#         nums2.index(result,start = nums2[n1+1])
#     print(nums2)
# print(result)



# def power(x, n):
#     if n==0:
#         return 1
#     elif n>0 and n%2 ==0:
#         return power(x,n/2) * power(x,n/2 )
        
#     elif n>0 and n%2!=0:
#         return power(x,1)*(power(n-1)/2)*(power(n-1)/2)

#     else:
#         return 0
# power(2,3)



    # return power()
# 
