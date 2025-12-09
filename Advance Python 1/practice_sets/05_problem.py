import os
print("Saving table to:", os.getcwd())
n = int(input("Enter a number: "))
with open("practice_sets\Table.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{n} X {i} = {n*i}\n")
