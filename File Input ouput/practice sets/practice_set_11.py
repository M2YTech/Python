import os


os.rename("practice sets/old_filename.txt", "practice sets/new_filename.txt")
print("File renamed successfully.")
# If you want to make your script safer 
# (e.g., avoid crashing if the file doesn’t exist), you could add a chec
# import os

# old_path = "practice sets/old_filename.txt"
# new_path = "practice sets/renamed_by_python.txt"

# if os.path.exists(old_path):
#     os.rename(old_path, new_path)
#     print("File renamed successfully.")
# else:
#     print("The file does not exist.")