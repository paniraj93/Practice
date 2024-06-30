def search(str,sstr,ls,lb):
    for i in range(lb-ls):
        if str[i:i+ls] == sstr:
            print("Found at index", i)
            return 1

if __name__ == "__main__":
    s = input()
    p = input()
    search(s,p,len(p),len(s))