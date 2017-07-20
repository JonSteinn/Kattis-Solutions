#include <stdio.h>
#include <string.h>

// Brute force, O(n^2), should is fine for <= 256

int term(int* p1, int* p2, int t)
{
    int sum = 0;
    for (int i = 0; i <= t; i++) sum += p1[i] * p2[t - i];
    return sum;
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int pol1[600], pol2[600];
        memset(pol1, 0, sizeof(int) * 600);
        memset(pol2, 0, sizeof(int) * 600);
        int deg1, deg2, deg_sum;
        scanf("%d", &deg1);
        for (int i = 0; i <= deg1; i++) scanf("%d", pol1 + i);
        scanf("%d", &deg2);
        for (int i = 0; i <= deg2; i++) scanf("%d", pol2 + i);
        deg_sum = deg1 + deg2;
        printf("%d\n%d", deg_sum, term(pol1, pol2, 0));
        for (int i = 1; i <= deg_sum; i++) printf(" %d", term(pol1, pol2, i));
        putchar('\n');
    }
    return 0;
}