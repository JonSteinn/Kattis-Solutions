#include <stdlib.h>
#include "deque.h"

typedef struct {
    Deque* left;
    Deque* right;
} Teque;

Teque* create_teque(int max_operations);
void destroy_teque(Teque* t);
void push_front(Teque* t, int x);
void push_back(Teque* t, int x);
void push_middle(Teque* t, int x);
int get(Teque* t, int i);