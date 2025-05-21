class Employee:
    a = 1
    def __init__(self):
        print("constructor of Employee")

class Programmer(Employee):
    b = 2
    def __init__(self):
        print("constructor of Programmer")

class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("constructor of Manager")


o = Employee()
print(o.a)
o = Programmer()
print(o.a, o.b)
o = Manager()
print(o.a, o.b, o.c)
