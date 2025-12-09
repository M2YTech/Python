from functools import reduce
l = [1,2,6,4,5]

result = reduce(lambda a,b: a if a>b else b, l)
print(result)

