# getting the number from the user
i = float(input())
j = float(input())
if j>i:
    print("Profit: $%.2f"%(j-i))
elif i==j:
    print("there is neither profit nor loss")
else:
    print("Loss: $%.2f"%(i-j))