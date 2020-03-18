#include <stdlib.h>

typedef struct {
    int* arr;
    int lo;
    int hi;
    int mem_size;
    int count;
} Deque;

Deque* create_deque(int mem_size);
void destroy_deque(Deque* d);
void push_left(Deque* d, int x);
void push_right(Deque* d, int x);
int pop_left(Deque* d);
int pop_right(Deque* d);
int get_by_index(Deque* d, int i);