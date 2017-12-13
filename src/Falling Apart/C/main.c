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
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", arr + i);
    qsort((void*)arr, (size_t)n, sizeof(int), comparator);
    int a = 0, b = 0;
    for (int i = 0; i < n; i++)
    {
        if (i&1) b += arr[i];
        else a += arr[i];
    }
    printf("%d %d\n", a, b);
    return 0;
}