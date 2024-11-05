
#include <stdio.h>
#include <stdlib.h>

// Function to generate points on the parabola y = a * x^2 + b * x + c
void generate_parabola_points(double a, double b, double c, double x_start, double x_end, double step, double* x_points, double* y_points) {
    int index = 0;
    for (double x = x_start; x <= x_end; x += step) {
        x_points[index] = x;
        y_points[index] = a * x * x + b * x + c;
        index++;
    }
}

