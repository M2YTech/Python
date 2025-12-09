def myFunc():
    print("Hello World")



if __name__ == "__main__":
    # This block will only run if the script is executed directly
    print("we are directly running this code")
    myFunc()
    print(__name__)
# if __name__ == "__main__":
#     myFunc()
# #The __name__ variable is a built-in variable in Python that is used to determine 
# # whether a Python script is being run as the main program or if it is being 
# imported as a module in another script.
# # If the script is being run as the main program, __name__ will be set to "__main__".
# # If the script is being imported as a module, __name__ will be set to the name of the module.
# # This is useful for writing code that can be reused in other scripts without executing it when imported.
# # The if __name__ == "__main__": block is used to check if the script is being run as the main program.
# # If it is, the code inside the block will be executed. If it is not, the code inside the block will not be executed.