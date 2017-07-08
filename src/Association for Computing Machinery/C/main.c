#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return *((int*)a) - *((int*)b);
}

void solves(int first, int* minutes, size_t cnt)
{
    if (first > 300)
    {
        printf("0 0\n");
    }
    else if (first == 300)
    {
        printf("1 300\n");
    }
    else
    {
        int solved = 1;
        int time = first;
        int penalty = first;
        qsort(minutes, cnt, sizeof(int), comparator);
        for (int i = 0; i < cnt; i++)
        {
            if (time + minutes[i] > 300) break;
            time += minutes[i];
            penalty += time;
            solved++;
        }
        printf("%d %d\n", solved, penalty);
    }
}

int main()
{
    int n, k;
    scanf("%d %d",&n, &k);
    int first = 0, minutes[n-1];
    for (int i = 0; i < k; i++) scanf("%d", minutes + i);
    scanf("%d", &first);
    for (int i = k; i < n - 1; i++) scanf("%d", minutes + i);
    solves(first, minutes, n - 1U);
    return 0;
}