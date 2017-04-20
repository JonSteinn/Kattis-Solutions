#include <stdio.h>

struct sum 
{
    int a, b;
};

// ignores 2
int is_prime(int n) 
{
    if (n == 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    if (n < 25) return 1;
    int i;
    for (i = 5; i * i <= n; i += 6) if (n % i == 0 || n % (i + 2) == 0) return 0;
    return 1;
}

void experiment() 
{
    int n;
    scanf("%d", &n);
    if (n == 4)
    {
        printf("4 has 1 representation(s)\n");
        printf("2+2\n");
    }
    else
    {
        struct sum _sum[905];
        int end, start = 3, counter = 0;
        while (start <= (end = n - start))
        {
            if (is_prime(start) && is_prime(end))
            {
                _sum[counter].a = start;
                _sum[counter].b = end;
                counter++;
            }
            start += 2;
        }
        printf("%d has %d representation(s)\n", n, counter);
        int i;
        for (i = 0; i < counter; i++) printf("%d+%d\n", _sum[i].a, _sum[i].b);
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0) experiment();
}
