class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty1 = {}
        dicty2 = {}
        for item in s:
            if item not in dicty1:
                dicty1[item] = 1
            else:
                dicty1[item] += 1
        for item in t:
            if item not in dicty2:
                dicty2[item] = 1
            else:
                dicty2[item] += 1
        if dicty1 == dicty2:
            return True

        
        