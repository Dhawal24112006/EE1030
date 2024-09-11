import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL('./libline.so')

# Define the argument and return types for the functions
lib.set_line_parameters.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                     ctypes.c_double, ctypes.c_double, ctypes.c_double]

lib.get_line_parameters.argtypes = [ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double),
                                    ctypes.POINTER(ctypes.c_double)]

# Define the points P and Q
p_x, p_y, p_z = 1.0, 2.0, 3.0
q_x, q_y, q_z = 4.0, 5.0, 6.0

# Set the line parameters in the C library
lib.set_line_parameters(p_x, p_y, p_z, q_x, q_y, q_z)

# Prepare variables to receive data
px, py, pz = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()
qx, qy, qz = ctypes.c_double(), ctypes.c_double(), ctypes.c_double()

# Get the line parameters from the C library
lib.get_line_parameters(ctypes.byref(px), ctypes.byref(py), ctypes.byref(pz),
                        ctypes.byref(qx), ctypes.byref(qy), ctypes.byref(qz))

# Convert the results to numpy arrays
P = np.array([px.value, py.value, pz.value])
Q = np.array([qx.value, qy.value, qz.value])

# Create a parameter t to interpolate points along the line
t = np.linspace(0, 1, 100)
line_points = P[:, np.newaxis] * (1 - t) + Q[:, np.newaxis] * t

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(line_points[0], line_points[1], line_points[2], label='Line PQ')

# Mark the points P and Q
ax.scatter(P[0], P[1], P[2], color='red', label='Point P (1,2,3)')
ax.scatter(Q[0], Q[1], Q[2], color='blue', label='Point Q (4,5,6)')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line Plot')
ax.legend()

plt.show()

