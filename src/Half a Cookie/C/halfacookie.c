#include <stdio.h>
#include <math.h>

#define PI 3.1415926535897932384626433832795028841971693993751

// Formula:
// R * R * acos((R - h)/R) - (R - h) * sqrt(2 * R * h - h * h)
// From:
// http://mathworld.wolfram.com/CircularSegment.html

int main()
{
    double R, x, y;
    while(scanf("%lf %lf %lf", &R, &x, &y) == 3)
    {
        double distance;
        if ((distance = x * x + y * y) >= R * R) printf("miss\n");
        else
        {
            distance = sqrt(distance);
            double h = R - distance;
            double segment_a = R * R * acos((R - h)/R) - (R - h) * sqrt(2 * R * h - h * h);
            double circle_a = PI * R * R;
            double remaining_a = circle_a - segment_a;
            if (remaining_a < segment_a) printf("%.7f %.7f\n", segment_a, remaining_a);
            else printf("%.7f %.7f\n", remaining_a, segment_a);
        }
    }

    return 0;
}