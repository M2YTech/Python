class vector2d:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"The value oof x is {self.x} and y is {self.y}.")
    
class vector3d(vector2d):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z
    def show(self):
        print(f"The value oof x is {self.x} , y is {self.y}. and  is {self.z}.")
    
a = vector2d()
print(a.show)
b = vector3d()
print(b.show)
    