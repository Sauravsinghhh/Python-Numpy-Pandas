import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
y2 = [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]

plt.plot(x, y1, linestyle='--', color='blue', label='Line Plot')
plt.scatter(x, y2, color='red', s=100, label='Scatter Plot')

plt.title("Line and Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.savefig('line_scatter_plot.png')

plt.show()
