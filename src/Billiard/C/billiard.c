#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971693993751

int main()
{
    int a,b,s,m,n;
    while(1)
    {
        scanf("%d %d %d %d %d",&a,&b,&s,&m,&n);
        if (!a && !b && !s && !m && !n) break;
        double dist_X = a * m;
        double dist_Y = b * n;
        double dist_total = sqrt(dist_X * dist_X + dist_Y * dist_Y);
        double velocity = dist_total / s;
        double angle = 180.0 * acos(dist_X / dist_total) / PI;
        printf("%.2f %.2f\n", angle, velocity);
    }
    return 0;
}