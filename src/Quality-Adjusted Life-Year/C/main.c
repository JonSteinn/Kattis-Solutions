#include <stdio.h>

int main() {
    int n;
    float total = 0.0f;
    scanf("%d", &n);
    while(n--) {
        float q,y;
        scanf("%f %f", &q, &y);
        total += q*y;
    }
    printf("%.3f\n", total);
    return 0;
}