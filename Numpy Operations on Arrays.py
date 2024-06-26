import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

addition = array1 + array2
print("Addition:", addition)

subtraction = array1 - array2
print("Subtraction:", subtraction)

multiplication = array1 * array2
print("Multiplication:", multiplication)

division = array1 / array2
print("Division:", division)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([1, 2, 3])

broadcast_add = array_2d + array_1d
print("\nBroadcasting addition:\n", broadcast_add)

broadcast_multiply = array_2d * array_1d
print("\nBroadcasting multiplication:\n", broadcast_multiply)
