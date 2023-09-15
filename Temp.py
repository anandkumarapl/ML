import matplotlib.pyplot as plt;
import numpy as num;
x=[4,5,7,2,3,4]
y=[5,6,7,8,9,0]
plt.title("hello")
plt.plot(x,y)
plt.scatter(x,y)
plt.grid()
plt.savefig("img2.png")
plt.show()