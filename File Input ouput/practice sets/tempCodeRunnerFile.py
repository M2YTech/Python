with open("practice sets/log.txt") as f:
    lines = f.readlines()

lineno =1 
for line in lines:
    if("python" in line):
        print(f"Python is present in the file, on line no: {lineno}")
        break
    line += 1
else:
    print("Python is not present")