"""
np.insert(arrray, index, value, axis= None)
array = Original array
index -
value -
axis - (optional)
axis = 0, row-wise
1 column wise
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_array = np.insert(arr,2, 100)
print(new_array)
print(arr)
