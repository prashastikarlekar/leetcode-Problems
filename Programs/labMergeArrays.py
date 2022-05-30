# Write a Python program that merges two given lists together to a single sorted list.Hint:First you can sort both of the given lists 
# separately by the built-insort()method forlists.  Then compare the lists element-wise to obtain the final sorted list.  Let’s assume 
# we havetwo lists A: [2, 8, 7, 4] and B:[11, 1, 3].  After usingsort()on A and B, they become A: [2,4, 7, 8] and B:[1, 3, 11].  Then 
# we look at the first elements of both lists to find which one issmaller.  In this example, it is 1 from list B. This should be the 
# first element of our final sortedlist.  Then we move forward with B (index-wise) to compare with the first element of A. Fromthat we
#  get 2 as the second element of our sorted list.  Instead of list B, now we move forwardwith A. Using this same logic, we exhaust
#  through the end of both lists.  If we are done withone list earlier than the other one, we can just pick the remaining elements of 
# the other list asthe end part of our final sorted list.  The final sorted list from A and B should be [1, 2, 3, 4, 7,8, 11].

list1 = [2,8,7,4] # 2,4,7,8
list2= [11,1,3] # 1,3,11
list1.sort()
list2.sort()
result =[]
i=j=0
while i < (len(list1)) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i+=1
    else:
        result.append(list2[j])
        j+=1
for i in range(len(list1)):
    if list1[i] not in result:
        result.append(list1[i])
for j in range(len(list2)):
    if list2[j] not in result:
        result.append(list2[j])
          

print(result)