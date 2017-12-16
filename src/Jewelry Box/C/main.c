#include <stdio.h>
#include <math.h>

double box(int x, int y)
{
    // critical points
    double h1 = (y + x - sqrt(y * y - x * y + x * x)) / 6.0;
    double h2 = (y + x + sqrt(y * y - x * y + x * x)) / 6.0;

    if (h1 < 0) return 2 * (y - 2 * h2) * (x - 2 * h2);
    else if (h2 < 0) return h1 * (y - 2 * h1) * (x - 2 * h1);
    else return fmax(h1 * (y - 2 * h1) * (x - 2 * h1), 2 * (y - 2 * h2) * (x - 2 * h2));
}

int main()
{
    int n = 0;
    scanf("%d", &n);
    while(n--)
    {
        int x = 0, y = 0;
        scanf("%d %d", &x, &y);
        printf("%.10f\n", box(x,y));
    }
    return 0;
}