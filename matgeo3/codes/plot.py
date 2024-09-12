import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object
line_points = ctypes.CDLL('./line_points.so')

# Define the function signatures
line_points.generate_points.argtypes = (ctypes.c_float * 3, ctypes.c_float * 3, ctypes.POINTER(ctypes.c_float * 3), ctypes.c_int)
line_points.find_unit_vector.argtypes = (ctypes.c_float * 3, ctypes.c_float * 3, ctypes.POINTER(ctypes.c_float * 3))

def generate_and_plot_points(A, B, n):
    # Prepare the output array for points
    points = np.zeros((n, 3), dtype=np.float32)
    points_c = points.ctypes.data_as(ctypes.POINTER(ctypes.c_float * 3))

    # Call the C function to generate points
    line_points.generate_points(
        (ctypes.c_float * 3)(*A),
        (ctypes.c_float * 3)(*B),
        points_c,
        n
    )

    # Prepare the output array for the unit vector
    unit_vector = (ctypes.c_float * 3)()  # Create a ctypes array of 3 floats

    # Call the C function to find the unit vector
    line_points.find_unit_vector(
        (ctypes.c_float * 3)(*A),
        (ctypes.c_float * 3)(*B),
        unit_vector
    )

    # Convert the unit vector to a numpy array
    unit_vector_np = np.array(unit_vector)

    # Convert points to numpy array for plotting
    points = np.array(points)

    # Print the unit vector
    print(f"Unit vector from A to B: {unit_vector_np}")

    # Plot the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(points[:, 0], points[:, 1], points[:, 2], marker='o')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title('Points on Line Segment AB')
    plt.show()

# Define points A and B
A = (1.0, 2.0, 3.0)
B = (4.0, 5.0, 6.0)
n = 10  # Number of points to generate

# Generate and plot points
generate_and_plot_points(A, B, n)

