cnt={}
nam=input("Enter the name: ")
nam=nam.lower()
for i in nam:
    cnt[i]=nam.count(i)
print(cnt)