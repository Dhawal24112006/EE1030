#include <stdio.h>
#include <math.h>

typedef struct {
    double x;
    double y;
    double z;
} Point;

// Function to calculate the normal vector of the plane formed by points B, C, D
void calculatePlaneEquation(Point B, Point C, Point D, double* A, double* B_coef, double* C_coef, double* D_coef) {
    // Vectors BC and BD
    double BC[3] = {C.x - B.x, C.y - B.y, C.z - B.z};
    double BD[3] = {D.x - B.x, D.y - B.y, D.z - B.z};

    // Normal vector (cross product of BC and BD)
    *A = BC[1] * BD[2] - BC[2] * BD[1];  // A
    *B_coef = BC[2] * BD[0] - BC[0] * BD[2];  // B
    *C_coef = BC[0] * BD[1] - BC[1] * BD[0];  // C

    // D coefficient (constant term)
    *D_coef = -(*A * B.x + *B_coef * B.y + *C_coef * B.z);
}

// Function to calculate the distance from point A to the plane
double distanceFromPlane(Point A, double A_coef, double B_coef, double C_coef, double D_coef) {
    return (A_coef * A.x + B_coef * A.y + C_coef * A.z + D_coef) /
           sqrt(A_coef * A_coef + B_coef * B_coef + C_coef * C_coef);
}

