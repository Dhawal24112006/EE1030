#include <stdlib.h>

// Function to multiply a 3x3 matrix with a 3x1 vector
void matrix_multiply(float A[3][3], float B[3], float result[3]) {
    for (int i = 0; i < 3; i++) {
        result[i] = 0;
        for (int j = 0; j < 3; j++) {
            result[i] += A[i][j] * B[j];
        }
    }
}

