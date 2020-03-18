#include "teque.h"

Teque* create_teque(int max_operations) {
    int size_needed = (max_operations >> 1) + 2;
    Teque* t = (Teque*)malloc(sizeof(Teque));
    t->left = create_deque(size_needed);
    t->right = create_deque(size_needed);
    return t;
}

void destroy_teque(Teque* t) {
    destroy_deque(t->left);
    destroy_deque(t->right);
    free(t);
}

void push_front(Teque* t, int x) {
    push_left(t->left, x);
    if (t->left->count > t->right->count + 1) {
        push_left(t->right, pop_right(t->left));
    }
}

void push_back(Teque* t, int x) {
    push_right(t->right, x);
    if (t->right->count > t->left->count) {
        push_right(t->left, pop_left(t->right));
    }
}

void push_middle(Teque* t, int x) {
    push_left(t->right, x);
    if (t->right->count > t->left->count) {
        push_right(t->left, pop_left(t->right));
    }
}

int get(Teque* t, int i) {
    return i < t->left->count ? get_by_index(t->left, i) : get_by_index(t->right, i - t->left->count);
}