import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(0, 4))

def f(x):
    return (x)
def g(x):
    return (x*x)
def h(x):
    return (x**x)

plt.title ("Weekly Task 08")
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")
plt.plot (f(x), label = "x", color = "red")
plt.plot (g(x), label = "x^2", color = "blue")
plt.plot (h(x), label = "x^3", color = "green")
plt.legend()
plt.show()