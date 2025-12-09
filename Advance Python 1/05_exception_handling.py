try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)

# In this code, we are using try and except block to handle exceptions.
# If an exception occurs in the try block, the code in the except block will be executed.
# This is useful for handling errors gracefully without crashing the program.
# The except block can also be used to catch specific exceptions.

try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)