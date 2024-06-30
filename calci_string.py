inp = input("enter the string: ")
n = list(map(float, inp.split('+' or '-' or '*' or '/' or '//' or '**')))
for _ in inp:
    if _ == '+':
        print(n[0]+n[1])
    elif _ == '-':
        print(n[0]-n[1])
    elif _ == '*':
        print(n[0]*n[1])
    elif _ == '/':
        print(n[0]/n[1])
    elif _ == '//':
        print(n[0]//n[1])
    elif _ == '**':
        print(n[0]**n[1])