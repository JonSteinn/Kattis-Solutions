#include <stdio.h>

int main()
{
    int published, impact;
    scanf("%d %d", &published, &impact);
    printf("%d\n", published * (impact - 1) + 1);
}
// x / published >  impact - 1
// x > published * (impact - 1)
// min { x in Z : x > published * (impact - 1) } = published * (impact - 1) + 1