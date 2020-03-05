#include <stdio.h>


int is_harshad(int n) {
    int x = n, sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    return n % sum == 0;
}

int main() {
    // https://oeis.org/A005349 seem to be rather dense
    // In that case, bruteforce will do fine
    int n;
    scanf("%d",&n);
    while(1) {
        if (is_harshad(n)) {
            printf("%d\n", n);
            break;
        }
        n++;
    }
    return 0;
}
