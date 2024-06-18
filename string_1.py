s=str(input("Enter the string: "))
if len(s)>2:
    print(s[-1]+s[1:-1]+s[0])
else:
    print("String is too short")