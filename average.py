#enter the number
n = int(input("Enter the number of elements: "))
sum=0
print("Enter the elements one by one: ")
for i in range(n):
    n=int(input())
    sum=sum+n
res=sum/n
print("Average is %.2f"%res)