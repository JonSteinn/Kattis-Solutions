#include <stdio.h>

void backward(int d, int h, int m)
{
    int d_h = d / 60;
    int d_m = d % 60;
    h -= d_h;
    m -= d_m;
    if (m < 0)
    {
        h -= 1;
        m += 60;
    }
    if (h < 0)
    {
        h += 24;
    }
    printf("%d %d\n",h,m);
}

void forward(int d, int h, int m)
{
    int d_h = d / 60;
    int d_m = d % 60;
    h += d_h;
    m += d_m;
    if (m >= 60)
    {
        h += 1;
        m -= 60;
    }
    if (h >= 24)
    {
        h -= 24;
    }
    printf("%d %d\n", h, m);
}

void test_case()
{
    char x[2];
    int d,h,m;
    scanf("%s %d %d %d", x, &d, &h, &m);
    if (x[0] == 'F') forward(d,h,m);
    else backward(d,h,m);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}