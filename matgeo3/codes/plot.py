
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates for points A and B
A = (1.0, 2.0, 3.0)
B = (4.0, 5.0, 6.0)

# Unpack coordinates
x = [A[0], B[0]]
y = [A[1], B[1]]
z = [A[2], B[2]]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, marker='o')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line Plot')

plt.show()

