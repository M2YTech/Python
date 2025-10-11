class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name of the student: {self.name} and age of the student: {self.age}")


class Student(Person):
    def __init__(self,name,age ,student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

person = Person("Ali", 10)
person.display()

student = Student("Ahmed", 11, 1)
student.display()

    