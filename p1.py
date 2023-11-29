import numpy as np


user_input = input("Enter an array of numbers(comma-separated values): ")


input_values = user_input.split(',')


np_array = np.array([int(value.strip()) for value in input_values])
print("Array:", np_array)
print("Type:", type(np_array))
print("Mean:", np.mean(np_array))
print("Median:", np.median(np_array))
print("Standard Deviation:", np.std(np_array))

    
