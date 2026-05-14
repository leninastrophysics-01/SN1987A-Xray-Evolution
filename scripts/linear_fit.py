import numpy as np
import matplotlib.pyplot as plt

x = np.array([24,25,26,27,28,29,30])
y = np.array([0.07,0.08,0.09,0.10,0.11,0.12,0.13])

m, b = np.polyfit(x, y, 1)

plt.scatter(x, y)
plt.plot(x, m*x + b)

plt.xlabel("Age")
plt.ylabel("Hardness Ratio")
plt.title("Linear Fit")

plt.savefig("linear_fit.png")
plt.show()

print("Slope:", m)
print("Intercept:", b)
