def power(n,m):
    if m==0:
        return 1
    else:
        m -= 1
        return n * power(n,m)
        
    
if __name__ == "__main__":
    print(power(int(input("num one: ")),int(input("num two: "))))