"""
reshape(rows , cols) specify new shape for an array without changing its data.
if dimensions do not match, it will throw an error.
reshaping doesnot crete copy , it return view of original array.
"""

import numpy as np 

arr = np.array([1,2,3,4,5,6])
print(arr)

reshape_arr = arr.reshape(2,3)
print(reshape_arr)

