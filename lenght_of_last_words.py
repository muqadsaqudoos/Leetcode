class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip()
        count = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] != " ":
                count += 1

            else:
                return count

        return count