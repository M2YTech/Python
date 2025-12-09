def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
    except ValueError as v:
        print(v)

    finally:
        print("hey i am inside finally block")

main()
#finally is used in functions when you want to run a specifc block of code even 
# if the try block raises an exception.