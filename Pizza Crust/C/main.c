#include <stdio.h>
#include <string.h>

double ratio(int R, int C)
{
    int no_cheese_radius = R-C;
    return ((double)(no_cheese_radius * no_cheese_radius * 100)) / (R * R);
}

int main()
{
    int R, C;
    scanf("%d %d", &R, &C);
    printf("%.10f\n", ratio(R, C));
    return 0;
}