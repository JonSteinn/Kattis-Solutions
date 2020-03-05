
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double max(double a, double b) { return a < b ? b : a; }
double dabs(double x) { return x < 0 ? -x : x; }
int main() {
    int x,y,x1,y1,x2,y2;
    scanf("%d %d %d %d %d %d", &x,&y,&x1,&y1,&x2,&y2);

    int width = x2-x1;
    int height = y2-y1;
    double cx = (x1+x2)/2.0;
    double cy = (y1+y2)/2.0;

    double dx = max(dabs(x - cx) - width / 2.0, 0);
    double dy = max(dabs(y - cy) - height / 2.0, 0);

    printf("%.6lf\n", sqrt(dx * dx + dy * dy));

    return 0;
}