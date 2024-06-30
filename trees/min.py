l = [-3,6,-4,2,-5,-3,7]
min = 999

for i in l:
    if i < 0:
        continue
    else:
        if i < min:
            min = i
            
print(min)