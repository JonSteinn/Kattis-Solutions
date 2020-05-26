#include <stdio.h>
#include "inversions.h"

int main() {
    int n,x;
    scanf("%d", &n);
    InversionCounter *ic = ic_create(n);
    for (int i = 0; i < n; i++) {
        scanf("%d",&x);
        ic_process_next_element(ic, x);
    }
    printf("%llu\n", ic_get_total(ic));
    //ic_destroy(ic);
    return 0;
}