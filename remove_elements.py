class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = j = k =  0
        while(i<len(nums)):
            if nums[i] == val:
                i +=1

            else: 
                nums[j] = nums[i]
                j += 1 
                i += 1
                k += 1

        return k