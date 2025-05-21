sentence = input("Enter a sentence: ")
vowels = ["a","e","i","o","u"]
vowel_count = 0
consonant_count = 0
for  j in sentence:
    if(j.isalpha()):
        if(j.lower() in vowels):
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
    
print("Total vowels are: ", vowel_count)
print("Total consonant are: ", consonant_count)



