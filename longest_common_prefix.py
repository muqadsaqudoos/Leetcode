def longest_common_prefix(strs):
    a = strs[0]
    for s in (strs[1:]):
        j =0
        while j< len(a) and j < len(s) and a[j] == s[j]:
            j += 1

        a = a[:j]

    if len(a) == 0:
        return None
    return a

print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))