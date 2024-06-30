# getting the number of minutes from the user
n = int(input("Enter the number of minutes: "))
d=n//(60*24)
hrs=(n%(60*24))//60
min=(n%(60*24))%60
'''hrs, min = divmod(n, 60)
d, hrs = divmod(hrs, 24)'''
print(int(d)," days,",int(hrs)," hours,",int(min)," minutes")