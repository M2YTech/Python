f = open("file.txt")
print(f.read())
f.close()

# same can be done using with statement 
with open("file.txt") as f:
    print(f.read())

# you do not have to close the file explicitly