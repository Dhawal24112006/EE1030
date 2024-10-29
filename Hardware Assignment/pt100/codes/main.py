import numpy as np
import matplotlib.pyplot as plt

# Load training data
A = np.loadtxt('training_data.txt')
T_train = A[:, 0]
Y_train = A[:, 1]

# Prepare design matrix for least squares (quadratic model)
X_train = np.column_stack((np.ones(A.shape[0]), T_train, T_train**2))

# Perform least squares fitting
theta = np.linalg.lstsq(X_train, Y_train, rcond=None)[0].reshape(-1, 1)
print("The value of n is:")
print(theta)

# Plot training results
plt.figure()
plt.plot(T_train, X_train @ theta, label='Fitted Model')
plt.plot(T_train, Y_train, 'k.', label='Training Data')
plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel('Temperature ($^{\circ}$C)')
plt.legend()
plt.tight_layout()
plt.savefig('../figs/train.png')

# Close current figure
plt.close()

# Load validation data
B = np.loadtxt('validation_data.txt')
T_valid = B[:, 0]
Y_valid = B[:, 1]

# Prepare design matrix for validation
X_valid = np.column_stack((np.ones(B.shape[0]), T_valid, T_valid**2))

# Plot validation results
plt.figure()
plt.plot(T_valid, X_valid @ theta, label='Fitted Model')
plt.plot(T_valid, Y_valid, 'k.', label='Validation Data')
plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel('Temperature ($^{\circ}$C)')
plt.legend()
plt.tight_layout()
plt.savefig('../figs/valid.png')
