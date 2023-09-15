import matplotlib.pyplot as plt
from scipy import stats

x = [1, 2, 3, 4, 5]
# y = [7, 9, 11, 13, 15]
# y=[-1,-2,-3,-4,-5]
y = [3, 7, 8, 10, 0]
slope, intercept, correlationcoefficient, p, slopeerror = stats.linregress(x, y)
print("Slope=", slope, ", Intercept=", intercept, ", Correlation =", correlationcoefficient, ",p=", p, "slope error=",
      slopeerror)
def linefunc(x):
    return slope * x + intercept
model = list(map(linefunc, x))
print(model)
predictedx = 10
predictedy = linefunc(predictedx)
print(predictedx, predictedy)
plt.scatter(x, y, color="red")
plt.plot(x, model, color="blue")
plt.title('Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()