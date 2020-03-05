#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int *read_votes(int p, int d) {
    int *votes = (int*)calloc(d << 1, sizeof(int));
    while (p--) {
        int x, a, b;
        scanf("%d %d %d", &x, &a, &b);
        votes[(x-1) << 1] += a;
        votes[((x-1) << 1) + 1] += b;
    }
    return votes;
}

void process_votes(int d, int *votes) {
    int total_w_a = 0, total_w_b = 0, total = 0;
    for (int i = 0; i < d; i++) {
        int a = votes[i<<1], b = votes[(i<<1) + 1];
        int w_a = a, w_b = b;
        total += a + b;
        if (a > b) {
            w_a -= (int)floor((a+b)/2)+1;
            printf("A %d %d\n", w_a, w_b);
        } else {
            w_b -= (int)floor((a+b)/2)+1;
            printf("B %d %d\n", w_a, w_b);
        }
        total_w_a += w_a;
        total_w_b += w_b;
    }
    printf("%.10f\n", abs(total_w_a-total_w_b) / (double)total);
}

int main() {
    int p,d;
    scanf("%d %d", &p, &d);
    int *votes = read_votes(p,d);
    process_votes(d,votes);
    free(votes);
    return 0;
}
