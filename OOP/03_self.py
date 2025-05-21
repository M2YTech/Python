class Employee:
    language = "Python" 
    salary = 1100000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Good morning")
muhammad = Employee()
muhammad.getinfo()
# Employee.getinfo(muhammad)
muhammad.greet()
