import random
acnm={}
acbal={}
def cre():
    while True:
        ac=random.randint(100000,999999)
        if ac not in acnm:
            print("Generating A/C number: ",ac)
            acnm[ac]=input("Enter A/C holder name: ")
            acbal[ac]=int(input("Enter balance: "))
            print("Account Created")
            break
def dep():
    num=int(input("Enter the account number: "))
    if num in acnm:
        amount=int(input("Enter the amount to Deposit: "))
        tid=random.randint(10000,99999)
        typ='Deposit'
        acbal[num]=acbal[num]+amount
        print("Transaction ID\tAccount\ttype\tAmount\tAvailable balance")
        print("%5d\t\t%6d\t%8s\t%6d\t%6d"%(tid,num,typ,amount,acbal[num]))
    else:
        print("Account not found try again")
def wit():
    num=int(input("Enter the account number: "))
    if num in acnm:
        amount=int(input("Enter the amount to Withdraw: "))
        if amount<acbal[num]:
            tid=random.randint(10000,99999)
            typ='Withdraw'
            acbal[num]=acbal[num]-amount
            print("Transaction ID\tAccount\ttype\tAmount\tAvailable balance")
            print("%5d\t\t%6d\t%8s\t%6d\t%6d"%(tid,num,typ,amount,acbal[num]))
        else:
            print("Insufficient balance. Try again")
    else:
        print("Account not found try again")
def trn():
    n1=int(input("Enter your acc num: "))
    n2=int(input("Enter receiver acc num: "))
    if n1 in acnm and n2 in acnm:
        amt=int(input("Enter the amount you want to transfer: "))
        acbal[n1]=acbal[n1]-amt
        acbal[n2]=acbal[n2]+amt
        tid=random.randint(10000,99999)
        typ='Withdraw'
        print("Transaction ID\tAccount\ttype\tAmount\tAvailable balance")
        print("%5d\t\t%6d\t%8s\t%6d\t%6d"%(tid,n1,typ,amt,acbal[n1]))
        print("%5d\t\t%6d\t%8s\t%6d\t%6d"%(tid,n2,typ,amt,acbal[n2]))
    else:
        if n1 not in acnm:
            print("Your acc number is wrong")
        else:
            print("receiver acc number is wrong")
def view():
    if len(acnm)==0:
        print("NO ACCOUNTS!")
    else:
        print("Username\t\tAccount\t\tLimit")
        for i in acnm:
            print("%10s\t\t%6d\t\t%6d"%(acnm[i],i,acbal[i]))
def menu():
    while True:
        print("\nMenu:")
        print("1. Create ACC")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View")
        print("6. EXIT")
        ch=int(input("Enter your choice: "))
        if ch==1:
            cre()
        elif ch==2:
            dep()
        elif ch==3:
            wit()
        elif ch==4:
            trn()
        elif ch==5:
            view()
        elif ch==6:
            print("GOOD BYE!")
            break

#Main program starts from here
menu()