#include <stdio.h>
#include <math.h>

// Define a structure to hold 3D vectors
typedef struct {
    double x;
    double y;
    double z;
} Vector3;

// Function to compute the unit vector of (a + b)
void compute_unit_vector(const Vector3* a, const Vector3* b, Vector3* unit_vector) {
    Vector3 sum;
    sum.x = a->x + b->x;
    sum.y = a->y + b->y;
    sum.z = a->z + b->z;

    // Compute the magnitude of the vector sum
    double magnitude = sqrt(sum.x * sum.x + sum.y * sum.y + sum.z * sum.z);

    // Normalize the vector to get the unit vector
    unit_vector->x = sum.x / magnitude;
    unit_vector->y = sum.y / magnitude;
    unit_vector->z = sum.z / magnitude;
}

