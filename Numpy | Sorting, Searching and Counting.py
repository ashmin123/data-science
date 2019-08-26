import numpy as np

# sort along the first axis
a = np.array([[12, 15], [10, 1]])
print(a)
arr1 = np.sort(a, axis=0)
print("Along first axis : \n", arr1)

# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis=-1)
print("\nAlong first axis : \n", arr2)

a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis=None)
print("\nAlong none axis : \n", arr1)

# Python code to demonstrate working of  numpy.argsort
import numpy as np
# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])
# unsorted array print
print('Original array:\n', a)
# Sort array indices
b = np.argsort(a)
print('Sorted indices of original array->', b)
# To get sorted array using sorted indices c is temp array created of same len as of b
c = np.zeros(len(b), dtype=int)
for i in range(0, len(b)):
    c[i] = a[b[i]]
print('Sorted array->', c)