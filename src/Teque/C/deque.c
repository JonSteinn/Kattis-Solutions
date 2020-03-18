#include "deque.h"

Deque* create_deque(int mem_size) {
    Deque* d = (Deque*)malloc(sizeof(Deque));
    d->arr = (int*)malloc(sizeof(int)*mem_size);
    d->lo = mem_size>>1;
    d->hi = d->lo;
    d->count = 0;
    d->mem_size = mem_size;
    return d;
}

void destroy_deque(Deque* d) {
    free(d->arr);
    free(d);
}

void push_left(Deque* d, int x) {
    d->lo = (d->mem_size + d->lo - 1) % d->mem_size;
    d->arr[d->lo] = x;
    d->count++;
}

void push_right(Deque* d, int x) {
    if (d->count == 0) {
        push_left(d,x);
    } else {
        d->arr[d->hi] = x;
        d->hi = (d->hi + 1) % d->mem_size;
        d->count++;
    }
}

int pop_left(Deque* d) {
    int ret = d->arr[d->lo];
    d->lo = (d->lo + 1) % d->mem_size;
    d->count--;
    return ret;
}

int pop_right(Deque* d) {
    d->hi = (d->mem_size + d->hi - 1) % d->mem_size;
    d->count--;
    return d->arr[d->hi];
}

int get_by_index(Deque* d, int i) {
    return d->arr[(d->lo + i) % d->mem_size];
}