
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib = ctypes.CDLL('./lib_unit_vector.so')

# Define the argument and return types for the C function
lib.unit_vector.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.unit_vector.restype = None

# Create the function to call the C unit_vector function
def compute_unit_vector(vector):
    result = (ctypes.c_double * 3)()
    lib.unit_vector((ctypes.c_double * 3)(*vector), result)
    return np.array(result)

# Define vectors a and b
a = np.array([2, -1, 1], dtype=np.float64)
b = np.array([0, 2, 1], dtype=np.float64)

# Compute the vector a + b
sum_vector = a + b

# Compute the unit vector of a + b
unit_vec = compute_unit_vector(sum_vector)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors a and b
ax.quiver(0, 0, 0, *a, color='b', label='Vector a (2,-1,1)')
ax.quiver(0, 0, 0, *b, color='g', label='Vector b (0,2,1)')

# Plot the unit vector of a + b
ax.quiver(0, 0, 0, *unit_vec, color='r', linestyle='--', label='Unit Vector of a + b')

# Set labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.legend()

plt.show()

