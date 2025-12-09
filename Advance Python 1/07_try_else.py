try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print(v)

else:
    print("i am inside else block")

# if the try block does not raise an exception, the code in the else block will be executed.
