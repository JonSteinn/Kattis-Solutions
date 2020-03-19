#include <stdio.h>

int min(int a, int b) {
    return a < b ? a : b;
}

int min_divisible_by(int x) {
    if (x % 4 == 0) return 4;
    if (x % 6 == 0) return x <= 18 ? 6 : min(6, min_divisible_by(x/6));
    if (x % 9 == 0) return x<=27 ? 9 : min(9, min_divisible_by(x/9));
    if (x % 2 == 0) return min(x/2, min_divisible_by(x/2));
    if (x % 3 == 0) return min(x/3, min_divisible_by(x/3));
    for (int i = 4; i <= 46340 /*ceil of sqrt(2**31-1) */ && i*i <= x; i++) {
        if (x % i == 0) return i;
    }
    return x;
}

void min_base(int x) {
    if (x == 3) printf("4\n");
    else if (x < 7) printf("No such base\n");
    else printf("%d\n",min_divisible_by(x-3)); 
}

int main() {
    while(1) {
        int n;
        scanf("%d",&n);
        if (!n) break;
        min_base(n);
    }
    return 0;
}