import numpy as np

array3 = np.array([10, 20, 30, 40])
array4 = np.array([2, 3, 4, 5])

ufunc_add = np.add(array3, array4)
print("\nnp.add():", ufunc_add)

ufunc_subtract = np.subtract(array3, array4)
print("np.subtract():", ufunc_subtract)

ufunc_multiply = np.multiply(array3, array4)
print("np.multiply():", ufunc_multiply)

ufunc_divide = np.divide(array3, array4)
print("np.divide():", ufunc_divide)

ufunc_sqrt = np.sqrt(array3)
print("\nnp.sqrt():", ufunc_sqrt)

ufunc_exp = np.exp(array3)
print("np.exp():", ufunc_exp)

ufunc_log = np.log(array4)
print("np.log():", ufunc_log)
