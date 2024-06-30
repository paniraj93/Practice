<<<<<<< HEAD
stk = ["$"]
t = 0
e = input()
print(e)
for I in e:
    if I == "(" or I == "{" or I == "[":
        stk.append(I)
        t += 1
    elif I == stk[t]:
        stk.pop()
        t -= 1
if stk[t] == '$':
    print("INVALID EXPRESSION")
else:
=======
stk = ["$"]
t = 0
e = input()
print(e)
for I in e:
    if I == "(" or I == "{" or I == "[":
        stk.append(I)
        t += 1
    elif I == stk[t]:
        stk.pop()
        t -= 1
if stk[t] == '$':
    print("INVALID EXPRESSION")
else:
>>>>>>> 1e4374c3a874f037ba1cfe876b6707251617a4f1
    print("VALID EXPRESSION")