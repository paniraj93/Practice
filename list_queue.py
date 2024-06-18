que=[]
# Function to add a element in queue
def insert():
    if len(que)==lim:
        print("QUEUE IS FULL!")
    else:
        que.append(int(input("ENTER the element: ")))
        print("Element added successfully")

# Function to remove a element from queue
def remove():
    if len(que)==0:
        print("QUEUE IS EMPTY!")
    else:
        e=que.pop(0)
        print("ELEMENt",e,"popped")

#Function to display queue
def display():
    if len(que)==0:
        print("QUEUE IS EMPTY!")
    else:
        print(que)

lim=int(input("Enter the limit of the QUEUE: "))
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        insert()
    elif ch==2:
        remove()
    elif ch==3:
        display()
    elif ch==4:
        break