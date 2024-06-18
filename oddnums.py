# getting the number from the user
i = int(input("Enter the number (I) : "))
j = int(input("Enter the number (J) : "))
for k in range(i,j+1) or range(j,i+1):
    if k%2!=0:
        print(i,end=' ')
