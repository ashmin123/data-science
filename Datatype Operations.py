# Python Program to create a data type object
import numpy as np

# np.int16 is converted into a data type object.
print(np.dtype(np.int16))

# Python Program to create a data type object containing a 32 bit big-endian integer
# i4 represents integer of size 4 byte
# > represents big-endian byte ordering and
# < represents little-endian encoding.
# dt is a dtype object
dt = np.dtype('>i4')

print("Byte order is:", dt.byteorder)

print("Size is:", dt.itemsize)

print("Data type is:", dt.name)