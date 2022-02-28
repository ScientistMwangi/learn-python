import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(type(arr))
print(arr)
print(arr.shape)

arr2 = np.zeros((3, 2), dtype=int)
arr_ones = np.ones((3, 2), dtype=int)
arr_five = np.full((3, 2), 5, dtype=int)
print(arr_five)
print(arr2)
print(arr_ones)
print(arr_five[1, 1])
