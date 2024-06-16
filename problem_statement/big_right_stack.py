def opp(i):
    top = len(s) - 1
    if top == -1:
        s.append(inp[i])
        return -1
    else:
        while top >= 0 and s[top] <= inp[i]:
            s.pop()
            top -= 1
        if top == -1:
            s.append(inp[i])
            return -1
        else:
            result = s[top]
            s.append(inp[i])
            return result

s = []
inp = []
op = []

inp = list(map(int, input("Enter the numbers separated by space: ").split()))
d = -(len(inp)+1)
s.clear()

for i in range(len(inp)):
    op.append(opp(i))

print(reversed(op))


'''
def find_supervisors(arr):
    stack = []
    supervisors = []
    for num in reversed(arr):
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            supervisors.append(stack[-1])
        else:
            supervisors.append(-1)
        stack.append(num)
    return list(reversed(supervisors))

arr = list(map(int, input("Enter the numbers separated by space: ").split()))
#3 5 3 14 5 3 7 9 4 6 9 4 2 5 3
print(find_supervisors(arr))'''