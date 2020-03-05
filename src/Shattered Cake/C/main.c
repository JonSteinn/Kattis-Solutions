#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);

    int p;
    scanf("%d", &p);

    int total_area = 0;
    while(p--) {
        int w,h;
        scanf("%d %d", &w, &h);
        total_area += w*h;
    }

    printf("%d\n", total_area / n);

    return 0;
}
