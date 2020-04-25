#include "set.h"

int set_contains(IntSet *set, int n) {
    return set->bits[n/INT_BITS] & (1<<(n%INT_BITS));
}

void set_add(IntSet *set, int n) {
    set->bits[n/INT_BITS] |= (1<<(n%INT_BITS));
}

void set_remove(IntSet *set, int n) {
    set->bits[n/INT_BITS] &= ~(1<<(n%INT_BITS));
}

void set_complement_up_to(IntSet* set, int max) {
    int x = max / INT_BITS;
    for (int i = 0; i < x; i++) set->bits[i] = ~set->bits[i];
    if (x < 125) set->bits[x] = ~set->bits[x] & ((1 << (max % INT_BITS))-1);
}