names = ["Muhammad", "Ahmed", "Amina", "Sawaiba"]
user_name = input("Enter your name: ")
for name in names:
    if name == user_name:
        print(user_name, " is found")
        break
else:
    print(user_name, " not found")