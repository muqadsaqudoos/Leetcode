class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dicty = {}
        s = s1.split()+s2.split()
        for word in s:
            if word not in dicty:
                dicty[word] = 1
            else:
                dicty[word] += 1
                

    
        l1 = []    
        for key in dicty.keys():
            if dicty[key] == 1:
                l1.append(key)
        return l1
            