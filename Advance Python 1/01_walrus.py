
from typing import List, tuple
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5] 

#tuple of integers and strings
data: tuple[int, str] = (1, "Muhammad")


# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
# Output: List is too long (5 elements, expected <= 3)

def sum(a: int, b: int) -> int:
    return a+b
sum(1, 2)
#so in this case we are giving hint to the compiler that this function will return an int