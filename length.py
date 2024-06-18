s=str(input("Enter the string: "))
arr=s.split()
size=0
for a in arr:
    if len(a)>size:
        size=len(a)
print(size)