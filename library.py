#Ask the user to enter the number of days the book return is delayed
days=int(input(""))
if days != 0:
    if days<6:
        print("$%d"%15)
    elif days<11:
        print("$%d"%50)
    elif days<30:
        print("$%d"%100)
    else:
        print("membership revoked")