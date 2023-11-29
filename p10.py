import numpy as np

rolls = np.random.randint(1, 7, size=1000)


counts = np.bincount(rolls)


for i, count in enumerate(counts[1:], start=1):
    print(f"Number {i}: {count} occurrences")
