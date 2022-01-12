# # Code to implement bubble sort algorithm
# nums=[5,4,3,2,1]
# n= len(nums)
# for i in range(n-1):
#     # print(i)
#     for j in range(n-i-1):
#         # print(j)
#         if nums[j]> nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]

# print(nums)




nums1=[7,6,5,4,3,2,1]
for i in range(len(nums1)-1):
    for j in range(len(nums1)-i-1):
        if nums1[j]>nums1[j+1]:
            nums1[j],nums1[j+1] = nums1[j+1], nums1[j]
print(nums1)

