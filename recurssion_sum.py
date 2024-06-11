def rec_sum_dig(n):
    sum = 0
    if n == 0:
        return 0
    else:
        dig = n%10
        return dig + rec_sum_dig(n//10)
    
print(rec_sum_dig(int(input("Enter no: "))))