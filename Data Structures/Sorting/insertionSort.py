# Code to implement insertion sort
nums=[9,8,7,6,5,4,3,2,1]
for i in range(1, len(nums)):
    currentElement = nums[i]
    previousIndex= i-1
    while previousIndex >=0 and nums[previousIndex] > currentElement:
        nums[previousIndex +1] = nums[previousIndex]
        previousIndex -= 1
    nums[previousIndex+1] = currentElement
print(nums)
