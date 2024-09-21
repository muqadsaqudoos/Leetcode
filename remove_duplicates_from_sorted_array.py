class Solution:
    def removeDuplicates(self, nums) -> int:
        j = k = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                i+=1

            else:
                i+=1
                k+=1
                nums[j] = nums[i]
                j+=1

            
        return k
        