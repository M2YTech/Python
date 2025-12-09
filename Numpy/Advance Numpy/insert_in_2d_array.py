import numpy as np

array_2d = np.array([[1,2],[3,4]])
print(array_2d)

new_arr_2d = np.insert(array_2d, 1, [5,6], 1)
print(new_arr_2d)
