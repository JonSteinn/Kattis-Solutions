#include <stdio.h>


void find_min(int* arr, int n, int* _min)
{
    for (int i = *_min; i < n+1; i++) {
        if (arr[i])
        {
            *_min = i;
            return;
        }
    }
}


int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    int arr[n+1];
    for (int i = 2; i < n + 1; i++) arr[i] = i;
    arr[0] = 0; arr[1] = 0;

    int sieved = 0;
    int cross_out = 0;
    int next_min = 2;
    while (sieved < k)
    {
        int start = next_min;
        for (int i = start; i <= n; i += start)
        {
            if (!arr[i]) continue;
            arr[i] = 0;
            cross_out = i;
            sieved++;
            if (sieved == k) break;
        }
        if (sieved < k) find_min(arr, n, &next_min);
    }

    printf("%d\n", cross_out);
    return 0;
}