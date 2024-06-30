def Rgcd(n1,n2):
    if n2==0:
        return n1
    else:
        return Rgcd(n2, n1%n2)
num1=int(input("Enter n1: "))
num2=int(input("Enter n2: "))
print(f"The GCD of {num1} and {num2} is : {Rgcd(num1,num2)}")