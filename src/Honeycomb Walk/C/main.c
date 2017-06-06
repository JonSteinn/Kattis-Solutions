#include <stdio.h>

long long honeycomb_walk(int n, long long* walks)
{
    if (walks[n] < 0)
    {
        long long c = honeycomb_walk(n-3, walks);
        long long b = honeycomb_walk(n-2, walks);
        long long a = honeycomb_walk(n-1, walks);
        return (a*n + 24*b*n + 36*c*n - 24*b - 72*c)*(n - 1)/ (n * n);
    }
    return walks[n];
}

int main()
{
    long long walks[15];
    walks[0] = 1;
    walks[1] = 0;
    walks[2] = 6;
    for (int i = 3; i < 15; i++) walks[i] = -1;
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int path;
        scanf("%d",&path);
        printf("%lld\n",honeycomb_walk(path, walks));
    }
    return 0;
}