class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @property
    def GPA(self):
        gpa = (self.marks/500) * 10
        return f"CGPA of {self.name} is {gpa}"
    @GPA.setter
    def GPA(self, value):
        self.marks = (value/10) * 500
    
d = Student("Muhammad", 450)
print(d.GPA)
d.GPA = 9.0
print(d.GPA)