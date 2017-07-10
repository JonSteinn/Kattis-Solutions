//
// Created by Jonni on 7/10/2017.
//

#ifndef STACK_H
#define STACK_H

#include <malloc.h>

typedef struct node pos;
struct node
{
    char r, c;
};

typedef struct point_stack stack;
struct point_stack
{
    int count;
    pos* mem;
    pos* curr;
};

typedef struct char_stack c_stack;
struct char_stack
{
    char* mem;
    char* curr;
};

void init(stack *s, int max_cap)
{
    s->mem = (pos*)malloc(sizeof(pos) * max_cap);
}

void clear(stack *s)
{
    s->curr = s->mem;
    s->count = 0;
}

void destroy(stack *s)
{
    free(s->mem);
}

int empty(stack *s)
{
    return !s->count;
}

void push(stack *s, char r, char c)
{
    s->curr->r = r;
    s->curr->c = c;
    s->curr++;
    s->count++;
}

pos* pop(stack *s)
{
    s->count--;
    return --s->curr;
}

#endif
