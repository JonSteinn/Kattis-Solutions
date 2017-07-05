#include <stdio.h>

typedef struct point pnt;
typedef struct triangle tri;

struct point
{
    int x, y;
};

struct triangle
{
    pnt a, b, c;
};

int double_area(tri* t)
{
    return t->a.x * t->b.y + t->b.x * t->c.y + t->c.x * t->a.y - t->b.x * t->a.y - t->c.x * t->b.y - t->a.x * t->c.y;
}

int left_of(pnt* p0, pnt* p1, pnt* p2)
{
    return (p1->x - p0->x) * (p2->y - p0->y) - (p2->x - p0->x) * (p1->y - p0->y) > 0;
}

int inside(tri* t, pnt* p)
{
    // Order of triangle vertices (a,b,c) is guaranteed to be clockwise so we can just check
    // if the point is not on the left side of the line segments ab, bc, ca.
    return !left_of(&t->a, &t->b, p) && !left_of(&t->b, &t->c, p) && !left_of(&t->c, &t->a, p);
}

int main()
{
    tri t;
    scanf("%d %d %d %d %d %d", &t.a.x, &t.a.y, &t.b.x, &t.b.y, &t.c.x, &t.c.y);

    // If a > 0 then [a,b,c] is sorted ccw and we swap b and c to make it cw.
    int a = double_area(&t);
    if (a < 0)
    {
        a = -a;
    }
    else
    {
        if (t.b.x - t.c.x) t.b.x ^= t.c.x ^= t.b.x ^= t.c.x;
        if (t.b.y - t.c.y) t.b.y ^= t.c.y ^= t.b.y ^= t.c.y;
    }
    printf(a&1 ? "%d.5\n" : "%d.0\n", a >> 1);

    int n, c = 0;
    scanf("%d",&n);
    while (n--)
    {
        pnt p;
        scanf("%d %d", &p.x, &p.y);
        if (inside(&t, &p)) c++;
    }
    printf("%d\n", c);

    return 0;
}