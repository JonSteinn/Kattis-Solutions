#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);

    double curr_t, curr_v, prev_t, prev_v, sum = 0.0;
    scanf("%lf %lf", &prev_t, &prev_v);

    while (--n) {
        scanf("%lf %lf", &curr_t, &curr_v);
        sum += (prev_v + curr_v) / 2.0 * (curr_t - prev_t);
        prev_t = curr_t;
        prev_v = curr_v;
    }

    printf("%.6f\n", sum / 1000.0);

    return 0;
}
