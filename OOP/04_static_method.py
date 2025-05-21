# Sometimes we need a function that does not use the self-parameter. We can define a 
# static method like this: 

class Employee:
    language = "Python" 
    salary = 1100000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")
muhammad = Employee()
muhammad.getinfo()
# Employee.getinfo(muhammad)
muhammad.greet()
