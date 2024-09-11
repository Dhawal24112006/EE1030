import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Load the shared object file
sphere = ctypes.CDLL('./sphere.so')

# Define the Point structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]

# Define the function prototypes
sphere.generate_sphere.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(Point)), ctypes.POINTER(ctypes.POINTER(ctypes.c_int)), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
sphere.free_sphere_data.argtypes = [ctypes.POINTER(Point), ctypes.POINTER(ctypes.c_int)]

# Function to compute distance between two points
def distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

# Given points and constant
A = Point(3, 4, 5)
B = Point(-1, 3, -7)
K = np.sqrt(161)

# Calculate the distance between points A and B
distance_AB = distance(A, B)

# Center of the sphere is the midpoint of A and B
center_x = (A.x + B.x) / 2
center_y = (A.y + B.y) / 2
center_z = (A.z + B.z) / 2

# Calculate the radius of the sphere
radius = K - distance_AB / 2

# Parameters for the sphere
num_latitude = 30  # Increased to improve sphere coverage
num_longitude = 30  # Increased to improve sphere coverage

# Allocate pointers
vertices_ptr = ctypes.POINTER(Point)()
indices_ptr = ctypes.POINTER(ctypes.c_int)()
num_vertices = ctypes.c_int()
num_indices = ctypes.c_int()

# Generate the sphere
sphere.generate_sphere(num_latitude, num_longitude, ctypes.byref(vertices_ptr), ctypes.byref(indices_ptr), ctypes.byref(num_vertices), ctypes.byref(num_indices))

# Convert to numpy arrays
vertices = np.array([(vertices_ptr[i].x, vertices_ptr[i].y, vertices_ptr[i].z) for i in range(num_vertices.value)])
indices = np.array([indices_ptr[i] for i in range(num_indices.value)])

# Free the allocated memory
sphere.free_sphere_data(vertices_ptr, indices_ptr)

# Translate and scale vertices
vertices = vertices * radius
vertices[:, 0] += center_x
vertices[:, 1] += center_y
vertices[:, 2] += center_z

# Create a list of triangles directly from the vertex data
triangles = []
num_longitude_plus_one = num_longitude + 1

for i in range(num_latitude):
    for j in range(num_longitude):
        # Directly obtain vertices for the current "quad"
        v0 = vertices[i * num_longitude_plus_one + j]
        v1 = vertices[i * num_longitude_plus_one + (j + 1)]
        v2 = vertices[(i + 1) * num_longitude_plus_one + j]
        v3 = vertices[(i + 1) * num_longitude_plus_one + (j + 1)]

        # Add two triangles for the quad
        triangles.append([v0, v2, v1])
        triangles.append([v1, v2, v3])

# Plotting
fig = plt.figure(figsize=(10, 8))  # Adjust figure size for better visualization
ax = fig.add_subplot(111, projection='3d')
ax.add_collection3d(Poly3DCollection(triangles, facecolors='lightblue', linewidths=0.5, edgecolors='k', alpha=.25))

# Plot points A and B
ax.scatter(A.x, A.y, A.z, color='red', label='A (3, 4, 5)')
ax.scatter(B.x, B.y, B.z, color='green', label='B (-1, 3, -7)')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Locus of P')

# Set axis limits to be exactly -7 to 12
ax.set_xlim(-7, 12)
ax.set_ylim(-7, 12)
ax.set_zlim(-7, 12)

# Set equal aspect ratio
ax.set_box_aspect([1,1,1])  # Aspect ratio is 1:1:1

ax.legend()

plt.show()

