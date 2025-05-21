with open("practice sets/log.txt") as f:
    content = f.read()

if("python" in content):
    print("Python is present in the file")
else:
    print("Python is not present")