# Brute force approach
# nums= [10,20,30,40,50]
# largestSum=0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         sum=0
        
#         # print(f"i:{i}, j:{j}") # print combinations of all indices
#         for k in range(i,j+1):
#             sum+=nums[k]
#             print(f"{nums[k]} , ", end= " ")
#         if sum > largestSum:
#             largestSum = sum  
#         print(end="\n")  
# print(largestSum)
        

# Prefix sum approach
# nums1= [1,-2,3,4,-5]
# prefix=[] 
# # print(prefix)
# prefix.insert(0,nums1[0])
# # print(prefix)
# # prefix.insert(0)= nums1[0]
# largestSum= 0

# for i in range(1,len(nums1)):
#     prefix.insert(i,prefix[i-1] + nums1[i])
#     print(prefix)
# print(prefix)
# for i in range(len(nums1)):
#     for j in range(i, len(nums1)):
#         subarraySum= prefix[j] - prefix[i-1] if i>0  else prefix[j]
#         largestSum= max(largestSum, subarraySum)
#         # for k in range(i, j+1):
#         #     print(f"{i},{j}")
# print(largestSum)
# here the time complexity is reudced to nsquare instead of ncube

# Kadane's algorithm approach
# Dynamic Programming approach which states that every element has two choices: 1. continuing with the previous series 2. starting
# its own series
nums2= [-2,3,4,-1,5,-12,6,1,3,2]
# nums2=[4,3,-2,6,-14,7,-1,4,5,7,-10,2,9,-10,-5,-9,6,1]
# nums2=[4,3,-2,6,7,-10,-10,4,5,9,-3,4,7,-28,2,9,3,2,11]
# nums2=[-2,-1]
currentSum=nums2[0]
largestSum=nums2[0]
# if len(nums2) ==1:
#     largestSum = nums2[0]

for i in range(1,len(nums2)):
    currentSum = max(nums2[i], currentSum + nums2[i]) 
    if currentSum > largestSum:
        largestSum = currentSum
    print(currentSum)
print(largestSum)
        
