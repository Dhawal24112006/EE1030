// triangle_median.c

#include <stdio.h>

// Function prototypes
void find_coordinates(double A_x, double A_y, double B_x, double B_y, double C_x, double C_y, double *Q_x, double *Q_y, double *R_x, double *R_y);

void find_coordinates(double A_x, double A_y, double B_x, double B_y, double C_x, double C_y, double *Q_x, double *Q_y, double *R_x, double *R_y) {
    // Coordinates of A, B, C
    double E_x = (A_x + C_x) / 2.0;
    double E_y = (A_y + C_y) / 2.0;
    double F_x = (A_x + B_x) / 2.0;
    double F_y = (A_y + B_y) / 2.0;

    // Coordinates of Q (divides BE in ratio 2:1)
    *Q_x = (2 * E_x + B_x) / 3.0;
    *Q_y = (2 * E_y + B_y) / 3.0;

    // Coordinates of R (divides CF in ratio 2:1)
    *R_x = (2 * F_x + C_x) / 3.0;
    *R_y = (2 * F_y + C_y) / 3.0;
}

int main() {
    // Define points A, B, C
    double A_x = 4.0, A_y = 2.0;
    double B_x = 6.0, B_y = 5.0;
    double C_x = 1.0, C_y = 4.0;

    double Q_x, Q_y, R_x, R_y;

    // Find coordinates
    find_coordinates(A_x, A_y, B_x, B_y, C_x, C_y, &Q_x, &Q_y, &R_x, &R_y);

    // Print results
    printf("Coordinates of Q: (%.2f, %.2f)\n", Q_x, Q_y);
    printf("Coordinates of R: (%.2f, %.2f)\n", R_x, R_y);

    return 0;
}

