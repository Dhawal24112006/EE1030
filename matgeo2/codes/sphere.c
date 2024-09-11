#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Point;

void generate_sphere(int num_latitude, int num_longitude, Point **vertices, int **indices, int *num_vertices, int *num_indices) {
    int num_verts = (num_latitude + 1) * (num_longitude + 1);
    int num_faces = num_latitude * num_longitude * 2;

    *vertices = (Point *)malloc(num_verts * sizeof(Point));
    *indices = (int *)malloc(num_faces * 3 * sizeof(int));

    double pi = M_PI;
    double theta_step = pi / num_latitude;
    double phi_step = 2 * pi / num_longitude;

    // Generate vertices
    for (int i = 0; i <= num_latitude; ++i) {
        double theta = i * theta_step;
        for (int j = 0; j <= num_longitude; ++j) {
            double phi = j * phi_step;
            Point *p = &(*vertices)[i * (num_longitude + 1) + j];
            p->x = sin(theta) * cos(phi);
            p->y = sin(theta) * sin(phi);
            p->z = cos(theta);
        }
    }

    // Generate indices
    int index = 0;
    for (int i = 0; i < num_latitude; ++i) {
        for (int j = 0; j < num_longitude; ++j) {
            int first = i * (num_longitude + 1) + j;
            int second = first + num_longitude + 1;

            (*indices)[index++] = first;
            (*indices)[index++] = second;
            (*indices)[index++] = first + 1;

            (*indices)[index++] = second;
            (*indices)[index++] = second + 1;
            (*indices)[index++] = first + 1;
        }
    }

    *num_vertices = num_verts;
    *num_indices = num_faces * 3;
}

void free_sphere_data(Point *vertices, int *indices) {
    free(vertices);
    free(indices);
}
