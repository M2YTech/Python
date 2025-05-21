# Create a class with a class attribute a; create an object from it and set ‘a’ 
# # directly using ‘object.a = 0’. Does this change the class attribute? 
class Problem3:
    a = 4

c = Problem3()
print(c.a)#print the class attribute because instance attribute is not present
c.a = 5#instance attribute is set
print(c.a)#print the class attribute because instance attribute is present
print(Problem3.a)#prints the class attribute