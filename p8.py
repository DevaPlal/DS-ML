import numpy as np


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


matrix = []


print(f"Enter {rows} rows of {columns} columns for the matrix:")
for i in range(rows):
    row_values = []
    for j in range(columns):
        num = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row_values.append(num)
    matrix.append(row_values)


matrix = np.array(matrix)

print("Matrix:")
print(matrix)


determinant = np.linalg.det(matrix)
print("Determinant:", determinant)


if(determinant!=0):
 inverse = np.linalg.inv(matrix)
 print("Inverse:")
 print(inverse)
else:
     print("The matrix is singular and does not have an inverse.")
