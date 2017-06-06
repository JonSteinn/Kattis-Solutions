#include <stdio.h>

long long honeycomb_walk(int n, long long* walks)
{
    if (walks[n] < 0)
    {
        walks[n-3] = honeycomb_walk(n-3, walks);
        walks[n-2] = honeycomb_walk(n-2, walks);
        walks[n-1] = honeycomb_walk(n-1, walks);
        walks[n] = (walks[n-1]*n + 24*walks[n-2]*n + 36*walks[n-3]*n - 24*walks[n-2] - 72*walks[n-3])*(n - 1)/ (n * n);
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
