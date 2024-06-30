n = input("Enter the number")
cnt1 = len(n)//3
cnt2 = len(n)-cnt1
s = ''
print(cnt1,cnt2)
for i in range(cnt1):
    s = s + '999'
print((int(n)*2)-int(s)-1000)