#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846264338327950288419716939937510582

double get_distance(int n)
{
    double sum = 0.0;
    int first_x, last_x, first_y, last_y;
    scanf("%d %d", &last_x, &last_y);
    first_x = last_x;
    first_y = last_y;
    n--;
    while(n--)
    {
        int x,y;
        scanf("%d %d",&x,&y);
        int dx = x - last_x;
        int dy = y - last_y;
        last_x = x;
        last_y = y;
        sum += sqrt(dx * dx + dy * dy);
    }
    int dx = first_x - last_x;
    int dy = first_y - last_y;
    return sum + sqrt(dx * dx + dy * dy);
}

void output(double x)
{
    if (x < 0) printf("Not possible\n");
    else printf("%.6lf\n", x);
}

void test_case()
{
    int r, n;
    scanf("%d %d",&r,&n);
    double distance = get_distance(n);
    output((distance - 2 * r * PI) / distance);
}

int main()
{
    int tc;
    scanf("%d",&tc);
    while(tc--) test_case();
    return 0;
}