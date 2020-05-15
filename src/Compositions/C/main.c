#include <stdio.h>

int compositions(int n, int m, int k, int *mem) {
    if (n==0) return 1;
    int offset = (30*(n-1)+m)*30 + k;
    if (*(mem+offset) == -1) {
        int total = 0;
        for (int i = n; i > 0; i--) {
            if (i % k != m) total += compositions(n-i, m, k, mem);
        }
        *(mem+offset) = total;
    }
    return *(mem+offset);
}

int main() {
    int mem[27000] = {[0 ... 26999] = -1}; // 30*30*30
    int tc,c,n,m,k;
    scanf("%d",&tc);
    while(tc--) {
        scanf("%d %d %d %d", &c, &n, &m, &k);
        printf("%d %d\n", c, compositions(n, m, k, (int*)mem));
    }
    return 0;
}