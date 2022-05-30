# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
nums= [1,2,3,4]
# loop through the left and add products of the numbers on the lhs of the current number
# for eg, in this case we will get [1,1,2,6]
# loop from the end of the array and add products of the numbers on the rhs of the current number
# for eg, in this case - [24,12,4,1]
# for the solution, multiply the numbers index wise, we get   =[24,12,8,6]
left_array,right_array,result = [1]*len(nums),[0]*len(nums),[]
for i in range(1,len(nums)):
    left_array[i] = nums[i-1]*left_array[i-1]

print(left_array)
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1: right_array[len(nums)-1]= 1
    else:
        right_array[i]=right_array[i+1]*nums[i+1]
print(right_array)
#for the solution, multiply the elements index wise
for i in range(len(nums)):
    result.append(left_array[i]*right_array[i])
print(result)


#approach 2 - without using any extra space except the output array
output = [1]*len(nums)
# we are using the output array as the left array used earlier
for i in range(1,len(nums)):
    output[i] = output[i-1]*nums[i-1]
print(output)
# for the right products, we will use a variable
product =1
for i in range(len(nums)-1,-1,-1):
    output[i] = output[i]*product
    product*=nums[i]
print(output)