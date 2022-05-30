def twoSum(nums, i, result):
    low = i+1
    high= len(nums)-1
    while low<high:
        sum =nums[i]+nums[low]+nums[high]
        if sum<0:
            low+=1
        elif sum >0:
            high-=1
        else:
            result.append([nums[i],nums[low],nums[high]])
            low+=1
            high-=1
            while low<high and nums[low]==nums[low-1]:
                low+=1
                
if __name__=="__main__":  
    nums = [-1,0,1,2,-1,-4]
    result =[]
    nums.sort()           
    for i in range(len(nums)):
        if nums[i]>0: break
        if i==0 or nums[i-1]!=nums[i]:
            twoSum(nums,i,result)
    print(result)