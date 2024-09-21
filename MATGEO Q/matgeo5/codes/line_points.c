
#include <stdlib.h>
#include <math.h>

// Function to generate points on a line segment AB
void generate_points(float A[3], float B[3], float points[][3], int n) {
    for (int i = 0; i < n; ++i) {
        float t = (float)i / (n - 1);
        points[i][0] = A[0] + t * (B[0] - A[0]);
        points[i][1] = A[1] + t * (B[1] - A[1]);
        points[i][2] = A[2] + t * (B[2] - A[2]);
    }
}

// Function to find the unit vector from A to B
void find_unit_vector(float A[3], float B[3], float unit_vector[3]) {
    // Compute the direction vector AB
    float direction[3];
    direction[0] = B[0] - A[0];
    direction[1] = B[1] - A[1];
    direction[2] = B[2] - A[2];
    
    // Compute the magnitude of direction
    float magnitude = sqrt(direction[0] * direction[0] +
                            direction[1] * direction[1] +
                            direction[2] * direction[2]);
    
    // Normalize the direction vector to get the unit vector
    if (magnitude != 0) {  // Avoid division by zero
        unit_vector[0] = direction[0] / magnitude;
        unit_vector[1] = direction[1] / magnitude;
        unit_vector[2] = direction[2] / magnitude;
    } else {
        // Handle the case where A and B are the same point
        unit_vector[0] = 0.0f;
        unit_vector[1] = 0.0f;
        unit_vector[2] = 0.0f;
    }
}

