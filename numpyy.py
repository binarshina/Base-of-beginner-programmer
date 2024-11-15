import numpy as np

# Create a simple NumPy array
array = np.array([1, 2, 3, 4, 5])

# Print the original array
print("Original array:", array)

# Perform basic mathematical operations
array_plus_10 = array + 10
print("Array + 10:", array_plus_10)

array_squared = array**2
print("Array squared:", array_squared)

# Calculate summary statistics
mean_value = np.mean(array)
print("Mean:", mean_value)

sum_value = np.sum(array)
print("Sum:", sum_value)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (Matrix):\n", matrix)

# Transpose the matrix
matrix_transpose = np.transpose(matrix)
print("Transposed Matrix:\n", matrix_transpose)

# Calculate the dot product of two arrays
array2 = np.array([2, 3, 4, 5, 6])
dot_product = np.dot(array, array2)
print("Dot product of array and array2:", dot_product)
