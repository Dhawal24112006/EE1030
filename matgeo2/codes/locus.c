#include <math.h>

// Structure to represent a point in 3D space
typedef struct {
    double x, y, z;
} Point;

// Function to compute the square of the distance between two points
double distance_squared(Point p1, Point p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) +
           (p1.y - p2.y) * (p1.y - p2.y) +
           (p1.z - p2.z) * (p1.z - p2.z);
}

// Function to check if the condition PA^2 + PB^2 = K^2 holds
int check_locus(Point A, Point B, Point P, double K) {
    double PA_squared = distance_squared(A, P);
    double PB_squared = distance_squared(B, P);
    return fabs(PA_squared + PB_squared - K * K) < 1e-6;
}

