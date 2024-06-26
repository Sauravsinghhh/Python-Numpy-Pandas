import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print("Array using array():", array1)

array_zeros = np.zeros((2, 3))
print("\nArray of zeros:\n", array_zeros)

array_ones = np.ones((3, 2))
print("\nArray of ones:\n", array_ones)

array_empty = np.empty((2, 2))
print("\nEmpty array:\n", array_empty)

array_arange = np.arange(0, 10, 2)
print("\nArray using arange():", array_arange)

array_linspace = np.linspace(0, 1, 5)
print("\nArray using linspace():", array_linspace)
