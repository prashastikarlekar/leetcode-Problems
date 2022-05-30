# Given a binary array, find the maximum number of consecutive 1s in this array.
# nums= [1,1,0,1,1,1]
nums= [1,1,0,1]
# nums =[1]
count=0
maxCount=0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
    else:
        maxCount =max(count,maxCount)
        count=0
    
        
        
   
print(maxCount)
