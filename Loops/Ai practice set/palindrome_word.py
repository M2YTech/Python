word=input("Enter a word: ")
reverse_word = ""
palindrom =""
for char in word:
    reverse_word = char + reverse_word
if(reverse_word==word):
    print("the word is palindrome")
else:
    print("it is not a palindrome")
   
