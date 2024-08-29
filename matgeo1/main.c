// main.c

#include <stdio.h>

// Function prototype declaration from the shared library
void find_coordinates(double A_x, double A_y, double B_x, double B_y, double C_x, double C_y, double *Q_x, double *Q_y, double *R_x, double *R_y);

int main() {
    // Define points A, B, C
    double A_x = 4.0, A_y = 2.0;
    double B_x = 6.0, B_y = 5.0;
    double C_x = 1.0, C_y = 4.0;

    double Q_x, Q_y, R_x, R_y;

    // Find coordinates using the shared library function
    find_coordinates(A_x, A_y, B_x, B_y, C_x, C_y, &Q_x, &Q_y, &R_x, &R_y);

    // Print results
    printf("Coordinates of Q: (%.2f, %.2f)\n", Q_x, Q_y);
    printf("Coordinates of R: (%.2f, %.2f)\n", R_x, R_y);

    return 0;
}

