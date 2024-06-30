import sqlite3
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Update password")
    print("4. exit")
    choice = input("Select an option: ")
    if choice == '1':
        #Get data to register a new user
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        conn = sqlite3.connect("user_db.sqlite")
        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already exists. Please choose a different one.")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print("User registered successfully.")

        conn.close()
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        conn = sqlite3.connect("user_db.sqlite")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            print("Login successful. Welcome, " + username + "!")
        else:
            print("Login failed. Please check your username and password.")

        conn.close()
    elif choice == '3':
        username = input("Enter your username: ")
        
        conn = sqlite3.connect("user_db.sqlite")
        cursor = conn.cursor()
        # Check for the username exists
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            npd=("Enter new password: ")
            cpd=("Conform password: ")
            if cpd==npd:
                cursor.execute("INSERT INTO users (password) VALUES (?)", (npd))
                conn.commit()
                print("Password updated successfully.")
        else:
            print("USER NOT FOUND!s")
    elif choice == '4':
        print("GOODBYE")
        break