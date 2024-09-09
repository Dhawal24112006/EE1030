import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ctypes

# Load the shared object file
locus = ctypes.CDLL('./locus.so')

# Define the Point structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Define the function prototypes
locus.check_locus.argtypes = [Point, Point, Point, ctypes.c_double]
locus.check_locus.restype = ctypes.c_int

# Given points and constant
A = Point(3, 4, 5)
B = Point(-1, 3, -7)
K = np.sqrt(161)

# Calculate the distance between points A and B
def distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

distance_AB = distance(A, B)

# Center of the sphere is the midpoint of A and B
center_x = (A.x + B.x) / 2
center_y = (A.y + B.y) / 2
center_z = (A.z + B.z) / 2

# Calculate the radius of the sphere
radius = K - distance_AB / 2

# Generate a grid of points in spherical coordinates
phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x = radius * np.sin(theta) * np.cos(phi)
y = radius * np.sin(theta) * np.sin(phi)
z = radius * np.cos(theta)

# Adjust the coordinates to the center of the sphere
x += center_x
y += center_y
z += center_z

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='lightblue', alpha=0.6)

# Plot points A and B
ax.scatter(A.x, A.y, A.z, color='red', label='A (3, 4, 5)')
ax.scatter(B.x, B.y, B.z, color='green', label='B (-1, 3, -7)')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Locus of P satisfying PA^2 + PB^2 = K^2')
ax.legend()

plt.show()

