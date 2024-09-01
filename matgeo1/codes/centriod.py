import ctypes
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./libsection_formula.so')

# Define the argument and return types for the C function
lib.find_section_point.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.find_section_point.restype = None

def find_section_point(x1, y1, x2, y2, m, n):
    x = ctypes.c_double()
    y = ctypes.c_double()
    lib.find_section_point(x1, y1, x2, y2, m, n, ctypes.byref(x), ctypes.byref(y))
    return (x.value, y.value)

# Given points
A = (4, 2)
B = (6, 5)
C = (1, 4)

# Midpoints of medians (E and F)
E = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
F = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)

# Find Q on BE such that BQ : QE = 2 : 1
Q = find_section_point(B[0], B[1], E[0], E[1], 2, 1)

# Find R on CF such that CR : RF = 2 : 1
R = find_section_point(C[0], C[1], F[0], F[1], 2, 1)

# Format the results to 2 decimal places
Q_formatted = (round(Q[0], 2), round(Q[1], 2))
R_formatted = (round(R[0], 2), round(R[1], 2))

# Print results with 2 decimal precision
print(f"Q: {Q_formatted}")
print(f"R: {R_formatted}")

# Plotting
plt.figure(figsize=(8, 8))

# Plot the triangle
plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-', label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], 'go-', label='BC')
plt.plot([C[0], A[0]], [C[1], A[1]], 'bo-', label='CA')

# Plot the medians
plt.plot([B[0], E[0]], [B[1], E[1]], 'r--', label='BE')
plt.plot([C[0], F[0]], [C[1], F[1]], 'g--', label='CF')

# Plot Q and R
plt.plot(*Q_formatted, 'ko', label='Q', markersize=8)
plt.plot(*R_formatted, 'ko', label='R', markersize=8)

# Annotate points
plt.text(*Q_formatted, f' Q {Q_formatted}', fontsize=12, ha='right', color='black')
plt.text(*R_formatted, f' R {R_formatted}', fontsize=12, ha='left', color='black')
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle ABC with Medians and Points Q and R')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

