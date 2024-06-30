def min(l):
    min = 999

    for i in l:
        if i < 0:
            continue
        else:
            if i < min:
                min = i
    return min

nums = list(map(int, input("comma separated values: ").split()))
nums.sort()
result=1
for i in nums:
    if result == i:
        result += 1
print(result)