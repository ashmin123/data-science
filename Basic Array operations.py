# Python program to demonstrate
# basic operations on single array
import numpy as np

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
print("Array 1:\n",a)

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
print("\nArray 2:\n",b)

# Adding 1 to every element
print("\nAdding 1 to every element:\n", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:\n", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)