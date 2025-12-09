l = [10,25,32,43,55]
def fifdiv(n):
    if(n%5==0):
        return True
    return False

onlyEven = filter(fifdiv, l)
print(list(onlyEven))
