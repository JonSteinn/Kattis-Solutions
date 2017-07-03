#include <stdio.h>

typedef unsigned long long ull;

ull binom[51][51];

ull binomial(int n, int k)
{
    return (k < 0 || k > n) ? 0 : binom[n][k];
}

ull count(int n, int twos)
{
    int ones = n - 2 * twos;
    ull b = binomial(ones + twos, twos);
    return b * b;
}

void boundaries(int n, int* lo, int* hi)
{
    *hi = n >> 1;
    *lo = n%3 ? n/3 + 1 : n/3;
}

void steps()
{
    int t, n;
    scanf("%d %d",&t,&n);
    n >>= 1;
    int a, b;
    boundaries(n, &a, &b);
    ull sum = 0;
    for (int i = a; i <= b; i++) sum += count(n, i);
    printf("%d %llu\n", t, sum);
}

void set_binomials()
{
    binom[0][0] = 1;
    for (int i = 1; i <= 50; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            binom[i][j] = (i-1 >= 0 && j-1 >= 0 ? binom[i-1][j-1] : 0) + (i-1 >= 0 && j <= i ? binom[i-1][j] : 0);
        }
    }
}

int main()
{
    set_binomials();
    int n;
    scanf("%d",&n);
    while(n--) steps();
    return 0;
}