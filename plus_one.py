class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        n = None
        for i in range(len(digits)):
            n = s*10
            s = n+digits[i]

        s = s+1
        return list(map(int,str(s)))
        