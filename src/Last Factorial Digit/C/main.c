#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        int k;
        scanf("%d",&k);
        printf("%d\n", k==3 ? 6 : k < 5 ? k : 0);
    }
}