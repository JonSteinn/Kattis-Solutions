#include <stdio.h>
#include <stdint.h>

int main() {
    int64_t n,v;
    scanf("%ld %ld", &n, &v);
    int64_t best = -4294967296L;
    while(n--){
        int64_t a,b,c,curr;
        scanf("%ld %ld %ld", &a, &b, &c);
        curr = a*b*c - v;
        if (curr > best) best = curr;
    }
    printf("%ld\n", best);
    return 0;
}