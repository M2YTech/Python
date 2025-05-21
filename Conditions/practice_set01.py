a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
c = int(input("Enter first number: "))
d = int(input("Enter first number: "))
if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and a>d):
    print(c)
else:
    print(d)