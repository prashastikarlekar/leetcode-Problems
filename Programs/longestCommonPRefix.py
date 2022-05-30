# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# strs=["flower","flow","flight"] #o/p =fl
# strs = ["dog","racecar","car"]
strs =['cir','car']
# strs.sort(key=(lambda(strs[i]:len(strs[i]) for i in range(len(strs)))))
# print(strs)

# nums=[10,20,30,40]
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         for k in range(i,j+1):
#             print(str(nums[k])+ "," ,end="")


# for i in range(len(strs)):
#     print(strs[i].split())
    

# take the first word from the first string
# check if it is there in the other strings
# if not, return false
# else, take the second word from the first string and repeat
# return the prefix before which it stops returning false

# for i in range(len(strs)):
#     for j in range(len(strs[i])):
#         if strs[i][j] in strs[i]:
#             print(f"{strs[i][j]} is there in the rest of the strings")
        
#         print(strs[i][j])

# split the strings in strs and construct an array
# sort the array strings with respect to the length of the strings
# check if the first string is there in the other strings
# if there, return it
# else pop the last element from the first string and check again 
# continue the same process and return the longest string

sortedStrings = strs.sort(key= len)
print(strs)
count =0 # to check if all the strings have been checked 
i=0
while(len(strs[0])>=1):
# for i in range(1,len(strs[0])) :
    # print(strs[0][-1])
    print(len(strs[0]))
    if str(strs[0]) in strs[i]:
            # print(f"i is {i} and strs[i] is {strs[i]}") 
            count +=1
    if count != len(strs)-1:
        strs[0] = strs[0].strip(strs[0][-1])
        i+=1
        print(strs[0])
    if len(strs[0]) ==1 and strs[i][0] != strs[0]:
        print("")
        

    
