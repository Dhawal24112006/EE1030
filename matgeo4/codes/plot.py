
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL('./libvector_utils.so')

# Define the argument and return types for the C function
class Vector3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

lib.compute_unit_vector.argtypes = [ctypes.POINTER(Vector3), ctypes.POINTER(Vector3), ctypes.POINTER(Vector3)]

# Create instances of the vectors a and b
a = Vector3(2, -1, 1)
b = Vector3(0, 2, 1)
unit_vector = Vector3()

# Compute the unit vector of a + b
lib.compute_unit_vector(ctypes.byref(a), ctypes.byref(b), ctypes.byref(unit_vector))

# Convert to numpy arrays for plotting
a_np = np.array([a.x, a.y, a.z])
b_np = np.array([b.x, b.y, b.z])
sum_vector_np = a_np + b_np
unit_vec_np = np.array([unit_vector.x, unit_vector.y, unit_vector.z])

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors a, b, and the unit vector of a + b
ax.quiver(0, 0, 0, a_np[0], a_np[1], a_np[2], color='b', label='Vector a')
ax.quiver(0, 0, 0, b_np[0], b_np[1], b_np[2], color='g', label='Vector b')
ax.quiver(0, 0, 0, unit_vec_np[0], unit_vec_np[1], unit_vec_np[2], length=1, color='r', label='Unit Vector of a + b')

# Set labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.legend()

plt.show()

