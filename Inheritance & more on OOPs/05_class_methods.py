class Employee:
    a= 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

b = Employee()
b.a = 45
b.show()