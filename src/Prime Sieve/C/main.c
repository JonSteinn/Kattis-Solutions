#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void unset_bit(int* x, int b)
{
    *x &= ~(1 << b);
}

int is_set(int* x, int b)
{
    return *x & (1 << b);
}

void unset(int* numbers, int number)
{
    int index = number >> 5;
    unset_bit(numbers + index, number - (index << 5));
}

int is_prime(int* numbers, int number)
{
    int index = number >> 5;
    return is_set(numbers + index, number - (index << 5));
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);

    int sq = 1 + (int)(sqrt(n));
    int len = (((n+1) >> 5) << 5) - (n+1) ? ((n + 1) >> 5) + 1 : (n + 1) >> 5;
    int* numbers = (int*)malloc(len * sizeof(int));

    memset(numbers, 0xFF, sizeof(int) * len);
    unset(numbers, 0);
    unset(numbers, 1);

    int counter = 0;
    for (int x = 2; x <= sq; x++)
    {
        if (is_prime(numbers, x))
        {
            for (int j = x * x; j <= n; j += x)
            {
                if (is_prime(numbers, j)) counter++;
                unset(numbers, j);
            }
        }
    }

    printf("%d\n", n - (counter + 1));
    while(q--)
    {
        int x;
        scanf("%d",&x);
        printf("%d\n", is_prime(numbers, x) != 0);
    }
}