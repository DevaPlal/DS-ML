class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
      
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
       
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
       
        return ComplexNumber(
            (self.real * other.real) - (self.imag * other.imag),
            (self.real * other.imag) + (self.imag * other.real)
        )

    def __str__(self):
        
        if self.imag < 0:
            return f"{self.real} - {abs(self.imag)}i"
        else:
            return f"{self.real} + {self.imag}i"


real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))

complex_num1 = ComplexNumber(real1, imag1)
complex_num2 = ComplexNumber(real2, imag2)

addition_result = complex_num1 + complex_num2
subtraction_result = complex_num1 - complex_num2
multiplication_result = complex_num1 * complex_num2

print("First Complex Number:", complex_num1)
print("Second Complex Number:", complex_num2)
print("Addition Result:", addition_result)
print("Subtraction Result:", subtraction_result)
print("Multiplication Result:", multiplication_result)
