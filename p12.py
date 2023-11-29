import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
labels = ['A', 'B', 'C', 'D', 'E'] 
colors = ['red', 'green', 'blue', 'purple', 'orange'] 
markers = ['o', 's', '^', 'v', 'x']  
for i in range(len(x)):
    plt.scatter(x[i], y[i], c=colors[i], marker=markers[i], label=labels[i])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Labeled Data Points')

plt.legend()

plt.show()
