

import numpy as np
import matplotlib.pyplot as plt

def cubic_power_basis_curve_with_cusp(u):
    # Define the cubic power basis functions
    def basis_function_0(u): return (1 - u) ** 3
    def basis_function_1(u): return 3 * u * (1 - u) ** 2
    def basis_function_2(u): return 3 * u ** 2 * (1 - u)
    def basis_function_3(u): return u ** 3

    # Define the control points for the curve
    P0 = np.array([0, 0])
    P1 = np.array([1, 2])
    P2 = np.array([2, -2])
    P3 = np.array([3, 0])

    # Calculate the point on the curve at parameter u
    point = (basis_function_0(u) * P0 +
             basis_function_1(u) * P1 +
             basis_function_2(u) * P2 +
             basis_function_3(u) * P3)
    
    return point

# Generate points on the curve
u_values = np.linspace(0, 1, 10)
curve_points = np.array([cubic_power_basis_curve_with_cusp(u) for u in u_values])

# Plot the curve
plt.plot(curve_points[:, 0], curve_points[:, 1], label='Cubic Power Basis Curve with Cusp')
plt.scatter([0, 1, 2, 3], [0, 2, -2, 0], color='red', label='Control Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Power Basis Curve with Cusp')
plt.grid(True)
plt.show()
