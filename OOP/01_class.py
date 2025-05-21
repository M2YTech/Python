class Employee:
    Language = "Python" # this is a class attribute
    salary = 1100000

muhammad = Employee()# muhammad is an object here
muhammad.name = "Muhammad"# this is an object/instance attribute
print(muhammad.name, muhammad.salary, muhammad.Language)

ahmed = Employee()
ahmed.name = "Ahmed"
print(ahmed.name, ahmed.Language, ahmed.salary)

# Here name is object/instance attribute and salary and language are class attrubutes 
# as they directly belongs to the class