ls=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    ele=input(f"Enter element {i+1}: ")
    ls.append(ele)
cp=[]
for i in ls:
    if i not in cp:
        cp.append(i)
print("The original list: ",ls)
print("unique list: ",cp)