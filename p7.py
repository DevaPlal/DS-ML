import numpy as np

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))


array1 = []
array2 = []


print("Enter values for the first matrix:")
for i in range(row):
    row_values = []
    for j in range(column):
        num1 = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row_values.append(num1)
    array1.append(row_values)


print("Enter values for the second matrix:")
for i in range(row):
    row_values = []
    for j in range(column):
        num2 = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row_values.append(num2)
    array2.append(row_values)


array1 = np.array(array1)
array2 = np.array(array2)

print("Matrix 1:")
print(array1)

print("Matrix 2:")
print(array2)


add = np.add(array1, array2)
print("Matrix Addition:")
print(add)

product = np.multiply(array1, array2)
print("Element-wise Multiplication:")
print(product)

sub = np.subtract(array1, array2)
print("Matrix Subtraction:")
print(sub)

abs_diff = np.abs(sub)
print("Element-wise Absolute Difference:")
print(abs_diff)

div = np.divide(array1, array2, where=array2 != 0)
print("Element-wise Division (with division by zero protection):")
print(div)
