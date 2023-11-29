import matplotlib.pyplot as plt


complex_number_str = input("Enter a complex number (e.g., 3+2i): ")
real_part, imaginary_part = complex_number_str.split('+')
real_part = float(real_part)
imaginary_part = float(imaginary_part[:-1]) 
z = complex(real_part, imaginary_part)

plt.figure(figsize=(6, 6))
plt.scatter(z.real, z.imag, color='red', label='Complex Number')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Plot of a Complex Number')
plt.legend()
plt.grid(True)
plt.show()
