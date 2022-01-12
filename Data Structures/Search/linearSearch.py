# Code to implement linear search algorithm

def linearSearch(arr, search):
    for i in range(len(arr)):
        if arr[i]==search:
            return i
    return -1


nums= [42,5,2,6,7,2,6,8,67,2]
key= 67
result= linearSearch(nums,key)
print(result)