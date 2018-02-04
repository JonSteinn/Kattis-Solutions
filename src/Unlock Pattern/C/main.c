#include <stdio.h>
#include <stdint.h>
#include <math.h>

typedef struct
{
    uint8_t x, y;
} point2d;

uint8_t pow2(uint8_t x)
{
    return x * x;
}

double distance(point2d* p1, point2d* p2)
{
    return sqrt(pow2(p1->x - p2->x) + pow2(p1->y - p2->y));
}

double path(point2d* pos)
{
    double d = 0.0;
    for (int i = 0; i < 8; i++) d += distance(pos + i, pos + i + 1);
    return d;
}

void read_pos(point2d* pos)
{
    for (uint8_t y = 0; y < 3; y++)
    {
        for (uint8_t x = 0; x < 3; x++)
        {
            int32_t index = 0;
            scanf("%d", &index);
            pos[index - 1].x = x;
            pos[index - 1].y = y;
        }
    }
}

int main()
{
    point2d pos[9];
    read_pos(pos);
    printf("%.10f\n", path(pos));
    return 0;
}