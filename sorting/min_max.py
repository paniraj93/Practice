elements = list(map(int, input('Enter values saperated by space: ').split()))
minn = maxx = elements[0]
n = len(elements)
for i in range(1,n):
    if maxx < elements[i]:
        maxx = elements[i]
    elif minn > elements[i]:
        minn = elements[i]
print(elements)