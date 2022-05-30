# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
nums = [-4,-1,0,3,10]
squaredNums=[]
for i in range(len(nums)):
    (squaredNums).append(nums[i]**2)
squaredNums.sort()
print(squaredNums)


nums=[1,3,6,7,9,5]
target= 13
for i in range(len(nums)):
    if nums[i] + nums[i+1] == target:
        print(i)