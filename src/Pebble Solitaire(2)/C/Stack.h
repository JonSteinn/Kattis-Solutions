//
// Created by Jonni on 7/8/2017.
//

#ifndef DFS_STACK_H
#define DFS_STACK_H

#include <stdlib.h>

typedef struct dfs_stack stack;
struct dfs_stack
{
    int* memory;
    int* next;
};

void init(stack* s, int max_capacity)
{
    s->memory = (int*)malloc(sizeof(int) * max_capacity);
    s->next = s->memory;
}

void destroy(stack* s)
{
    free(s->memory);
}

int is_empty(stack* s)
{
    return s->memory == s->next;
}

int pop(stack* s)
{
    return *(--(s->next));
}

void push(stack* s, int v)
{
    *(s->next++) = v;
}

void clear(stack* s)
{
    s->next = s->memory;
}

#endif