import operator
nums = [2,2,1,1,1,2,2]
map = {}
for i in nums:
    if i in map:
        map[i] +=1
    else:
        map[i] =1
print(map)

# maxValue = max(map.values())
# for x in map.items():
#     # print(x
#     if x[1] == maxValue:
#         print(x[0])
# using lambda function
maxKey = max(map, key= lambda x : map[x])
print(maxKey)

# using operator module's itemgetter()
# here we pass an iteratable i.e a set of tuples from map.keys() to max()
# and key is operator.itemgetter(1) which means (key,value)'s value field is deciding factor
# this will return a set of tuple with highest value and we want its key, so append[0] to the result
keyMax = max(map.items(), key = operator.itemgetter(1))[0]
print(keyMax)

# using sort()
# since a majority element is the one occuring >n/2 times, we can sort the array and find the middle element as it would be the
# majority element
nums.sort()
sortedMax= nums[len(nums)//2]
print(sortedMax)
# now to make sure we have majority element, we check counts of this element
print(sortedMax) if nums.count(sortedMax) > len(nums)//2 else print("No")

# Boyer moore algorithm
majorityElement = nums[0] 
# current = nums[0]
count = 0
for i in nums:
    if majorityElement == i:
        count+=1
    else:
        count-=1
    if count ==0:
        majorityElement = i
        count=1
        # majorityElement = i
# now to ensure that we found the right element, we check if the majority element found above has count > n//2  or not
count =0
for i in nums:
    if i == majorityElement:
        count+=1
if count > len(nums)//2:
    print("Yes it is majority element and the count is " + str(count))
print("There is a majority element = "+str(majorityElement)) if count >0 else print("there is no majority element")