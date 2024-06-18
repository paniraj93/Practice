plt=100
# getting the number of plates from the user
x = int(input("Enter the  number of plates you need : "))
ttlp=plt*x
if (ttlp>250):
    dis=40
    gp=ttlp-dis
    print("===============================")
    print("item\tcost\tQTY\t total")
    print("UPMA\t",plt,"\t",x,"\t",ttlp)
    print("Discount :\t\t",dis)
    print("grand total :\t\t",gp)
    print("===============================")
else:
    print("===============================")
    print("Item\tCost\tQTY\t Total")
    print("UPMA\t",plt,"\t",x,"\t",ttlp)
    print("grand total :\t\t",ttlp)
    print("===============================")