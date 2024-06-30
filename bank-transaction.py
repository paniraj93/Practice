import random
opn_bnl=5000
avl_bln=5000
num=533266
bank=()
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View")
    print("4. EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        amount=int(input("Enter the amount to Deposit: "))
        tid=random.randint(10000,99999)
        typ='Deposit'
        avl_bln=avl_bln+amount
        bank=bank+((tid,num,typ,amount,avl_bln),)
        print("Deposit Successful")
    elif ch==2:
        amount=int(input("Enter the amount to Withdraw: "))
        if amount<avl_bln:
            tid=random.randint(10000,99999)
            typ='Withdraw'
            avl_bln=avl_bln-amount
            bank=bank+((tid,num,typ,amount,avl_bln),)
            print("withdraw successful")
        else:
            print("Insufficient balance. Try again")
    elif ch==3:
        if len(bank)==0:
            print("no transactions")
        else:
            print("Transaction ID\tAccount\ttype\tAmount\tAvailable balance")
            for i in bank:
                print("%5d\t\t%6d\t%8s\t%6d\t%6d"%(i))
    elif ch==4:
        print("GOODBYE")
        break
    else:
        print("Invalid Choice")