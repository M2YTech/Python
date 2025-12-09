"""
reshape(row, column) specify new shape
if dimensions match

reshaping does not return a copy it returns a view changing values in the new shape will effect the array
"""

import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
