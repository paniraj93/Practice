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
    print("VALID EXPRESSION")