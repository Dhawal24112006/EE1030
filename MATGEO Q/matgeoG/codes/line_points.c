#include <stdio.h>

void generate_line_points(double m, double c, double x_start, double x_end, double step, double *x_vals, double *y_vals, int *n) {
    int i = 0;
    for (double x = x_start; x <= x_end; x += step) {
        x_vals[i] = x;
        y_vals[i] = m * x + c;  // Equation: y = mx + c
        i++;
    }
    *n = i;  // Number of points generated
}

