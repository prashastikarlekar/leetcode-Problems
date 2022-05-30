

nums=[-1,2,1,-4]
target =1
nums.sort()
diff = float('inf')
for i in range(len(nums)):
    low= i+1
    high = len(nums)-1
    while low<high:
        sum = nums[i]+nums[low]+nums[high]
        if abs(target-sum) < abs(diff):
            diff = target-sum
        if sum < target: low+=1
        else:
            high-=1
    if diff ==0:break
print(target - diff)