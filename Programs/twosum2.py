# # second try
# def binarySearch(arr,low,high,searchTerm):
#     if low<=high:
#         mid= int((low+high)/2)
#         if arr[mid] == searchTerm:
#             return mid
#         elif arr[mid] < searchTerm:
#             return binarySearch(arr,mid+1,high,searchTerm)
#         else:
#             return binarySearch(arr,low,mid-1,searchTerm)
#     return -1

# nums = [2,7,11,15]
# # nums =[3,2,3]
# numsSorted = sorted(nums) # 2,3,3
# target = 9
# for i in range(len(numsSorted)):
#     complement= target - numsSorted[i]
#     if binarySearch(numsSorted, i+1, len(numsSorted)-1, complement) !=-1:
#         originalIndex = nums.index(numsSorted[i])
#         if complement == numsSorted[i]:
#             complementIndex = nums.index(complement, originalIndex+1)
#         else:
#             complementIndex = nums.index(complement)

# result = [originalIndex, complementIndex]
# print(result)
    


def binarySearh(arr, low, high, searcg):
    if low <high:
    
        mid = int((low+ high)/2)
        if searcg == mid:
            return mid
        elif arr[mid] < searcg:
            return binarySearh(low, mid, searcg)
        else: # arr[mid] > searcg
            binarySearh(mid+1, high, searcg)

if __name__== "__main__":

    number = int(input("Enter the number of elements"))
    numbers = []
    for i in range(numbers):
        element = int(input("Enter the element "))
        numbers.append(element)
    
    

    



    

