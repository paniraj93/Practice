<<<<<<< HEAD
elements = list(map(int, input('Enter values saperated by space: ').split()))
minn = maxx = elements[0]
n = len(elements)
for i in range(1,n):
    if maxx < elements[i]:
        maxx = elements[i]
    elif minn > elements[i]:
        minn = elements[i]
=======
elements = list(map(int, input('Enter values saperated by space: ').split()))
minn = maxx = elements[0]
n = len(elements)
for i in range(1,n):
    if maxx < elements[i]:
        maxx = elements[i]
    elif minn > elements[i]:
        minn = elements[i]
>>>>>>> 1e4374c3a874f037ba1cfe876b6707251617a4f1
print(elements)