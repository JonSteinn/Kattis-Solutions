#include <stdio.h>
#include <stdint.h>

int main()
{
    uint64_t a,b,c;
    scanf("%llu %llu %llu", &a, &b, &c);
    printf((b+c)/a&1 ? "opponent\n" : "paul\n");
    return 0;
}