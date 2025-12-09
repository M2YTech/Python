def get_sum(a,b):
    if a>b:
        a,b = b,a
    total = 0
    for i in range(a, b+1):
        total+=i
    return total

print(get_sum(-1,2))