#include <stdio.h>
#include <math.h>

int main() {
    double x;
    scanf("%lf", &x);
    printf("%.5f\n", pow(x, 1/x));
    return 0;
}