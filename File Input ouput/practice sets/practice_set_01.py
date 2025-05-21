f = open("poem.txt")
data = f.read().lower()
# word = input("Enter a word: ").lower()
if("twinkle" in data):
    # print(f"{word} is in the file.")
    print("The word twinkle is in the file.")
else:
    # print(f"{word} does not exist in the file.")
    print("The word twinkle is not in the file.")
f.close()