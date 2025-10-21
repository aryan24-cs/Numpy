'''
slicing:

array[start:stop:step]
start: starting index (inclusive)
stop: ending index (exclusive)
step: step size (default is 1)

arr[start:stop]          # Slices from start to stop-1
negative step , -1 for reverse
'''

import numpy as np  

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(arr[1:5])  # index 1 to 4
print(arr[:4])   # index 0 to 3
print(arr[::2])  # every second element
print(arr[::-1]) # reverse the array