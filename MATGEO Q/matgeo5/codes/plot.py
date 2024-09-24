import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared libraries
rotation_lib = ctypes.CDLL('./rotation_matrix.so')
multiplication_lib = ctypes.CDLL('./matrix_multiply.so')
line_points_lib = ctypes.CDLL('./line_points.so')

# Set the argument and return types for the functions
rotation_lib.generate_rotation_matrix.argtypes = [ctypes.c_float, np.ctypeslib.ndpointer(dtype=np.float32, shape=(3, 3))]
multiplication_lib.matrix_multiply.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32, shape=(3, 3)), 
                                                np.ctypeslib.ndpointer(dtype=np.float32, shape=(3,)), 
                                                np.ctypeslib.ndpointer(dtype=np.float32, shape=(3,))]
line_points_lib.generate_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32, shape=(3,)),
                                             np.ctypeslib.ndpointer(dtype=np.float32, shape=(3,)),
                                             ctypes.POINTER(ctypes.c_float),  # Use pointer to float for points
                                             ctypes.c_int]

# Define points A, B, and calculate C
A = np.array([6.0, 0.0, 0.0], dtype=np.float32)
B = np.array([0.0, 0.0, 0.0], dtype=np.float32)
BC_length = 8.0
angle_B = 60.0  # in degrees

# Generate rotation matrix
rotation_matrix = np.zeros((3, 3), dtype=np.float32)
rotation_lib.generate_rotation_matrix(angle_B, rotation_matrix)

# Vector BC
BC_vector = np.array([BC_length, 0.0, 0.0], dtype=np.float32)

# Multiply rotation matrix by BC vector to get point C
C = np.zeros(3, dtype=np.float32)
multiplication_lib.matrix_multiply(rotation_matrix, BC_vector, C)

# Convert C to a numpy array
C = np.array([C[0], C[1], 0.0], dtype=np.float32)

# Generate points on line segments AB, BC, and CA
n_points = 10
# Allocate space for points on all segments: 3*n_points
points = np.zeros((3 * n_points, 3), dtype=np.float32)

# Call the function to generate points for AB
line_points_lib.generate_points(A, B, points.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n_points)

# Call the function to generate points for BC
line_points_lib.generate_points(B, C, points[n_points:].ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n_points)

# Call the function to generate points for CA
line_points_lib.generate_points(C, A, points[2*n_points:].ctypes.data_as(ctypes.POINTER(ctypes.c_float)), n_points)

# Plotting the triangle ABC and line segments
plt.figure()
plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'b-')  # Triangle edges
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')  # Points A, B, C

# Add labels for points A, B, C with coordinates
plt.text(A[0], A[1], f'A ({A[0]:.1f}, {A[1]:.1f})', fontsize=12, ha='left', color='black')
plt.text(B[0], B[1], f'B ({B[0]:.1f}, {B[1]:.1f})', fontsize=12, ha='right', color='black')
plt.text(C[0], C[1], f'C ({C[0]:.1f}, {C[1]:.1f})', fontsize=12, ha='right', color='black')

# Plot the generated points on line segments
plt.scatter(points[:, 0], points[:, 1], color='green', label='Points on AB, BC, CA')
plt.legend()
plt.xlim(-1, 9)
plt.ylim(-1, 9)
plt.grid()
plt.title('Triangle ABC with Points on Line Segments AB, BC, and CA')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

