std={}
# Getting username and password from user
for _ in range(3):
    un=input("Enter the Username: ")
    std[un]=int(input("Enter Password: "))
print("Database created")
while True:
    un=input("Enter the Username: ")
    if un in std:
        pwd=int(input("Enter Password: "))
        if std[un]==pwd:
            print("welcome ",un)
            break
        else:
            print("Username and password not found try again")
    else:
        print("User not found try again")