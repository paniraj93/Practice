l = [int(x) for x in range(100000)]
with open('list.txt','w') as f:
    f.write(str(l))