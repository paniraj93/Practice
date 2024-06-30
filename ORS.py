# getting the number from the user
x = int(input("Enter the two digit number : "))
n1 = x//10
n2 = x%10
y = n1+(n2*10)
res = x+y
print(res)