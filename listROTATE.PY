ls=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    ele=input(f"Enter element {i+1}: ")
    ls.append(ele)
sh=int(input("Enter the number of elements you want to shift: "))
print("The original list: ",ls)
print("Shifted list: ",ls[sh:]+ls[:sh])