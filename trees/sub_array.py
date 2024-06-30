def max_subarray():
    l=[-2 ,-3 ,4,-1,-2,1,5,-3]
    max_sum_1=l[0]
    max_sum_2=l[0]
    for i in range(1,len(l)):
        print("1:  ",l[i]," + ",max_sum_1+l[i])
        max_sum_1=max(l[i],max_sum_1+l[i])
        print(max_sum_1)
        print("2: ",max_sum_1," + ",max_sum_2)
        max_sum_2=max(max_sum_1,max_sum_2)
        print(max_sum_2)
    return max_sum_2

print("Maximum contiguous sum is",max_subarray())