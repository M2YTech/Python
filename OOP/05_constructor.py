class Employee:
    language = "Python" 
    salary = 1100000

    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

muhammad = Employee("Muhmmad", 1200000, "C++")
# muhammad.name = "Muhammad"
print(muhammad.name, muhammad.salary, muhammad.language)
