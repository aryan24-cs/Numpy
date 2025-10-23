'''
.ravel() -> return view
.flatten() -> return copy
'''

import numpy as np 

arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())  # return view of original array
print(arr.flatten())  # return copy of original array

