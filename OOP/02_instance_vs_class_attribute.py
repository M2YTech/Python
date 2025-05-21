class Employee:
    Language = "Python" 
    salary = 1100000

muhammad = Employee()# muhammad is an object here
muhammad.Language = "Javascript"
print(muhammad.salary, muhammad.Language)

# Note: Instance attributes, take preference over class attributes during assignment & retrieval. 