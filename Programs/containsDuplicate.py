from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dictionary={}
        for i in range(len(nums)):
            if nums[i] in dictionary.keys():
                return True
            else:
                dictionary[nums[i]] = 1
        return False

nums=[1,2,3,1]
sol= Solution()
print(sol.containsDuplicate(nums=nums))
