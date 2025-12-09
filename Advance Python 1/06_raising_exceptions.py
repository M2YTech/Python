a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if(b==0):
    raise ZeroDivisionError("Division by zero is not allowed")
else:
    print(f"The answer is {a/b}")
# In this code, we are using the raise statement to raise a ZeroDivisionError exception if the user tries to divide by zero.
# This is useful for enforcing constraints in your code and providing meaningful error messages.
# The raise statement can also be used to raise custom exceptions.
# in this case the program did crash because we want the developer to know that this is a bug in the code
# and we want to fix it
# 
#
