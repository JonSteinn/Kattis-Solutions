#include <stdio.h>

int main()
{
    int n = 0;
    scanf("%d", &n);
    while(n--)
    {
        double b, p;
        scanf("%lf %lf", &b, &p);
        double x = 60.0 / p;
        double xb = x * b;
        printf("%.6f %.6f %.6f\n", xb - x, xb, xb + x);
    }
    return 0;
}