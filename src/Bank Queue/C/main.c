#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return *((int*)b) - *((int*)a);
}

int main()
{
    int n, t;
    scanf("%d %d",&n,&t);

    size_t lengths[t + 1];
    int current[t + 1];
    memset(lengths, 0, (t+1) * sizeof(size_t));
    memset(current, 0, (t+1) * sizeof(int));
    int money[t + 1][n];

    for (int i = 0; i < n; i++)
    {
        int _m,_t;
        scanf("%d %d",&_m,&_t);
        money[_t][lengths[_t]++] = _m;
    }

    for (int i = 0; i <= t; i++)
    {
        if (lengths[i] > 1) qsort(money[i], lengths[i], sizeof(int), comparator);
    }

    int sum = 0;
    for (int i = t; i >= 0; i--)
    {
        int max_above = -1;
        int max_above_index = -1;
        for (int j = i; j <= t; j++)
        {
            if (lengths[j] && money[j][current[j]] > max_above)
            {
                max_above = money[j][current[j]];
                max_above_index = j;
            }
        }
        if (max_above_index != -1)
        {
            sum += money[max_above_index][current[max_above_index]];
            current[max_above_index]++;
            lengths[max_above_index]--;
        }
    }

    printf("%d\n",sum);

    return 0;
}