username="BITM"
password="533266"
while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Update password")
    print("3. exit")
    choice = input("Select an option: ")
    if choice == '1':
        user=input("Enter Username: ")
        pas=input("Enter Username: ")
        if username==user and password==pas:
            print("Login successful. Welcome, " + username + "!")
        else:
            print("Login failed. Please check your username and password.")
            print("IF FORGOTTEN PLEASE UPDATE YOUR PASSWORD")
    elif choice == '2':
        user=input("Enter Username: ")
        if username==user:
            npd=input("Enter new password: ")
            cpd=input("Conform password: ")
            if cpd==npd:
                password=npd
            else:
                print("PASSWORD DO NO MATCH")
        else:
            print("WRONG USERNAME")
    elif choice == '3':
        print("GOODBYE")
        break