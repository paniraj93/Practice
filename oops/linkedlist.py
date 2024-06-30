class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        if self.head==None:
            print("ll is null")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
    
    def createlist(self,num):
        n = num
        if n==0:
            return
        for i in range(n):
            data = int(input("Enter the data: "))
            if i==0:
                self.head = node(data)
                temp = self.head
            else:
                temp.next = node(data)
                temp = temp.next
        temp.next = None
        self.printlist()
        
    def deletenode(self,data):
        if self.head==None:
            print("ll is null")
            return
        else:
            prev = temp = self.head
            if temp.data==data:
                self.head = temp.next
                temp = None
                return
            else:
                while temp.next.data!=data:
                    temp = temp.next
                temp.next = temp.next.next
            self.printlist()
            
    def insertnode(self,data,val):
        if self.head==None:
            self.head.data = data
            self.printlist()
            return
        else:
            prev = self.head
            temp = self.head.next
            frd = temp.next
            if prev.data==data:
                new = node(val)
                self.head.next = new
                new.next = temp
                temp = None
                return
            else:
                while temp.data!=data:
                    temp = temp.next
                    frd = frd.next
                new = node(val)
                temp.next = new
                new.next = frd
            self.printlist()
    
    def frontinsert(self,data):
        if self.head==None:
            self.head.data = data
            self.printlist()
            return
        temp = self.head
        new = node(data)
        head = new
        new.next = temp
        self.printlist()
    
    def lastinsert(self,data):
        if self.head==None:
            self.head.data = data
            self.printlist()
            return
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        new = node(data)
        temp.next = new
        self.printlist()
        
    def frontdelete(self):
        if self.head==None:
            print("ll is null")
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.printlist()
            
    def lastdelete(self):
        if self.head==None:
            print("ll is null")
            return
        else:
            temp = self.head
            while temp.next.next!=None:
                temp = temp.next
            temp.next = None
            self.printlist()
        
if __name__=='__main__':
    ll = linkedlist()
    ll.createlist(int(input("Enter the number of nodes: ")))
    while(True):
        print("SELECT FROM THE OPTIONS\n1. insert front\n2. rear insert\n3. mid insert\n4. front delete\n")
        ll.deletenode(int(input("Enter the data to delete node: ")))
        ll.insertnode(int(input("Enter the data to insert next: ")),int(input("Enter the data to node: ")))