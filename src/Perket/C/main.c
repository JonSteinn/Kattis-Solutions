#include <stdio.h>

typedef struct ingredient pair;
struct ingredient
{
    int s;
    int b;
};

int diff(int subset, pair* arr)
{
    int prod = 1;
    int sum = 0;
    int index = 0;

    while (subset)
    {
        if (subset&1)
        {
            prod *= arr[index].s;
            sum += arr[index].b;
        }
        index++;
        subset >>= 1;
    }

    return prod > sum ? prod - sum : sum - prod;
}

int main()
{
    int n;
    scanf("%d",&n);

    pair arr[n];
    for (int i = 0; i < n; i++) scanf("%d %d", &arr[i].s, &arr[i].b);

    int upper_limit = (1<<n)-1;
    int min_diff = 2147483647;

    for (int i = 1; i <= upper_limit; i++)
    {
        int d = diff(i, arr);
        if (d < min_diff) min_diff = d;
    }

    printf("%d\n", min_diff);

    return 0;
}