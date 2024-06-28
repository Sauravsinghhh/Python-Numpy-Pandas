import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
data = [2, 3, 5, 6, 6, 7, 7, 7, 8, 9, 9, 10, 10, 10, 11, 11, 11, 12, 13, 13, 14, 15, 16, 16, 17]

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].bar(categories, values, color='green')
axs[0].set_title("Bar Plot")
axs[0].set_xlabel("Categories")
axs[0].set_ylabel("Values")
axs[0].grid(True)

axs[1].hist(data, bins=15, color='purple')
axs[1].set_title("Histogram")
axs[1].set_xlabel("Data")
axs[1].set_ylabel("Frequency")
axs[1].grid(True)

plt.tight_layout()

plt.show()
