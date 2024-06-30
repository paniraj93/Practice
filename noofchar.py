for i in range(5):
    while True:
        s=str(input("Enter the string %d: "%(i+1)))
        if (len(s)>5):
            print(s)
            break
        print("The string %d is too small please enter again"%(i+1))