import numpy as np

point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])

distance = np.linalg.norm(point1 - point2)

print("Euclidean Distance:", distance)
