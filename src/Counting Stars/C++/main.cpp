#include <stdio.h>
#include "Sky.h"

int main() {
    int m, n, test_case = 1;
    while (scanf("%d %d", &m, &n) == 2) {
        printf("Case %d: %d\n", test_case++, Sky(m,n).number_of_stars());
    }
    return 0;
}