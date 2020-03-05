#include <stdio.h>
#include <math.h>

int main() {
    double x;
    scanf("%lf",&x);
    printf("%d\n", (int)round(x * 5280 / 4.854));
    return 0;
}