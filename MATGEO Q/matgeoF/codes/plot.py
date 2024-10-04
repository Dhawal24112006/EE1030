import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
lib = ctypes.CDLL('./plane_calculations.so')

# Define the Point structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Define the function signatures
lib.calculatePlaneEquation.argtypes = [Point, Point, Point, 
                                        ctypes.POINTER(ctypes.c_double), 
                                        ctypes.POINTER(ctypes.c_double), 
                                        ctypes.POINTER(ctypes.c_double), 
                                        ctypes.POINTER(ctypes.c_double)]

lib.distanceFromPlane.argtypes = [Point, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.distanceFromPlane.restype = ctypes.c_double

# Input coordinates for points B, C, D
B = Point(3, 2, 1)
C = Point(4, 5, 5)
D = Point(4, 2, -2)

# Create an instance of Point A
A = Point(0, 5, -1)  # You can set x later

# Calculate plane coefficients
A_coef = ctypes.c_double()
B_coef = ctypes.c_double()
C_coef = ctypes.c_double()
D_coef = ctypes.c_double()

lib.calculatePlaneEquation(B, C, D, 
                            ctypes.byref(A_coef), 
                            ctypes.byref(B_coef), 
                            ctypes.byref(C_coef), 
                            ctypes.byref(D_coef))

# Now you can find the correct x for A if needed
def find_x(A_y, A_z, A_coef, B_coef, C_coef, D_coef):
    return (-B_coef.value * A_y - C_coef.value * A_z - D_coef.value) / A_coef.value

# Given y and z for point A
A_y = 5
A_z = -1
A.x = find_x(A_y, A_z, A_coef, B_coef, C_coef, D_coef)

# Calculate distance from point A to the plane
distance = lib.distanceFromPlane(A, A_coef.value, B_coef.value, C_coef.value, D_coef.value)

# Print results
print(f"Point A coordinates: ({A.x}, {A.y}, {A.z})")
print(f"Distance from point A to the plane: {distance:.2f}")

# Plotting the points and the plane
# Create a grid to plot the plane
xx, yy = np.meshgrid(range(0, 10), range(0, 10))
zz = (-A_coef.value * xx - B_coef.value * yy - D_coef.value) / C_coef.value

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot the points
ax.scatter(A.x, A.y, A.z, color='red', label=f'Point A ({A.x:.2f}, {A.y}, {A.z})')
ax.scatter(B.x, B.y, B.z, color='blue', label='Point B (3, 2, 1)')
ax.scatter(C.x, C.y, C.z, color='green', label='Point C (4, 5, 5)')
ax.scatter(D.x, D.y, D.z, color='orange', label='Point D (4, 2, -2)')

# Labels and legend
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
ax.set_title('Plane and Points in 3D')

plt.show()

