#include <stdio.h>

int main() {
    int n,x,y,s=0;
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &x, &y);
        s += (y-x);
    }
    printf("%.3f\n", s/(double)n);
    return 0;
}

// See py for explanation