#ifndef _INVERSION_COUNTER_H
#define _INVERSION_COUNTER_H

#include <stdlib.h>
#include "fenwick.h"

/*
The idea here is that given some permutation a1a2...an, that
for any element ai (with i>2), it has a mega inversion as The
leas element for all pairs of non-equal larger elements to it
left. If we store how many elements are larger to the left for
each element, we can sum them to get this number of pairs.

As an example. Suppose we have n = 5 and at some point we come
across x = 2. For a mid element 3, we have summed up the total
larger elements to the left of them (could be 4 for the first 3
and 7 for the second three, yeilding a total of 11 if only these
two 3s). Then there are 11 mega inversions with x-3-2 for the 2
we just looked at (there can be more of this form for later 2s).
We also need to repeat this for 4 but since n = 5, 5 can't be a
middle element and we are done for this particular 2 we just came
across. This is repeated for the entire array.
*/

typedef struct {
    FenwickTree *counter;
    FenwickTree *left_larger;
    int n;
    ull mega_inversions;
} InversionCounter;

void ic_process_next_element(InversionCounter *ic, int x) {
    fwt_increment(ic->counter, x);
    // Can't have smaller if n
    if (x != ic->n) {
        fwt_update(ic->left_larger, x, fwt_sum_from(ic->counter, x+1));
        // Can't be least of three uniques if n-1
        if (x != ic->n -1) ic->mega_inversions += fwt_sum_from(ic->left_larger, x+1);
    }
}

ull ic_get_total(InversionCounter *ic) {
    return ic->mega_inversions;
}

InversionCounter *ic_create(int n) {
    InversionCounter *inv = (InversionCounter*)malloc(sizeof(InversionCounter));
    inv->n = n;
    inv->counter = fwt_create(n);
    inv->left_larger = fwt_create(n);
    inv->mega_inversions = 0LLU;
    return inv;
}

void ic_destroy(InversionCounter *ic) {
    fwt_destroy(ic->counter);
    fwt_destroy(ic->left_larger);
    free(ic);
}

#endif