class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def midpoint(p1,p2):
        mx=(p1.x+p2.x)/2
        my=(p1.y+p2.y)/2
        return point(mx,my)
p=point(2,7)
q=point(4,3)
r=p.midpoint(q)
print(str(r))