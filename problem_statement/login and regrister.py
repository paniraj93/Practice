''' WAP to build a login system using fuctions.
the function name should be login and regrister.
1. it should ask user to enter the details for regristration and out of all these details only username and password should be stored
2.now this function shoule ask user to enter username and password.if these match with the regristered details login successful otherwise repeate this process of login saying that its invalid'''
import os
def login_and_regrister():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    name = input("Enter user name: ")
    password = input("Enter password: ")
    email = input("Enter your email: ")
    
    os.system("cls")
    
    users = {}
    users[name] = password
    t = True
    
    while(t):
        print("LOGIN PAGE")
        u_name = input("Enter user name: ")
        if u_name in users:
            t = False
            while(True):
                u_pass = input("Enter your password: ")
                if u_pass == users[u_name]:
                    print("SUCCESSFUL LOGIN")
                    break
                else:
                    print("INVALID CREDENITALS")
        else:
            print("USER NAME NOT FOUND")
    
if __name__=="__main__":
    login_and_regrister()
        