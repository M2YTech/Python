from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base*self.height)/2
    
ac = Circle(3)
print(ac.area())

at = Triangle(2,3)
print(at.area())