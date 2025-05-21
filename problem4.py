import os

# Specify the directory you want to list
directory = input("Enter the directory path: ")

try:
    # Use os.listdir() to get the list of files and folders
    contents = os.listdir(directory)
    
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the specified directory.")
