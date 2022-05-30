# Given an array nums of integers, return how many of them contain an even number of digits.
nums = [345,12,347,456,34,45,799,46,345,89,5663]
evens=0
for i in range(len(nums)):
    count=0
    while nums[i]!=0:
        nums[i]=nums[i]//10
        count=count+1
    if count%2 ==0:
        evens=evens+1
print(evens)