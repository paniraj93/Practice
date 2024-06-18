class circle:
    pi=3.14159
    def __init__(self,r):
        self.rds=r
    def area(self):
        return self.pi*self.rds**2
    
c1=circle(7)
c2=circle(14)
print("Radius=%.2f and Area=%.2f"%(c1.rds,c1.area()))
print("Radius=%.2f and Area=%.2f"%(c2.rds,c2.area()))