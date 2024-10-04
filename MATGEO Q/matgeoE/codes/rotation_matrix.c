#include <math.h>
#include <stdlib.h>

// Function to generate a rotation matrix for a given angle
void generate_rotation_matrix(float angle, float matrix[3][3]) {
    float radians = angle * M_PI / 180.0; // Convert degrees to radians
    float cos_angle = cos(radians);
    float sin_angle = sin(radians);

    matrix[0][0] = cos_angle;
    matrix[0][1] = -sin_angle;
    matrix[0][2] = 0;

    matrix[1][0] = sin_angle;
    matrix[1][1] = cos_angle;
    matrix[1][2] = 0;

    matrix[2][0] = 0;
    matrix[2][1] = 0;
    matrix[2][2] = 1;
}

