#include <stdio.h>

int SSD(int b, int n) {
    int total = 0;
    while (n>0) {
        int next = (n % b);
        total += next*next;
        n /= b;
    }
    return total;
}

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        int c, b, x;
        scanf("%d %d %d", &c, &b, &x);
        printf("%d %d\n", c, SSD(b, x));
    }
    return 0;
}