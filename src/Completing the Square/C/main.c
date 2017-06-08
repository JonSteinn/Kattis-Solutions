#include <stdio.h>

typedef struct point v;
typedef struct point p;
struct point
{
    int x, y;
};

void getInput(p* pts)
{
    scanf("%d %d %d %d %d %d", &pts[0].x, &pts[0].y, &pts[1].x, &pts[1].y, &pts[2].x, &pts[2].y);
}

void out(p* pt)
{
    printf("%d %d\n", pt->x, pt->y);
}

void vec_from_to(p* p1, p* p2, v* vec)
{
    vec->x = p2->x - p1->x;
    vec->y = p2->y - p1->y;
}

int orthogonal(v* v1, v* v2)
{
    return v1->x * v2->x + v1->y * v2->y == 0;
}

void add_vec_to_point(p* pt, v* vec)
{
    pt->x += vec->x;
    pt->y += vec->y;
}

void find(p* pts, p* pt)
{
    v vec1, vec2;
    vec_from_to(pts, pts + 1, &vec1);
    vec_from_to(pts, pts + 2, &vec2);
    if (orthogonal(&vec1, &vec2))
    {
        pt->x = pts[1].x;
        pt->y = pts[1].y;
        add_vec_to_point(pt, &vec2);
    }
    else
    {
        vec_from_to(pts + 1, pts, &vec1);
        vec_from_to(pts + 1, pts + 2, &vec2);
        if (!orthogonal(&vec1, &vec2))
        {
            vec_from_to(pts + 2, pts, &vec1);
            vec_from_to(pts + 2, pts + 1, &vec2);
        }
        pt->x = pts[0].x;
        pt->y = pts[0].y;
        add_vec_to_point(pt, &vec2);
    }
}

int main()
{
    p pts[3];
    getInput(pts);
    p missing;
    find(pts, &missing);
    out(&missing);
    return 0;
}