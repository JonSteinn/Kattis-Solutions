#include <stdio.h>

struct circle
{
    int x;
    int y;
    int r;
};

struct rectangle
{
    int x1;
    int y1;
    int x2;
    int y2;
};


int main()
{
    int n;
    scanf("%d", &n);

    struct rectangle rectangles[n];
    struct circle circles[n];
    int number_of_rectangles = 0, number_of_circles = 0;

    int i;
    char buffer[10];
    for (i = 0; i < n; i++)
    {
        scanf("%s", buffer);
        if (buffer[0] == 'c')
        {
            struct circle next;
            scanf("%d %d %d", &next.x, &next.y, &next.r);
            circles[number_of_circles++] = next;
        }
        else
        {
            struct rectangle next;
            scanf("%d %d %d %d", &next.x1, &next.y1, &next.x2, &next.y2);
            rectangles[number_of_rectangles++] = next;
        }
    }

    int x, y;
    scanf("%d", &n);
    while (n-- > 0)
    {
        int counter = 0;

        scanf("%d %d", &x, &y);
        for (i = 0; i < number_of_circles; i++)
        {
            int dX = x - circles[i].x;
            int dY = y - circles[i].y;
            if (dX * dX + dY * dY <= circles[i].r * circles[i].r) counter++;
        }
        for (i = 0; i < number_of_rectangles; i++)
        {
            if (x >= rectangles[i].x1 && x <= rectangles[i].x2 && y >= rectangles[i].y1 && y <= rectangles[i].y2)
            {
                counter++;
            }
        }
        printf("%d\n", counter);
    }

    return 0;
}