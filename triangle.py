n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,2*i):
        if i != n:
            if k==1 or k==(2*i)-1:
                print("*",end='')
            else:
                print(" ",end='')
        else:
            print("*",end='')
    print()