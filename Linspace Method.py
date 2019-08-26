# Python Programming illustrating numpy.linspace method

import numpy as np

# restep set to True
print("B\n", np.linspace(2.0, 3.0, num=5, retstep=True), "\n")

# To evaluate sin() in long range
x = np.linspace(0, 2, 10)
print("A\n", np.sin(x))