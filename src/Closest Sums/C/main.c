#include <stdio.h>

int abs(int x)
{
    return x < 0 ? -x : x;
}

int find(int* arr, int len, int goal)
{
    int sum = 0;
    int distance = 999999999;

    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            int s = arr[i] + arr[j];
            int d = abs(goal - s);
            if (d < distance)
            {
                distance = d;
                sum = s;
            }
        }
    }

    return sum;
}

int main()
{
    int n, case_number = 1;
    while (scanf("%d",&n) == 1)
    {
        printf("Case %d:\n", case_number++);
        int arr[n];
        for (int i = 0; i < n; i++) scanf("%d", arr + i);
        int q;
        scanf("%d", &q);
        while (q--)
        {
            int value;
            scanf("%d",&value);
            printf("Closest sum to %d is %d.\n", value, find(arr, n, value));
        }
    }
    return 0;
}