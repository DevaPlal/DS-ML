import numpy as np
import matplotlib.pyplot as plt


mean = float(input("Enter the mean: "))
std_dev = float(input("Enter the standard deviation: "))

num_samples = int(input("Enter sample size: "))
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=30, density=True, alpha=0.5, color='blue', edgecolor='black')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)
plt.plot(x, pdf, 'k-', linewidth=2)

plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution (Mean={}, Std Dev={})'.format(mean, std_dev))

plt.show()
