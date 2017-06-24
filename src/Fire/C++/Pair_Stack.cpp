//
// Created by Jonni on 6/24/2017.
//

#include "Pair_Stack.h"

Pair_Stack::Pair_Stack(int max_capacity) {
    memory = (FNode*)malloc(sizeof(FNode) * max_capacity);
    next = memory;
}

Pair_Stack::~Pair_Stack() {
    free(memory);
}

bool Pair_Stack::is_empty() {
    return memory == next;
}

FNode *Pair_Stack::pop() {
    next--;
    return next;
}

void Pair_Stack::push(short x, short y) {
    next->x = x;
    next->y = y;
    next++;
}