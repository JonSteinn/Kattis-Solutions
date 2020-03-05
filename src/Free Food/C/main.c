#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);

    int sum = 0;
    int year[365] = {0};
    while(n-- && sum < 365) {
        int from, to;
        scanf("%d %d", &from, &to);
        for (int i = from - 1; i < to; i++) {
            if (year[i]) continue;
            year[i] = 1;
            sum += 1;
        }
    }
    printf("%d\n", sum);
    return 0;
}
