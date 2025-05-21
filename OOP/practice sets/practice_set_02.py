import math
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"square of {self.n} is {math.pow(self.n, 2)}")
    def cube(self):
        print(f"cube of {self.n} is {math.pow(self.n, 3)}")
    def square_root(self):
        print(f"Square root of {self.n} is {math.sqrt(self.n)}")
    
calc = Calculator(2)
calc.cube()