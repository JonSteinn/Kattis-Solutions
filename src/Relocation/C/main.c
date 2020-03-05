#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,q;
    scanf("%d %d", &n, &q);

    int companies[n];
    for (int i = 0; i < n; i++) scanf("%d", companies + i);

    while(q--) {
        int type, a,b;
        scanf("%d %d %d", &type, &a, &b);
        if (type == 1) {
            companies[a-1] = b;
        } else {
            printf("%d\n", abs(companies[a-1] - companies[b-1]));
        }
    }

    return 0;
}