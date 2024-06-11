# calculate the sum of digits of a number where each digit is powered to its position in number
num=int(input("Enter number: "))
t = num
des = 0
pow = 0
if num is not None:
    while(t>0):
        t = t//10
        pow += 1
    while(pow>0):
        rem = num%10
        des = des + rem**pow
        num = num//10
        pow -= 1
    print(des)