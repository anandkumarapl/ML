import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Apples', 'Oranges', 'Bananas', 'Grapes']
values1 = [20, 15, 10, 25]
values2 = [15, 10, 15, 20]

# Create a bar plot with customizations
bar_width = 0.35
plt.bar(categories, values1, color='orange', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width)
plt.bar(categories, values2, color='blue', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width, bottom=values1)

# Display the plot
plt.show()