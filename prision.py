p = int(input("Enter number of prisioners: "))
c = int(input("Enter number of chocolates: "))
s = int(input("Enter first number: "))
sol = (s+c-1)%p
if sol==0:
    sol =6; 
print(f"prisoner {sol} gets faulty chocolate")