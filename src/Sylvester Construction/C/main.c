#include <stdio.h>

int val(int x, int y, unsigned long long n)
{
    int v = 1;
    while (!(n&1))
    {
        n >>= 1;
        if (x < n)
        {
            if (y >= n) y -= n;
        }
        else
        {
            x -= n;
            if (y >= n)
            {
                y -= n;
                v = -v;
            }
        }
    }
    return v;
}

void test_case()
{
    unsigned long long n;
    int x, y, w, h;
    scanf("%llu %d %d %d %d", &n, &x, &y, &w, &h);
    for (int _y = y; _y < y + h; _y++)
    {
        if (w) printf("%d", val(x, _y, n));
        for (int _x = x + 1; _x < x + w; _x++)
        {
            printf(" %d", val(_x, _y, n));
        }
        putchar('\n');
    }
    putchar('\n');
}

int main()
{
    int tc;
    scanf("%d",&tc);
    while(tc--) test_case();
    return 0;
}