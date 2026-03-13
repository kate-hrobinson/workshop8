import numpy as np
import matplotlib.pyplot as pyplot
def F(x):
    return np.exp(x) * np.cos(5 * x)

def Fp(x):
    return F(x) - 5 * np.exp(x) * np.sin(5*x)

x_plot = np.linspace(-np.pi, np.pi, 1000)
fig, ax = plt.subplots(1)
ax.plot(x_plot, F(x_plot), "k-")
plt.show()