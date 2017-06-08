#include <stdio.h>

struct pos
{
    int x, y;
};

void window(int max_x, struct pos* dim)
{
    int y_max = 0;
    int x_max = 0;
    while(1)
    {
        int x, y;
        scanf("%d %d",&x,&y);
        if (x == -1 && y == -1)
        {
            dim->y += y_max;
            break;
        }
        if (dim->x + x > max_x)
        {
            dim->y += y_max;
            dim->x = x;
            y_max = y;
        }
        else
        {
            if (y > y_max) y_max = y;
            dim->x += x;
        }
        if (dim->x > x_max) x_max = dim->x;
    }
    dim->x = x_max;
}

int main()
{
    while(1)
    {
        int n;
        scanf("%d",&n);
        if (!n) break;
        struct pos p;
        p.x = 0;
        p.y = 0;
        window(n, &p);
        printf("%d x %d\n", p.x, p.y);
    }
    return 0;
}