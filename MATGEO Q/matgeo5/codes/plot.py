
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
triangle_lib = ctypes.CDLL('./triangle_points.so')

# Define the argument and return types
triangle_lib.generate_triangle_vertices.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]

# Parameters for the triangle
AB = 5.0  # Length of AB in cm
BC = 6.0  # Length of BC in cm
angle_B = 60.0  # Angle at B in degrees

# Create an array to hold the vertices
vertices = (ctypes.c_double * 6)()  # Array to hold x1, y1, x2, y2, x3, y3

# Call the function
triangle_lib.generate_triangle_vertices(AB, BC, angle_B, vertices)

# Extract the vertices
A = (vertices[0], vertices[1])
B = (vertices[2], vertices[3])
C = (vertices[4], vertices[5])

# Create lists of points for plotting
points_AB = np.array([A, B])
points_BC = np.array([B, C])
points_CA = np.array([C, A])

# Plotting
plt.figure()

# Plot each line in a different color
plt.plot(points_AB[:, 0], points_AB[:, 1], marker='o', color='blue', label='Line AB')
plt.plot(points_BC[:, 0], points_BC[:, 1], marker='o', color='green', label='Line BC')
plt.plot(points_CA[:, 0], points_CA[:, 1], marker='o', color='red', label='Line CA')

# Mark the points A, B, and C
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
plt.text(C[0], C[1], 'C', fontsize=12, ha='center')

plt.xlim(-1, max(vertices[2], vertices[4]) + 1)
plt.ylim(-1, max(vertices[5], 1) + 1)
plt.title('Triangle ABC')
plt.xlabel('X-axis (cm)')
plt.ylabel('Y-axis (cm)')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

