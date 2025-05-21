n = [1,2,3,4,5,6,7,8,9,10]
even_number = 0
odd_number = 0
for i in n:
    if(i%2==0):
        even_number += 1
    elif(i%2!=0):
        odd_number += 1
print("even number: ", even_number)
print("Odd number: ", odd_number)