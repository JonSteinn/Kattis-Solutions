#include <stdio.h>

typedef unsigned long long ull;

int game(ull a, ull b)
{
    int win = 1;
    while ((a % b) && (a < (b << 1)))
    {
        a = a - b;
        if (a-b) a^=b^=a^=b;
        win = !win;
    }
    return win;
}

int main()
{
    ull a, b;
    scanf("%llu %llu", &a, &b);
    if (a < b) a^= b^= a^= b;
    printf(game(a,b) ? "win\n" : "lose\n");
    return 0;
}