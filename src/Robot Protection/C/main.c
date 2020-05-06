#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x,y;
} Point2d;

Point2d first;

int orientation(Point2d *p0, Point2d *p1, Point2d *p2) {
    int x = (p1->y - p0->y) * (p2->x - p1->x) - (p1->x - p0->x) * (p2->y - p1->y);
    return (x > 0) - (x < 0);
}

int dist_sq(Point2d *p0, Point2d *p1) {
    int dx = p0->x - p1->x;
    int dy = p0->y - p1->y;
    return dx*dx + dy*dy;
}

int angle_comparator(const void *a, const void *b) {
    Point2d *_a = (Point2d*)a;
    Point2d *_b = (Point2d*)b;
    int o = orientation(&first, _a, _b);
    return o ? o : dist_sq(&first, _a) - dist_sq(&first, _b);
}

double triangle_area(Point2d *a, Point2d *b, Point2d *c) {
    return abs(
        a->x*b->y +
        b->x*c->y +
        c->x*a->y -
        a->y*b->x -
        b->y*c->x -
        c->y*a->x
    )/2.0;
}

int read_points(Point2d *points, int n) {
    int sw = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &points[i].x, &points[i].y);
        if (i > 0 && points[i].x == points[sw].x && points[i].y == points[sw].y) {
            i--;
            n--;
            continue;
        }
        if (points[i].y < points[sw].y || (points[i].y == points[sw].y && points[i].x < points[sw].x)) sw = i;
    }
    if (sw != 0) {
        points[sw].x ^= points[0].x ^= points[sw].x ^= points[0].x;
        points[sw].y ^= points[0].y ^= points[sw].y ^= points[0].y;
    }
    first = points[0];
    return n;
}

int trim_points(Point2d *points, int n) {
    int size = 1;
    for (int i = 1; i < n; i++) {
        while (i < n-1 && !orientation(&points[0],&points[i],&points[i+1])) i++;
        points[size].x = points[i].x;
        points[size].y = points[i].y;
        size++;
    }
    return size;
}

void graham_scan(Point2d *points, int n) {
    Point2d hull[n];
    int hull_s = 3;
    for (int i = 0; i < 3; i++) hull[i] = points[i];

    for (int i = 3; i < n; i++) {
        while (orientation(&hull[hull_s-2], &hull[hull_s-1], &points[i]) >= 0) {
            hull_s--;
        }
        hull[hull_s++] = points[i];
    }

    double area = 0;
    for (int i = 0; i < hull_s-1; i++) {
        area += triangle_area(&hull[0],&hull[i], &hull[i+1]);
    }

    printf("%.1lf\n", area);
}

int main() {
    while(1) {
        int n;
        scanf("%d",&n);
        if (!n) break;

        Point2d points[n];
        n = read_points(points, n);
        qsort(points + 1, n-1, sizeof(Point2d), angle_comparator);
        n = trim_points(points, n);

        if (n < 3) {
            printf("0.0\n");
        } else {
            graham_scan(points, n);
        }
    }

    return 0;
}