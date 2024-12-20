import matplotlib.pyplot as plt
import numpy as np

def pBasicCurve(degree, p0, p1, d0):
    u = np.linspace(0, 1, 100)
    c = np.zeros_like(u)
    factorial = 1
    for i in range(0, degree + 1):
        if i == 0:
            a = p0
        else:
            factorial *= i
            a = d0[i-1]/factorial
        c += a * u ** i
    return u, c

# Example usage
degree = 5
p0 = 10
p1 = 9
d0 = [10, 5, 0.3, 4, 5]

u, c = pBasicCurve(degree, p0, p1, d0)

plt.plot(u, c)
plt.title('Basic Curve')
plt.xlabel('u')
plt.ylabel('c')
plt.grid(True)
plt.show()
