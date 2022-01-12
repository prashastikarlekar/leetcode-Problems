# Code to implement binary search alogorithm

def binarySearch(arr,low,high,search):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]== search:
            return mid
        elif arr[mid] < search:
            return binarySearch(arr,mid+1,high,search)
        else:
            return binarySearch(arr,low,mid,search)
    return -1
    


nums=[2,3,7,12,24,27,45,78]
result= binarySearch(nums, 0,len(nums)-1,12)
print(result)


