#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int p_tea[n];
    for (int i = 0; i < n; i++) scanf("%d", p_tea + i);

    int m;
    scanf("%d",&m);
    int p_top[m];
    for (int i = 0; i < m; i++) scanf("%d", p_top + i);

    int cheapest = 99999;
    for (int i = 0; i < n; i++)
    {
        int k;
        scanf("%d", &k);
        for (int j = 0; j < k; j++)
        {
            int tmp;
            scanf("%d",&tmp);
            int curr = p_tea[i] + p_top[tmp-1];
            if (curr < cheapest) cheapest = curr;
        }
    }
    int money;
    scanf("%d", &money);
    int cups = money / cheapest;
    printf("%d\n", cups > 0 ? cups - 1 : 0);
    return 0;
}