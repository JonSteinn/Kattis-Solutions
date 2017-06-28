#include <stdio.h>

typedef unsigned long long ull;

char bat(int n, ull k, ull* fibs)
{
    if (n == 1) return 'N';
    if (n == 2) return 'A';
    ull l = fibs[n-2];
    return l < k ? bat(n-1, k-l, fibs) : bat(n-2, k, fibs);
}

int main()
{
    ull fibs[88];
    fibs[0] = 0;
    fibs[1] = 1;
    for (int i = 2; i < 88; i++) fibs[i] = fibs[i-2] + fibs[i-1];
    int n;
    ull k;
    scanf("%u %llu",&n,&k);
    n = n > 89 ? 89 : n;
    printf("%c\n", bat(n, k, fibs));
    return 0;
}