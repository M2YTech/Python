class Complex:
    def __init__(self, r ,i):
        self.r = r
        self.i = i
    def __add__(self, value):
        return Complex(self.r + value.r, self.i + value.i)
    def __mul__(self, value):
        real_part = (self.r * value.r) - (self.i * value.i)
        imaginary_part = (self.r * value.i) + (self.i * value.r)
        return Complex(real_part, imaginary_part)
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 * c2)
# The output of the code is:
# 4 + 6i
