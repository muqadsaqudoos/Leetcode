def sum_array(nums,target):
    dict1 = {v: k for k, v in enumerate(nums)}
    b = []
    for i in range(len(nums)):
        c = target - nums[i]
        if c in dict1 and i != dict1[c]:
            b.append(i)
            b.append(dict1[c])
            break

    return b

print(sum_array([2,7,11,15],9))
print(sum_array([3,3],6))
print(sum_array([3,2,3],6))
