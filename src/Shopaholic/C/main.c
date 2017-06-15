#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return *((int*)b) - *((int*)a);
}

int main()
{
    int n;
    scanf("%d",&n);
    int prices[n];
    for (int i = 0; i < n; i++) scanf("%d",prices+i);
    qsort(prices, (size_t)n, sizeof(int), comparator);
    long long sum = 0L;
    for (int i = 2; i < n; i += 3) sum += prices[i];
    printf("%lld",sum);
    return 0;
}