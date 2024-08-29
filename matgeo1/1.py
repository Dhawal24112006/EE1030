import matplotlib.pyplot as plt
import numpy as np

# Define points A, B, and C
A = np.array([4, 2])
B = np.array([6, 5])
C = np.array([1, 4])

# Calculate midpoints E and F
E = (A + C) / 2
F = (A + B) / 2

# Function to find a point on a line segment given a ratio
def point_on_segment(P1, P2, ratio):
    return P1 + ratio * (P2 - P1)

# Calculate points Q and R
# BQ:QE = 2:1 means Q divides BE in the ratio 2:1
Q = point_on_segment(B, E, 2 / 3)

# CR:RF = 2:1 means R divides CF in the ratio 2:1
R = point_on_segment(C, F, 2 / 3)

# Plotting
plt.figure(figsize=(8, 6))

# Plot triangle ABC
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-')  # AB
plt.plot([B[0], C[0]], [B[1], C[1]], 'bo-')  # BC
plt.plot([C[0], A[0]], [C[1], A[1]], 'bo-')  # CA

# Plot medians BE and CF
plt.plot([B[0], E[0]], [B[1], E[1]], 'g--', label='Median BE')
plt.plot([C[0], F[0]], [C[1], F[1]], 'g--', label='Median CF')

# Plot points A, B, C, E, F, Q, R
plt.plot(*A, 'ro', label='A (4, 2)')
plt.plot(*B, 'ro', label='B (6, 5)')
plt.plot(*C, 'ro', label='C (1, 4)')
plt.plot(*E, 'go', label=f'E ({E[0]:.2f}, {E[1]:.2f})')
plt.plot(*F, 'go', label=f'F ({F[0]:.2f}, {F[1]:.2f})')
plt.plot(*Q, 'mo', label=f'Q ({Q[0]:.2f}, {Q[1]:.2f})')
plt.plot(*R, 'mo', label=f'R ({R[0]:.2f}, {R[1]:.2f})')

# Annotate points
plt.text(A[0], A[1], ' A', fontsize=12, verticalalignment='bottom')
plt.text(B[0], B[1], ' B', fontsize=12, verticalalignment='bottom')
plt.text(C[0], C[1], ' C', fontsize=12, verticalalignment='bottom')
plt.text(E[0], E[1], ' E', fontsize=12, verticalalignment='bottom')
plt.text(F[0], F[1], ' F', fontsize=12, verticalalignment='bottom')
plt.text(Q[0], Q[1], ' Q', fontsize=12, verticalalignment='bottom')
plt.text(R[0], R[1], ' R', fontsize=12, verticalalignment='top')

# Set plot limits and labels
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle ABC with Medians BE and CF')

plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

