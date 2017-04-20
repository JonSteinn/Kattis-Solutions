#include <stdio.h>

#define EULER_TOTIENT 1000000006L
#define PRIME 1000000007L

static long long pre_calc[41] =
{
    1L,
    3L,
    9L,
    27L,
    81L,
    243L,
    729L,
    2187L,
    6561L,
    19683L,
    59049L,
    177147L,
    531441L,
    1594323L,
    4782969L,
    14348907L,
    43046721L,
    129140163L,
    387420489L,
    162261460L,
    486784380L,
    460353133L,
    381059392L,
    143178169L,
    429534507L,
    288603514L,
    865810542L,
    597431612L,
    792294829L,
    376884473L,
    130653412L,
    391960236L,
    175880701L,
    527642103L,
    582926302L,
    748778899L,
    246336683L,
    739010049L,
    217030133L,
    651090399L,
    953271190L
};

long long remain(long long d)
{
    if (d <= 40) return pre_calc[d];
    long long rem = remain(d >> 1);
    return (((d & 1) ? 3 : 1) * rem * rem) % PRIME;
}

void experiment()
{
    long long d;
    scanf("%lld", &d);
    d = (d - 1) << 1;
    if (d >= EULER_TOTIENT) d -= (d / EULER_TOTIENT) * EULER_TOTIENT;
    printf("%lld\n", (8 * remain(d)) % PRIME);
}

int main()
{
    int n;
    scanf("%d", &n);
    while(n-- > 0) experiment();
    return 0;
}