import numpy as np

arr = np.array([1.0, 2.2, 3.3, 4.5, 5.6])
print(arr.dtype)

#convert float to int
int_arr = arr.astype(int)
print(int_arr)

#check the dtype of the new array
print(int_arr.dtype)