def isPalindrome(x: int) -> bool:
    temp = x
    rev_no = 0
    while temp > 0:
        a = temp % 10
        rev_no = (rev_no*10) + a
        temp = temp //10

    if x == rev_no :
        return True
    else:
        return False
        

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))