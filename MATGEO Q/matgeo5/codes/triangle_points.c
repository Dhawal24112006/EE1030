// triangle_points.c
#include <stdio.h>
#include <math.h>

void generate_triangle_vertices(double AB, double BC, double angle_B, double* vertices) {
    // Calculate angle in radians
    double angle_B_rad = angle_B * (M_PI / 180.0);
    
    // Coordinates of points A, B, C
    vertices[0] = 0.0; // A.x
    vertices[1] = 0.0; // A.y
    vertices[2] = AB;  // B.x
    vertices[3] = 0.0; // B.y
    vertices[4] = BC * cos(angle_B_rad); // C.x
    vertices[5] = BC * sin(angle_B_rad); // C.y
}

