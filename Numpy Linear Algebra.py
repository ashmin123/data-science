import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))

# Python program explaining eigh() function
from numpy import linalg as geek
# Creating an array using array function
a = np.array([[1, -2j], [2j, 5]])
print("Array is :", a)
# calculating an eigen value using eigh() function
c, d = geek.eigh(a)
print("Eigen value is :", c)
print("Eigen value is :", d)