s=str(input("Enter the string: "))
l=len(s)
if l<3:
    print(s)
elif s[-3:]=="ing":
    print(s[:-3]+"ly")
else:
    print(s+"ing")