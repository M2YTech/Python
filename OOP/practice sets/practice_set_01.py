class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
p = Programmer("Muhamamd", 1100000, "Python")
print(p.name, p.salary, p.language, p.company)