#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, x, c = 0, *hs = (short*)calloc(1000000,sizeof(int));
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&x);
        if (hs[x]) hs[x]--;
        else c++;
        hs[x-1]++;
    }
    printf("%d\n", c);
    free(hs);
    return 0;
}