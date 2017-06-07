#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971

void test_case()
{
    int moves;
    scanf("%d",&moves);
    double x = 0.0, y = 0.0, theta = PI / 2.0;
    while(moves--)
    {
        double delta_theta, radius;
        scanf("%lf %lf",&delta_theta,&radius);
        theta += delta_theta * PI / 180.0;
        x += radius * cos(theta);
        y += radius * sin(theta);
    }
    printf("%.4lf %.4lf\n",x,y);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}