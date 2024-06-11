lst = list(map(int, input().split()))
s = 0
c0 =0
c1 = 0
c2 = 0
e = len(lst)
for i in lst:
    if i == 0:
        c0 += 1
    elif i == 1:
        c1 += 1
    else:
        c2 += 1

c1 = c0 + c2

print(f"{c0}{c1}{c2}")
for i in range(e):
    if i<c0:
        lst[i]=0
    elif i<c1:
        lst[i]=1
    else:
        lst[i]=2
print(lst)