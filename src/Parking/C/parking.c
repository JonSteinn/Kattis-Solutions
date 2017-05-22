#include <stdio.h>

void swap(int* a, int* b)
{
    int c = *a;
    *a = *b;
    *b = c;
}

void three_sort(int* arr)
{
    if (arr[0] > arr[2]) swap(arr, arr+2);
    if (arr[0] > arr[1]) swap(arr, arr+1);
    if (arr[1] > arr[2]) swap(arr+1, arr+2);
}

int main()
{
    int prices[3];
    scanf("%d %d %d",prices,prices+1,prices+2);

    int min[3], max[3];
    for (int i = 0; i < 3; i++) scanf("%d %d", min + i, max + i);

    three_sort(min);
    three_sort(max);

    int sum = 0;
    for (int i = min[0]; i <= max[2]; i++)
    {
        int amount = (i >= min[0]) + (i >= min[1]) + (i >= min[2]) - (i >= max[0]) - (i >= max[1]) - (i >= max[2]);
        sum += prices[amount-1] * amount;
    }
    printf("%d\n", sum);
    return 0;
}