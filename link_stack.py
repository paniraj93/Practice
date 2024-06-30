stk=[]
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None


class Linked_list():
    def __init__(self):
        self.head=None

    def Insert(self,v):
        nn=Node(v)
        if self.head==None:
            self.head=nn
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=nn
            self.top=temp.next

    def display(self):
        '''t=self.head
        if t==None:
            print("Empty stack")
        else:
            while t.next!=None:
                stk.append(t.data)
                t=t.next
            stk.append(t.data)
            stk.reverse()
            print(stk)'''
        print(self.top.data,"is top")

    def delete(self):
        temp=self.head
        while temp.next!=None:
            prev=temp
            temp=temp.next
        print(temp.data,"deleted")
        prev.next=None
        self.top=prev
nn=Linked_list()
while True:
    print("\n1. Insert\n2. Display\n3. Delete\n4. Exit")
    n=int(input("Enter the choice: "))
    if n==1:
        ele=int(input("Enter the element: "))
        nn.Insert(ele)
    elif n==2:
        nn.display()
        stk=[]
    elif n==3:
        nn.delete()
    elif n==4:
        break