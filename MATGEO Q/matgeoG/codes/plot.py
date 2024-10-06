import numpy as np
import matplotlib.pyplot as plt
import ctypes
from scipy.optimize import fsolve
from scipy.integrate import quad

# Load the shared libraries
line_lib = ctypes.CDLL('./line_points.so')
parabola_lib = ctypes.CDLL('./parabola_points.so')

# Define the function prototypes for the C functions
line_lib.generate_line_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
parabola_lib.generate_parabola_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Number of points
n_points = 1000

# Allocate memory for the points
x_points = np.linspace(-10, 10, n_points)
y_line_points = np.zeros(n_points, dtype=np.float64)
y_parabola_points = np.zeros(n_points, dtype=np.float64)

# Define the start and end of x values
x_start, x_end = -10.0, 10.0
step = (x_end - x_start) / n_points

# Call the C functions to generate the points
line_lib.generate_line_points(1.5, 6.0, x_start, x_end, step, x_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), y_line_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
parabola_lib.generate_parabola_points(0.75, 0, 0, x_start, x_end, step, x_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), y_parabola_points.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

# Define the equations for the line and the parabola
def line_eq(x):
    return 1.5 * x + 6  # Line equation: y = 1.5x + 6

def parabola_eq(x):
    return 0.75 * x ** 2  # Parabola equation: y = 0.75x^2

# Define the system of equations to find intersections
def equations(x):
    return parabola_eq(x) - line_eq(x)

# Find the intersection points using fsolve
x_intersect_1 = fsolve(equations, -5)[0]  # First intersection, close to -5
x_intersect_2 = fsolve(equations, 5)[0]   # Second intersection, close to 5

y_intersect_1 = line_eq(x_intersect_1)  # y-coordinate of first intersection
y_intersect_2 = line_eq(x_intersect_2)  # y-coordinate of second intersection

# Calculate the area between the curves
def integrand(x):
    return abs(parabola_eq(x) - line_eq(x))

area, _ = quad(integrand, x_intersect_1, x_intersect_2)

print(f"Area between the line and the parabola: {area:.4f}")

# Plot the figures
plt.figure(figsize=(10, 6))

# Plot line points
plt.plot(x_points, y_line_points, 'r', label='Line: y = 1.5x + 6')

# Plot parabola points
plt.plot(x_points, y_parabola_points, 'g', label='Parabola: y = 0.75x^2')

# Shade the area between the line and parabola between the intersection points
plt.fill_between(x_points, y_line_points, y_parabola_points, 
                 where=((x_points >= x_intersect_1) & (x_points <= x_intersect_2)),
                 color='gray', alpha=0.5, label='Area between')

# Highlight the intersection points
plt.scatter([x_intersect_1, x_intersect_2], [y_intersect_1, y_intersect_2], color='blue', s=100, zorder=5)

# Annotate the intersection points
plt.text(x_intersect_1, y_intersect_1, f'({x_intersect_1:.2f}, {y_intersect_1:.2f})', fontsize=12, ha='right')
plt.text(x_intersect_2, y_intersect_2, f'({x_intersect_2:.2f}, {y_intersect_2:.2f})', fontsize=12, ha='left')

# Add labels and grid
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Between Line and Parabola')
plt.grid(True)

# Show plot
plt.show()

