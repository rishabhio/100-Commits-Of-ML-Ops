import numpy as np

# Creating Arrays
arr = np.array([1, 2, 3])
zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((2, 3))
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 50)

# Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result_add = a + b
result_sub = a - b
result_mul = a * b
result_div = a / b

dot_product = np.dot(a, b)
transposed_arr = np.transpose(zeros_arr)
reshaped_arr = np.reshape(arr, (2, 3))

# Statistical Operations
arr = np.array([1, 2, 3, 4, 5])

mean_value = np.mean(arr)
median_value = np.median(arr)
std_dev = np.std(arr)
sum_value = np.sum(arr)

# Indexing and Slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

element = matrix[1, 2]
submatrix = matrix[:2, 1:3]
