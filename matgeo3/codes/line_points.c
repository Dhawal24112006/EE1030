

// line_points.c
#include <stdlib.h>

// Function to generate points on a line segment AB
void generate_points(float A[3], float B[3], float points[][3], int n) {
    for (int i = 0; i < n; ++i) {
        float t = (float)i / (n - 1);
        points[i][0] = A[0] + t * (B[0] - A[0]);
        points[i][1] = A[1] + t * (B[1] - A[1]);
        points[i][2] = A[2] + t * (B[2] - A[2]);
    }
}

