n = [1,1,2,1,1]
k = 3
res = count = l = 0
for r in range(len(n)):
            if n[r] % 2:
                k -= 1
count = 0
while not k:
    k += (n[l] % 2)
    count += 1
    l += 1
res += count
print(res) 