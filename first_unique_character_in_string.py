def f(s):
        count_dict = {}
        for element in s:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
        b = None
        for key, count in count_dict.items():
            if count == 1 :
                b = key 
                break
            
        for i in range(len(s)):
            if b == s[i]:
                return i
        return -1
        

print(f("leetcode"))
print(f("abba"))