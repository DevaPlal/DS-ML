n = int(input("Enter a positive integer: "))


sum_of_cubes = 0


for i in range(2, n + 1, 2):
   
    sum_of_cubes += i ** 3


print("Sum of Cubes of Even Numbers:", sum_of_cubes)
