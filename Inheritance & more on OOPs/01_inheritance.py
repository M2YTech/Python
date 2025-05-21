class Employee:
    company = "PAK"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
# instead of this:
# class Programmer:
#     company = "PAK 2"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is very good with {self.language} Language")

# we use this:
class Programmer(Employee):
    def showLanguage(self):
        print(f"The name is {self.name} and he is very good with {self.language} Language")

a = Employee()
b = Programmer()
print(a.company)
print(b.company)