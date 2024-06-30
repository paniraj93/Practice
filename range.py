#Getting the in put from the user
a=int(input("enter the starting number: "))
b=int(input("enter the ending number: "))
if b>a:
    for i in range(a,(b+1)):
        print(i,end=' ')
else:
    for i in range(a,(b-1),-1):
        print(i,end=' ')
