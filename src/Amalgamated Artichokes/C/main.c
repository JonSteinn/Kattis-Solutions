#include <stdio.h>
#include <math.h>

int main()
{
    int p,a,b,c,d,n;
    scanf("%d %d %d %d %d %d",&p,&a,&b,&c,&d,&n);
    double max_dif = 0.0;
    double max_val = p * (sin(a + b) + cos(c + d) + 2);
    for (int i = 2; i <= n; i++)
    {
        double next = p * (sin(a * i + b) + cos(c * i + d) + 2);
        if (max_val < next) max_val = next;
        else if (max_val - next > max_dif) max_dif = max_val - next;
    }
    printf("%.7lf\n", max_dif);
    return 0;
}