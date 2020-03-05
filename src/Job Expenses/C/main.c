#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);

    int sum = 0;
    while(n--) {
        int x;
        scanf("%d",&x);
        if (x < 0) sum -= x;
    }
    printf("%d\n", sum);
    return 0;
}
