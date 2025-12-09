filename = ["1.txt", "2.txt", "3.txt"]

for filename in filename:
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"The content of th f: {content}" )
    except FileNotFoundError:
        print(f"File not found: {filename}")
