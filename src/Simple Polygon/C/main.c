#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x,y;
    int index;
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
    return o ? o :  dist_sq(&first, _a)-dist_sq(&first, _b);
}

void read_points(int n, Point2d *pnts) {
    int sw = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &pnts[i].x, &pnts[i].y);
        pnts[i].index = i;
        if (i && (pnts[i].y < pnts[sw].y || (pnts[i].y == pnts[sw].y && pnts[i].x < pnts[sw].x))) sw = i;
    }

    first = pnts[sw];

    if (sw) {
        pnts[sw] = pnts[0];
        pnts[0] = first;
    }
}

void test_case(int n) {
    Point2d points[n];
    read_points(n, points);

    qsort(points + 1, n-1, sizeof(Point2d), angle_comparator);

    // Handle returning on colinear points
    int j = n-1;
    while (j > 0 && 0 == orientation(&points[0], &points[j], &points[j-1])) j--;

    for (int i = 0; i < j; i++) {
        if (i) putchar(' ');
        printf("%d", points[i].index);
    }
    for (int i = n-1; i >= j; i--) printf(" %d", points[i].index);
    putchar('\n');
}

int main() {
    int c,n;
    scanf("%d",&c);
    while(c--) {
        scanf("%d", &n);
        test_case(n);
    }
    return 0;
}