class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def Insert(self,v,cont,cplus,cs):
        nn=Node(v)
        if cs==1:
            self.cse=1
            if self.head==None:
                self.head=nn
                self.nod=self.head
                self.top=None
            elif self.top!=self.head:
                temp=self.head
                while temp.next!=None:
                    temp=temp.next
                temp.next=nn
                self.top=temp.next
            if cont==cplus:
                    self.top.next=self.head
        else:
            print("QUEUE IS FULL")

    def display(self):
        t=self.head
        if t==None:
            print("Empty stack")
        else:
            while True:
                print(t.data)
                if t==self.top:
                    break
                t=t.next

    def peek(self):
        print(self.head.data,"is top")

    def remove(self):
        self.head=self.head.next
        self.top.next=None

nn=Linked_list()
c=int(input("Enter the size: "))
cnt=0
cse=1
while True:
    print("\n1. Insert\n2. Display\n3. Peek\n4. Delete\n5. Exit")
    n=int(input("Enter the choice: "))
    if n==1:
        ele=int(input("Enter the element: "))
        print(cse)
        print(cnt)
        if cnt==c:
            cse=0
        cnt=cnt+1
        nn.Insert(ele,c,cnt,cse)
    elif n==2:
        nn.display()
        stk=[]
    elif n==3:
        nn.peek()
    elif n==4:
        cnt=cnt-1
        cse=1
        nn.remove()
    elif n==5:
        break