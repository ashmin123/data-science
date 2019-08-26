import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 0, 1]])

a = np.array([[0, 1, 2], [3, 4, 5],
              [6, 7, 8], [9, 10, 11]])
print("\nArray: \n",a)
print(a[1:2, 1:3])
print(a[1:2, [1, 2]])