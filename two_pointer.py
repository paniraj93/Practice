'''python program which takes a list from user
l = [4,0,5,0,1,1,9,0,0]
then using two pointer approach
make it like this
l = [4,5,1,9,0,0,0,0]
i.e all non zero numbers at first and zer values at last'''

def rearrange_list(lst):
    left = 0
    right = 0
    n = len(lst)
    for left in range(n):
        if lst[left] != 0:
            lst[right]=lst[left]
            right += 1
            
    while right < n:
        lst[right]=0
        right += 1
        
    return lst
user_input = input("Enter a list of numbers separated by spaces: ")
lst = [int(x) for x in user_input.split()]

rearranged_lst = rearrange_list(lst)

print("Rearranged list:", rearranged_lst)