import matplotlib.pyplot as plt
import numpy as num;
a=[1,2,3,4,5]
b=[5,4,3,2,1]
plt.plot(a,b)
plt.title("Mera Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.bar(a,b)
plt.savefig("BarGraph.png")
plt.show()