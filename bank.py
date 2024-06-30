import random
name=[]
acno=[]
lim=[]
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. View")
    print("3. Delete")
    print("4. EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        nm=input("Enter Username: ")
        while True:
            ac=random.randint(0,999999)
            if ac not in acno:
                print("Generating A/C number: ",ac)
                tl=int(input("Enter Limit: "))
                name.append(nm)
                acno.append(ac)
                lim.append(tl)
                print("Beneficiary added successfully")
                break
    elif ch==2:
        if len(name)==0:
            print("Beneficiary list is empty\nGoing back to main menu")
        else:
            print("Username\t\tAccount\t\tLimit")
            for i in range(len(name)):
                print("%10s\t\t%6d\t\t%6d"%(name[i],acno[i],lim[i]))
    elif ch==3:
        nm=input("Enter Username: ")
        ac=int(input("Enter A/C Number: "))
        for i in range(len(name)):
            if name[i]==nm and acno[i]==ac:
                tn=name[i]
                tac=acno[i]
                ttl=lim[i]
                del name[i]
                del acno[i]
                del lim[i]
                print(tn,"holding the account NO",tac,"has been removed")
                break
    elif ch==4:
        break
    else:
        print("Invalid Choice")