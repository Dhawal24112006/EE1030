
#include <math.h>

void unit_vector(const double vector[3], double result[3]) {
    double magnitude = sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]);
    if (magnitude == 0) {
        result[0] = result[1] = result[2] = 0;
    } else {
        result[0] = vector[0] / magnitude;
        result[1] = vector[1] / magnitude;
        result[2] = vector[2] / magnitude;
    }
}

