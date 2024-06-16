black = ['a','c','e','g']
white = ['b','d','f','h']

inp = input("input: ")
if inp[:1] in black:
    if (int(inp[1:])%2==0):
        print("true")
    else:
        print("false")
elif inp[:1] in white:
    if (int(inp[1:])%2!=0):
        print("true")
    else:
        print("false")
else:
    print("INVALID CHESS BLOCK")
