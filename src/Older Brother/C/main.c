#include <stdio.h>
#include <math.h>

#define EPISLON 1E-8
#define MIN_PRIME 2

int is_prime(int n) {
    if (n < 2) return 0;
    if (n < 4) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    if (n < 25) return 1;
    for (int i = 5; i*i <= n; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }
    return 1;
}

int is_prime_power(int n)
{
    if (is_prime(n)) return 1;
    int root = 2, next;
    double val;
    while ((next = (int)round(val = pow(n, 1.0 / root))) >= MIN_PRIME)
    {
        root++;
        if ((next < val ? val - next : next - val) > EPISLON) continue;
        if (is_prime(next)) return 1;
    }
    return 0;
}

int main()
{
    int n;
    scanf("%d",&n);
    printf(is_prime_power(n) ? "yes\n" : "no\n");
    return 0;
}