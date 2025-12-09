def dig_pow(n, p):
    n = str(n)
    final = 0
    for i in n:
        final += int(i)**p
        p+=1
        k = int(final/int(n))
    if k*int(n) == final:
        return k
        
    return -1


print(dig_pow(46288, 3))