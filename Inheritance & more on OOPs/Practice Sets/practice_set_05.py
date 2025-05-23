class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, value):
        return Vector(self.x + value.x, self.y + value.y, self.z + value.z)
    def __mul__(self, value):
        return self.x * value.x + self.y * value.y + self.z * value.z
    def __str__(self):
        return f" Vector {self.x}, {self.y}, {self.z}"
    
v1 =Vector(1, 2, 3)
v2 =Vector(4, 5, 6)
v3 =Vector(7, 8, 9)
print(v1 + v2)
print(v1 * v2)
print(v1 + v2 + v3) 