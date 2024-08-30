import ctypes

# Load the shared library
lib = ctypes.CDLL('./libgeometry.so')

# Define the return type of the function
lib.calculate_QR.restype = None

# Define the argument types of the function
lib.calculate_QR.argtypes = [ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]

# Create ctypes variables to hold the results
Qx = ctypes.c_double()
Qy = ctypes.c_double()
Rx = ctypes.c_double()
Ry = ctypes.c_double()

# Call the function
lib.calculate_QR(ctypes.byref(Qx), ctypes.byref(Qy), ctypes.byref(Rx), ctypes.byref(Ry))

# Print the results
print(f"Coordinates of Q: ({Qx.value:.2f}, {Qy.value:.2f})")
print(f"Coordinates of R: ({Rx.value:.2f}, {Ry.value:.2f})")

