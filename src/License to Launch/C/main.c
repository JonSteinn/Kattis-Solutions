#include <stdio.h>

int main() {
    int min_val = 1000000001, min_day = -1;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int j;
        scanf("%d", &j);
        if (j < min_val) {
            min_val = j;
            min_day = i;
        }
    }
    printf("%d\n", min_day);
    return 0;
}