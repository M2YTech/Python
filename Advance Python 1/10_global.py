a = 89
def fun():
    global a
    # This will change the value of the global variable 'a'
    a= 3
    print(a)

fun()
print(a)