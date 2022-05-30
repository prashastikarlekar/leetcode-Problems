# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
nums=[3,0,1]
n=len(nums)
for i in range(n+1):
    if i not in nums:
        print(i) 

# for optimization w ecan also use set
num_set =set(nums)
for i in range(n+1):
    if i not in num_set:
        print(i)

