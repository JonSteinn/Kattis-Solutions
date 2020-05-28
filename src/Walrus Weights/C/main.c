#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int w[n];
    for (int i = 0; i < n; i++) scanf("%d", w + i);
    int mem[2][1001];
    for (int t = 0; t <= 1000; t++) {
        mem[0][t] = t < (t>w[0] ? t-w[0] : w[0]-t) ? 0 : w[0];
    }
    for (int i = 1; i < n; i++) {
        for (int t = 0; t <= 1000; t++) {
            int incl = w[i] > t ? w[i] : w[i] + mem[!(i&1)][t-w[i]], excl = mem[!(i&1)][t];
            int a1 = t>incl ?  t - incl : incl - t, a2 = t>excl ? t - excl : excl - t;
            mem[i&1][t] = a1==a2 ? (incl > excl ? incl : excl) : (a1<a2 ? incl : excl);
        }
    }
    printf("%d\n", mem[!(n&1)][1000]);
    return 0;
}