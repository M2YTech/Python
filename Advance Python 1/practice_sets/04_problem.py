try:
    a = int(input("Enter a number: ")) 
    b = int(input("Enter a number: ")) 
    print(f"The result of a/b is: {a/b}")
except ZeroDivisionError:
    print("Infinite")