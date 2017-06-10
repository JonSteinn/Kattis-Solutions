#include <stdio.h>

struct pos
{
    double x,y;
};

void test_case(int n, double d_sq)
{
    struct pos positions[n];
    int marked[n];
    for (int i = 0; i < n; i++) marked[i] = 0;
    int sour = 0, sweet = n;
    for (int i = 0; i < n; i++) scanf("%lf %lf", &positions[i].x, &positions[i].y);
    for (int i = 0; i < n ; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (!marked[i] || !marked[j])
            {
                double dx = positions[i].x - positions[j].x;
                double dy = positions[i].y - positions[j].y;
                if (dx * dx + dy * dy < d_sq)
                {
                    sour += 2 - marked[i] - marked[j];
                    sweet -= 2 - marked[i] - marked[j];
                    marked[i] = 1;
                    marked[j] = 1;
                }
            }
        }
    }
    printf("%d sour, %d sweet\n", sour, sweet);
}

int main()
{
    while(1)
    {
        double d;
        int n;
        scanf("%lf %d",&d,&n);
        if (d == 0.0 && n == 0) break;
        test_case(n, d * d);
    }
    return 0;
}