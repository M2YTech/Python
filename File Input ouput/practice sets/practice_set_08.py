with open("practice sets/this.txt") as f:
    content = f.read()
    with open("practice sets/copy.txt", "w") as f:
        f.write(content)