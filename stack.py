stk=[]
#Function to add a element in stack
def push():
    if len(stk)==lim-1:
        print("Stack is Overflow")
    else:
        stk.append(int(input("Enter the element: ")))
        print("element added successfully")

#Function to remove a element in stack
def remove():
    if len(stk)==0:
        print("Stack is Underflow")
    else:
        print("element",stk.pop(),"successfully")

#Function to display the stack
def display():
    if len(stk)==0:
        print("Stack is Underflow")
    else:
        stk.reverse()
        print(stk)
        stk.reverse()

lim=int(input("Enter the limit of the stack: "))
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        push()
    elif ch==2:
        remove()
    elif ch==3:
        display()
    elif ch==4:
        break