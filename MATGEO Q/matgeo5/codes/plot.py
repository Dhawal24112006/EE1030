
import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared libraries
lib_calculate = ctypes.CDLL('./libtriangle_calculate.so')
lib_points = ctypes.CDLL('./libline_points.so')

# Define the C functions we want to call for calculating C
lib_calculate.calculate_point_C.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(2,)),
                                             np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(2,)),
                                             ctypes.c_float,
                                             ctypes.c_float,
                                             np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(2,))]

# Define the C functions we want to call for generating points
lib_points.generate_points.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(3,)),
                                        np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, shape=(3,)),
                                        np.ctypeslib.ndpointer(dtype=np.float32, ndim=2, shape=(10, 3)),
                                        ctypes.c_int]

# Points A and B
A = np.array([6.0, 0.0], dtype=np.float32)
B = np.array([0.0, 0.0], dtype=np.float32)
BC = 8.0
angle = np.pi / 3  # 60 degrees

# Calculate point C
C = np.zeros(2, dtype=np.float32)
lib_calculate.calculate_point_C(A, B, BC, angle, C)

# Generate points along AB and BC
n_points = 10
points_AB = np.zeros((n_points, 3), dtype=np.float32)
points_BC = np.zeros((n_points, 3), dtype=np.float32)

# Extend A and B to 3D (Z=0)
A_3D = np.array([A[0], A[1], 0.0], dtype=np.float32)
B_3D = np.array([B[0], B[1], 0.0], dtype=np.float32)
C_3D = np.array([C[0], C[1], 0.0], dtype=np.float32)

lib_points.generate_points(A_3D, B_3D, points_AB, n_points)
lib_points.generate_points(B_3D, C_3D, points_BC, n_points)

# Plotting the triangle
plt.figure()
plt.plot([B[0], A[0]], [B[1], A[1]], 'ro-')  # AB
plt.plot([B[0], C[0]], [B[1], C[1]], 'ro-')  # BC
plt.plot([A[0], C[0]], [A[1], C[1]], 'ro-')  # AC
plt.fill([B[0], A[0], C[0]], [B[1], A[1], C[1]], 'b', alpha=0.3)

# Annotate points A, B, and C
plt.text(A[0], A[1], f'A({A[0]}, {A[1]})', fontsize=12, ha='right', color='black')
plt.text(B[0], B[1], f'B({B[0]}, {B[1]})', fontsize=12, ha='right', color='black')
plt.text(C[0], C[1], f'C({C[0]:.2f}, {C[1]:.2f})', fontsize=12, ha='right', color='black')

# Set graph limits and labels
plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.title('Triangle ABC')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

