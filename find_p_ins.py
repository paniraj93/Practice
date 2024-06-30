res = []
def substring_instring(s,p):
    for i in range(len(s)-len(p)+1):
        if s[i:i+len(p)]==p:
            res.append(i)
    return res

s = input()
p = input()

print(substring_instring(s,p))