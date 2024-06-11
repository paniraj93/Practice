# calculate the sum of digits of a number where each digit is powered to no of didits
num=int(input("Enter number: "))
t = num
ams = 0
pow = 0
if num is not None:
    while(t>0):
        t = t//10
        pow += 1
    while(num>0):
        rem = num%10
        ams = ams + rem**pow
        num = num//10
    print(ams)
