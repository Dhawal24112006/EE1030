#include <stdio.h>

void calculate_QR(double *Qx, double *Qy, double *Rx, double *Ry) {
    // Coordinates of the vertices
    double Bx = 6, By = 5;
    double Ex = 5 / 2.0, Ey = 3;
    double Cx = 1, Cy = 4;
    double Fx = 5, Fy = 7 / 2.0;
    
    // Coordinates of Q (BQ : QE = 2:1)
    *Qx = (2 * Ex + 1 * Bx) / 3;
    *Qy = (2 * Ey + 1 * By) / 3;
    
    // Coordinates of R (CR : RF = 2:1)
    *Rx = (2 * Fx + 1 * Cx) / 3;
    *Ry = (2 * Fy + 1 * Cy) / 3;
}

int main() {
    double Qx, Qy, Rx, Ry;
    calculate_QR(&Qx, &Qy, &Rx, &Ry);
    printf("Coordinates of Q: (%.2f, %.2f)\n", Qx, Qy);
    printf("Coordinates of R: (%.2f, %.2f)\n", Rx, Ry);
    return 0;
}

