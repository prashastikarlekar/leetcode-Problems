# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number 
# of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the 
# last n elements are set to 0 and should be ignored. nums2 has a length of n.

# nums1 = [1,2,3,0,0,0]
nums1= [4,5,6,0,0,0]
nums2=[1,2,3]
m = 3
# nums2 = [2,5,6]
n = 3
# print(len(nums1))
# for i in range(m,len(nums1)):
#     nums1[i] = nums2[i-m]
# print(nums1)
# nums1.sort()
# print(nums1)
i=j=0
while i < (len(nums1)-m) and j < len(nums2):
    # print(i)
    if nums1[i] > nums2[j]:
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums1[m] = temp
        m+=1
    i+=1
print(m)
# for i in nums2:
#     # print(i)
#     if i not in nums1:
#         nums1[m] = i
#         m+=1

print(nums1)
print(nums2)





# temp=0
# for n2 in range(len(nums2)):
#     for n1 in range(len(nums1)):
#         print(f"Number from array 1 is {nums1[n1]} and from array 2 is {nums2[n2]}")
#         firstNumber =nums1[n1]
#         secondNumber =nums2[n2]
#         if secondNumber < nums1[m]:
#             firstNumber = nums1[n1]
#             firstNumber = nums1[m+1]
#             m+=1
        
#             nums1[n1-1] = nums2[n2]
#             break
#             # if n2 != len(nums1)-1:
#             #     nums1[n1] = tmp
                
        

#         print(nums1)

# print(nums1)

# # for j in range(len(nums2)):
# #     for i in range(len(nums1)):
# #         if nums2[i] <= nums1[j]:
# #             temp= nums1[j]
# #             nums1[j] = nums2[i]

# #             # nums1.insert(i+1, temp)
# #             if i != len(nums1) -1:
# #                 nums1[j+1] = temp 
            
    
# # print(nums1)


