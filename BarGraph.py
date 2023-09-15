import matplotlib.pyplot as plt
import numpy as num;
a=[11,21,31,40,57]
b=[6,7,8,9,10]
c=[11,19,13,14,105]
plt.title("Mera Graph")
plt.xlabel("X")
plt.ylabel("Y")
bar_width = 0.35
plt.plot(b,a)
plt.plot(b,c)
plt.bar(b,c,color='red', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width)
plt.bar(b,a,color='blue', alpha=0.5, edgecolor='black', linewidth=2, width=bar_width, bottom=b)

plt.legend(['a','b','c'])
plt.savefig("BarGraph.png")
plt.show()