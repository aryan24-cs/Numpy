python_list = [1, 2, 3, 4, 5]
print("Python List:", python_list)

import numpy as np
numpy_array = np.array([1,2,3,4,5])
print("NumPy Array:", numpy_array)  


# Creating arrays using list in NumPy
hello = np.array([1, 2, 3, 4, 5])
print(hello)


# create with default values
# np.zeros(shape)
zero_arry = np.zeros((3, 3))  # 3 rows and 4 columns
print(zero_arry)


# create with ones 
# np.ones(shape)
ones_array = np.ones((2, 4))  # 2 rows and 4
print(ones_array)


# create with any other number
# np.full(shape, fill_value)
full_array = np.full((2, 3), 7)  # 2 rows and 3 columns filled with 7
print(full_array)


# create sequence of numbers within a specified range
# np.arange(start, stop, step)
arr = np.arange(1, 10, 2)  # from 1 to 9 with step of 2
print(arr)