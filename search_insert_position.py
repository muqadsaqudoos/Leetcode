class Solution:
    def searchInsert(self, nums, target: int) -> int:
        
        i = 0
        while(i<len(nums)):
            if nums[i] < target:
                i += 1
            
            elif nums[i] == target:
                return i

            else:
                return i
        return i