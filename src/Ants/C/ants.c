#include <stdio.h>

void test_case()
{
    int l, n;
    scanf("%d %d", &l, &n);
    int min_max = 0, max_max = 0;
    while(n--)
    {
        int m, k;
        scanf("%d",&m);
        k = l - m;
        if (m < k) m^=k^=m^=k;
        if (k > min_max) min_max = k;
        if (m > max_max) max_max = m;
    }
    printf("%d %d\n", min_max, max_max);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}