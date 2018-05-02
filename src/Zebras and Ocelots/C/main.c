#include <stdio.h>

typedef unsigned long long ull;

ull count(unsigned int n)
{
    ull sum = 0LLU;
    ull step = 1LLU << (n-1);
    while(n--)
    {
        char buffer[2];
        scanf("%s", buffer);
        if (buffer[0] == 'O') sum += step;
        step >>= 1U;
    }
    return sum;
}

int main()
{
    unsigned int n = 0;
    scanf("%u", &n);
    printf("%llu\n", count(n));
    return 0;
}