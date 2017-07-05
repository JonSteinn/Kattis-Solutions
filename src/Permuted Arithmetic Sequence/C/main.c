#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return *((int*)a) - *((int*)b);
}

int arithmetic(int len, int* arr)
{
    int val = arr[1] - arr[0];
    for (int i = 2; i < len; i++)
    {
        if (val != arr[i] - arr[i-1]) return 0;
    }
    return 1;
}

void type(int len, int* arr)
{
    if (arithmetic(len, arr))
    {
        printf("arithmetic\n");
        return;
    }
    qsort(arr, (size_t)len, sizeof(int), comparator);
    if (arithmetic(len, arr)) printf("permuted arithmetic\n");
    else printf("non-arithmetic\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    while(n--)
    {
        int k;
        scanf("%d", &k);

        int arr[k];
        for (int i = 0; i < k; i++) scanf("%d", arr + i);
        type(k, arr);
    }
    return 0;
}