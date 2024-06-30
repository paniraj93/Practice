#start=temp=None
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
    def display(self):
        t=self.head
        if t==None:
            print("Empty LL")
        else:
            while t.next!=None:
                print(t.data)
                t=t.next
            print(t.data)
    def delete(self):
        print("\n1. Front\n2. Last")
        dch=input("Enter where you want to delete: ")
        temp=self.head
        match dch:
            case '1':
                self.head=temp.next
                print(temp.data,"Deleted")
            case '2':
                while temp.next!=None:
                    temp=temp.next
                print(temp.data,"deleted")
    def search(self):
        temp=self.head
        c=1
        s=int(input("Enter the element you want to search: "))
        while temp.next!=None:
            c=c+1
            if temp.data==s:
                print("ELEMENT",s,"FOUND AT",c,"POSITION")
            temp=temp.next
        if temp.data==s:
            print("ELEMENT",s,"FOUND AT",c,"POSITION")
        else:
            print("ELEMENT NOT FOUND")


nn=Linked_list()
while True:
    print("\n1. Insert\n2. Display\n3. Delete\n4. Search\n5. Exit")
    n=int(input("Enter the choice: "))
    if n==1:
        ele=int(input("Enter the element: "))
        nn.Insert(ele)
    elif n==2:
        nn.display()
    elif n==3:
        nn.delete()
    elif n==4:
        nn.search()
    elif n==5:
        break