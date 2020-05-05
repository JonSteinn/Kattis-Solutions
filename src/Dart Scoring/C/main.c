#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_POINTS 100

typedef struct {
    float x,y;
} Point2d;

typedef struct {
    char *str;
    int size;
} InputLine;

Point2d first;

int orientation(Point2d *p0, Point2d *p1, Point2d *p2) {
    float x = (p1->y - p0->y) * (p2->x - p1->x) - (p1->x - p0->x) * (p2->y - p1->y);
    return (x > 0) - (x < 0);
}

float dist_sq(Point2d *p0, Point2d *p1) {
    float dx = p0->x - p1->x;
    float dy = p0->y - p1->y;
    return dx*dx + dy*dy;
}

double dist(Point2d *p, Point2d *q) {
    return sqrt(dist_sq(p, q));
}

int angle_comparator(const void *a, const void *b) { 
    Point2d *_a = (Point2d*)a;
    Point2d *_b = (Point2d*)b;
    int o = orientation(&first, _a, _b);
    return o ? o : (dist_sq(&first, _b) > dist_sq(&first, _a) ? -1 : 1);
}

int read_points(Point2d *points, InputLine *line, int *darts) {
    float x, y;
    int n = 0, sw = 0, str_i = 0, ws_found = 0;

    while (str_i < line->size) {
        sscanf(line->str + str_i, "%f %f", &x, &y);
        while (ws_found < 2 && str_i < line->size) {
            if (line->str[str_i++] == ' ') ws_found++;
        }
        ws_found = 0;

        if (n > 0 && points[sw].x == x && points[sw].y == y) {
            (*darts)++;
            continue;
        }

        if (y < points[sw].y || (y == points[sw].y && x < points[sw].x)) sw = n;
        points[n++] = (Point2d){x,y};
    }
    
    if (sw != 0) {
        float t = points[0].x;
        points[0].x = points[sw].x;
        points[sw].x = t;
        t = points[0].y;
        points[0].y = points[sw].y;
        points[sw].y = t;
    }

    first = points[0];

    *darts = *darts + n;

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

double graham_scan(Point2d *points, int n) {
    Point2d hull[n];
    int hull_s = 3;
    for (int i = 0; i < 3; i++) hull[i] = points[i];

    for (int i = 3; i < n; i++) {
        while (orientation(&hull[hull_s-2], &hull[hull_s-1], &points[i]) >= 0) {
            hull_s--;
        }
        hull[hull_s++] = points[i];
    }

    double s = dist(&hull[0],&hull[hull_s-1]);
    for (int i = 0; i < hull_s-1; i++) s += dist(&hull[i], &hull[i+1]);
    return s;
}

int read_line(InputLine *line) {
    size_t x;
    line->str = NULL;
    line->size = (int)getline(&line->str, &x, stdin);
    if (line->size == -1) return 0;
    line->str[--line->size] = '\0';
    return 1;
}

int main() {
    InputLine line;
    while(read_line(&line)) {
        int darts = 0;

        Point2d points[MAX_POINTS];
        int n = read_points(points, &line, &darts);
        qsort(points + 1, n-1, sizeof(Point2d), angle_comparator);
        n = trim_points(points, n);

        double s;
        if (n == 1) {
            s = 0.0;
        } else if (n == 2) {
            s = 2.0 * dist(&points[0],&points[1]);
        } else {
            s = graham_scan(points, n);
        }

        double score = (100.0 * darts) / (1.0 + s);
        printf("%.5lf\n", score);
    }

    return 0;
}