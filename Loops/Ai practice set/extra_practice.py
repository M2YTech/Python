sentence = input("Enter a sentence: ")#takes input from the use
vowels =["a","e","i","o","u"]#list of vowels
for  j in sentence:#for loop value of sentence is stored in j here
    if(j.lower() in vowels):#condition check the sentence contain character which are in list after changing them to lower form
        print(j)#print those vowles which matches the condition