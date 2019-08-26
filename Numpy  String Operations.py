# Python program explaining numpy.lower() function
import numpy as np
# converting to lowercase
print(np.char.lower(['GEEKS', 'FOR']))
# converting to lowercase
print(np.char.lower('GEEKS'))

# Python program explaining numpy.split() function
import numpy as np
# splitting a string
print(np.char.split('geeks for geeks'))
# splitting a string
print(np.char.split('geeks, for, geeks', sep=','))

# Python program explainingnumpy.join() function
import numpy as np
# splitting a string
print(np.char.join('-', 'geeks'))
# splitting a string
print(np.char.join(['-', ':'], ['geeks', 'for']))

# Python program explaining numpy.count() function
import numpy as np
a = np.array(['geeks', 'for', 'geeks'])
# counting a substring
print(np.char.count(a, 'geek'))
# counting a substring
print(np.char.count(a, 'fo'))