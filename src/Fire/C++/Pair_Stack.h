//
// Created by Jonni on 6/24/2017.
//

#ifndef PAIR_STACK_H
#define PAIR_STACK_H

#include <stdlib.h>

struct FNode {
    short x;
    short y;
};

class Pair_Stack {
public:
    Pair_Stack(int max_capacity);
    ~Pair_Stack();
    bool is_empty();
    FNode* pop();
    void push(short x, short y);
private:
    FNode* memory;
    FNode* next;
};


#endif
