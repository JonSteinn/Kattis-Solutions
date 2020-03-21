#include <stdio.h>
#include <math.h>

int is_prime(int n)
{
    if (n < 2) return 0;
    if (n < 4) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    if (n < 25) return 1;
    double sq = sqrt(n)+1;
    for (int i = 5; i < sq; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }
    return 1;
}

int next(int n) {
    while (!is_prime(n)) n += 2;
    return n;
}

int main()
{
    while (1)
    {
        int n;
        scanf("%d",&n);
        if (!n) break;
        if (is_prime(n)) printf("%d\n", next(1+(n<<1)));
        else printf("%d (%d is not prime)\n", next(1+(n<<1)), n);
    }
    return 0;
}
