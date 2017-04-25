#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int min_sum = 0, sec_sum = 0;
    while (n-->0)
    {
        int m, s;
        scanf("%d %d", &m, &s);
        min_sum += m;
        sec_sum += s;
    }
    double sl_min = sec_sum / 60.0 / min_sum;
    if (sl_min <= 1.0) printf("measurement error\n");
    else printf("%.9f\n", sl_min);
}