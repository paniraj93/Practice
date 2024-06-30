s=str(input("Enter the string: "))
var=s[0]
for i in range(1,len(s)):
    if s[i].lower()==var.lower():
        s=s[:i]+'$'+s[i+1:]
print(s)