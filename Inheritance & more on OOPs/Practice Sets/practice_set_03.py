class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    @property
    def get_incremented_salary(self):
        return self.salary * self.increment
    @get_incremented_salary.setter
    def get_incremented_salary(self, value):
        self.increment = value/self.salary

e = Employee(1000, 1.1)
print(e.get_incremented_salary)
e.get_incremented_salary = 1200
print(e.increment)