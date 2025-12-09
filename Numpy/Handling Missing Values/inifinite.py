#np.ininf() 10^1000
#1/10 
#Any calculation which exceeds python number limit then we declare it infinity and we handle it through np.isinf() function
import numpy as np
arr = np.array([1,2,np.inf,4,5,-np.inf])

print(np.isinf(arr))
