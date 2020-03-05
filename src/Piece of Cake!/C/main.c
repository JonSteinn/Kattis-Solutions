#include <stdio.h>

int max(int a, int b) { return a < b ? b : a; }

int main() {
    int n, h, v;
    scanf("%d %d %d", &n, &h, &v);
    printf("%d\n", max(n-h,h) * max(n-v,v) * 4);
    return 0;
}