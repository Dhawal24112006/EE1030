#include <stdio.h>

static double px, py, pz;
static double qx, qy, qz;

void set_line_parameters(double p_x, double p_y, double p_z, double q_x, double q_y, double q_z) {
    px = p_x;
    py = p_y;
    pz = p_z;
    qx = q_x;
    qy = q_y;
    qz = q_z;
}

void get_line_parameters(double *p_x, double *p_y, double *p_z, double *q_x, double *q_y, double *q_z) {
    *p_x = px;
    *p_y = py;
    *p_z = pz;
    *q_x = qx;
    *q_y = qy;
    *q_z = qz;
}

