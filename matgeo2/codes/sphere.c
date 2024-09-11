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
    Point *v = *vertices;
    for (int i = 0; i <= num_latitude; ++i) {
        double theta = i * theta_step;
        for (int j = 0; j <= num_longitude; ++j) {
            double phi = j * phi_step;
            v->x = sin(theta) * cos(phi);
            v->y = sin(theta) * sin(phi);
            v->z = cos(theta);
            ++v; // Move to next Point
        }
    }

    // Generate indices
    int *idx = *indices;
    Point *p0, *p1, *p2, *p3;
    Point *row_start, *next_row_start;

    for (int i = 0; i < num_latitude; ++i) {
        row_start = *vertices + i * (num_longitude + 1);
        next_row_start = row_start + (num_longitude + 1);

        for (int j = 0; j < num_longitude; ++j) {
            p0 = row_start + j;
            p1 = p0 + 1;
            p2 = next_row_start + j;
            p3 = p2 + 1;

            *idx++ = (int)(p0 - *vertices);
            *idx++ = (int)(p2 - *vertices);
            *idx++ = (int)(p1 - *vertices);

            *idx++ = (int)(p1 - *vertices);
            *idx++ = (int)(p2 - *vertices);
            *idx++ = (int)(p3 - *vertices);
        }
    }

    *num_vertices = num_verts;
    *num_indices = num_faces * 3;
}

void free_sphere_data(Point *vertices, int *indices) {
    free(vertices);
    free(indices);
}

