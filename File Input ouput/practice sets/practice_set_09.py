with open("practice sets/first file.txt") as f1, open("practice sets/second file.txt") as f2:
    content1 = f1.read()
    content2 = f2.read()
    if(content1 == content2):
        print("Yes the content of both files are same.")
    else:
        print("No the content of both files are not the same.")