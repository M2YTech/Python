class Employee:
    company = "PAK"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Here is your by default langugage: {self.language}")
class Programmer(Employee, Coder):
    def showLanguage(self):
        print(f"The name is {self.company} and he is very good with {self.language} Language")

a = Employee()
b = Programmer()
print(a.company)
print(b.company)
b.showLanguage()