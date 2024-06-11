import random
global dict 
students = {}
class college:
    def __init__(self,br):
        num = random.randint(100,999)
        usn = '3BR21' + br + str(num)
        while(True):
            if usn in students:
                num = random.randint(100,999)
                usn = '3BR21' + br + str(num)
            else:
                students[usn] = input("Enter your name: ")
                print(f"{students[usn]} Your usn is {usn}")
                break
                    
class department:
    def section():
        n = random.randint(1,4)
        if n==1:
            sec = 'A'
        elif n==2:
            sec = 'B'
        else:
            sec = 'C'
        return sec
    
if __name__ == "__main__":
    print("SELECT YOUR BRANCH\n1.CSE\n2.EEE\n3.ECE\n")
    while(True):
        ch = int(input("Enter your choice: "))
        if ch==1:
            branch = 'CS'
            break
        elif ch == 2:
            branch = 'EE'
            break
        elif ch == 3:
            branch = 'EC'
            break
        else:
            print("PLEASE CHOOSE THE VALID DEPARTMENT\n")
    s1 = college(branch)
    ss1 = department
    ss1.section()
    