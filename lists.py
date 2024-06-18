ls=[]
lim='yes'
while lim.lower()=='yes':
    ele=input(f"Enter element: ")
    ls.append(ele)
    lim=input("Do you want to continue yes|no ")
print(ls)