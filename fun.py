#Function to add
def add(a,b):
    return (a+b)
#Function to subtract
def sub(a,b):
    return (a-b)
#Function to multiplication
def mul(a,b):
    return (a*b)
#Function to division
def div(a,b):
    return (a/b)
n1=float(input("Enter the first num: "))
op=input("Choose +,-,*,/ operation: ")
n2=float(input("Enter the second num: "))
if op=='+':
    print(f"{n1} + {n2} = {add(n1,n2)}")
elif op=='-':
    print(f"{n1} - {n2} = {add(n1,n2)}")
elif op=='*':
    print(f"{n1} * {n2} = {add(n1,n2)}")
elif op=='/':
    print(f"{n1} / {n2} = {add(n1,n2)}")
else:
    print("Invalid Choice")