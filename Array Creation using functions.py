# Python code to demonstrate the working of array()
# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])   #array(data type, value list)
print(arr)

# printing original array
print("The new created array is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\n")

# Python Programming illustrating numpy.empty method
#numpy.empty(shape, dtype = float, order = ‘C’)
#function is used to create an array with data type and value list specified in its arguments.

import numpy as np
b = np.empty(2, dtype=int)
print("Matrix b : \n", b)
a = np.empty([2, 2], dtype=int)
print("\nMatrix a : \n", a)
c = np.empty([3, 3])
print("\nMatrix c : \n", c)


# Python Program illustrating numpy.zeros method
#numpy.zeros(shape, dtype = None, order = ‘C’)
#Return a new array of given shape and type, with zeros.

import numpy as np
b = np.zeros(2, dtype = int)
print("Matrix b : \n", b)
a = np.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)
c = np.zeros([3, 3])
print("\nMatrix c : \n", c)

