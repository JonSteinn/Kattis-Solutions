#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        int c, d;
        scanf("%d %d", &c, &d);
        printf("%d %d\n", c, d + (d*(d+1))/2);
    }
    return 0;
}