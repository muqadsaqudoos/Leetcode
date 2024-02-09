def roman_to_integar(s):
   
    a = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    i = 0
    sum = 0
    while (i<len(s)):
        if i == len(s)-1:
            sum += a[s[i]]
            i+=1
        elif a[s[i]] >= a[s[i+1]]:
            sum += a[s[i]]
            i += 1
        else:
            diff = a[s[i+1]] - a[s[i]]
            sum += diff
            i += 2
    return sum

print(roman_to_integar("III"))
print(roman_to_integar("LVIII"))
print(roman_to_integar("MCMXCIV"))
        

    
