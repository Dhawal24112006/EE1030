
// line_plot.c
#include <stdio.h>
#include <stdlib.h>

// Function to plot a 3D line using gnuplot
void plot_line(double x1, double y1, double z1, double x2, double y2, double z2) {
    FILE *gnuplot = popen("gnuplot -persistent", "w");
    if (gnuplot == NULL) {
        fprintf(stderr, "Error: could not open gnuplot.\n");
        exit(1);
    }

    fprintf(gnuplot, "set title '3D Line Plot'\n");
    fprintf(gnuplot, "set xlabel 'X'\n");
    fprintf(gnuplot, "set ylabel 'Y'\n");
    fprintf(gnuplot, "set zlabel 'Z'\n");
    fprintf(gnuplot, "splot '-' with linespoints title 'Line AB'\n");
    fprintf(gnuplot, "%f %f %f\n", x1, y1, z1);
    fprintf(gnuplot, "%f %f %f\n", x2, y2, z2);
    fprintf(gnuplot, "e\n");

    pclose(gnuplot);
}

