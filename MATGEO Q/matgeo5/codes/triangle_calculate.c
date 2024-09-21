#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to calculate coordinates of point C
void calculate_point_C(float A[2], float B[2], float BC, float angle, float C[2]) {
    C[0] = B[0] + BC * cos(angle);
    C[1] = B[1] + BC * sin(angle);
}

