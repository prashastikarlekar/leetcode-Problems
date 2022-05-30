# code to implement binary search
def binarySearch(arr, low, high, searchItem):
    if high >=low:
        mid = int((low+high)//2)
        if arr[mid] == searchItem:
            return mid
        elif arr[mid] > searchItem:
            return binarySearch(arr,low,mid-1,searchItem)
        else:
            return binarySearch(arr,mid+1, high, searchItem)

    else:
        return -1


# two sum problem
# nums=[2,11,15,7] # 0,3
nums=[3,2,3]
# # numsSorted = [0,1,2,4,5,7,8]
target=6
numsSorted = sorted(nums) # 2,7,11,15       2,3,3
for i in range(len(numsSorted)): #3,3,4
    complement = target- numsSorted[i]
    if binarySearch(nums, 0, len(numsSorted)-1,complement) !=-1 :
        numIndex= nums.index(numsSorted[i])
        # print("the indexes are {0}, {1}".format(nums.index(complement), nums.index(numsSorted[i],i+1)))
        if numsSorted[i] == complement:
            complementIndex = nums.index(complement,i+1)
        else:
            complementIndex= nums.index(complement)

            result=[numIndex,complementIndex]
            print(result)
    




#  def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         numsSorted= nums.copy()
#         numsSorted.sort()
        
        
#         for i in range(len(nums)):
            
#             originalNumber = numsSorted[i]
#             complement = target- originalNumber
            
#             if binarySearch(numsSorted, 0, len(numsSorted)-1,complement)!=-1:
#                 indexOfOrig = nums.index(originalNumber) 
                
                
#                 if(complement == originalNumber):
#                     indexOfComp = nums.index(complement,indexOfOrig+1 ) 
#                 else:
#                     indexOfComp = nums.index(complement ) 
                    
                
#                 result = [indexOfOrig,indexOfComp]
#                 return result