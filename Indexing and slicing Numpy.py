import numpy as np

# 1D array
array_1d = np.array([10, 20, 30, 40, 50])
print("Element at index 2 in 1D array:", array_1d[2])

# 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, column 2 in 2D array:", array_2d[1, 2])

# 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Element at depth 1, row 0, column 1 in 3D array:", array_3d[1, 0, 1])
