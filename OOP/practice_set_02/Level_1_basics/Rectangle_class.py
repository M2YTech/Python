class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f"The area is {self.length*self.width} ")

    def perimeter(self):
        print(f"The perimeter is {2*(self.length+self.width)}")
    
Result = Rectangle(2,3)
Result.area()
Result.perimeter()