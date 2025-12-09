#np.nan_to_num(array, nan=value) default value is 0

import numpy as np

arr = np.array([1,2,np.nan,4,5,np.nan])

cleaned_arr = np.nan_to_num(arr, 100)
print(cleaned_arr)