# getting the number from the user
i = int(input("Enter the number (I) : "))
j = int(input("Enter the number (J) : "))
k=i+((i+(i%j))%j)
print(k)