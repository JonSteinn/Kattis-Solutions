#include <stdio.h>
#include <math.h>

int main() {
    int a,b,c,d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    double s = (a+b+c+d)/2.0;
    printf("%.6f\n", sqrt((s-a)*(s-b)*(s-c)*(s-d)));

    return 0;
}
