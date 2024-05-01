class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        braces = "(){}[]"
        for i in s:
            if a:
                if  (a[-1] == "(" and i == ")") or (a[-1] == "{" and i == "}") or (a[-1] == "[" and i == "]"):
                     a.pop()
                else:
                    a.append(i)
            elif i in braces:
                a.append(i)

                   

        if len(a) == 0:
            return True
        else:
            return False
