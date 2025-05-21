def sum_of_first_n(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n + sum_of_first_n(n-1)
    
print(sum_of_first_n(4))
