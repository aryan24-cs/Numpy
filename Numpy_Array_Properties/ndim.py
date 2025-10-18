import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array dimension:", arr_1d.ndim)
# output: 1 which indicates that this is a one-dimensional array

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array dimension:", arr_2d.ndim)
# output: 2 which indicates that this is a two-dimensional array

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("3D Array dimension:", arr_3d.ndim)  
# output: 3 which indicates that this is a three-dimensional array