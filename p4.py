import numpy as np
array = np.array([[55, 25, 15],
                   [30, 44, 2],
                   [11, 45, 77]])
print(array)
array_sum = np.trace(array)
print("Sum of diagonal elements:", array_sum)
