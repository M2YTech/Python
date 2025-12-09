"""
np.isnan(array)
"""

import numpy as np

arr = np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr))

#you can directly compare np.nan values with each other.