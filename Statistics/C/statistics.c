#include "stdio.h"

void experiment(int n, int index)
{
    int _min = 1000001;
    int _max = -1000001;
    int next, i;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &next);
        if (next < _min) _min = next;
        if (next > _max) _max = next;
    }
    printf("Case %d: %d %d %d\n", index, _min, _max, _max - _min);
}

int main()
{
    int n, index = 1;
    while (scanf("%d", &n) == 1) experiment(n, index++);
    return 0;
}