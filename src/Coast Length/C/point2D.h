//
// Created by Jonni on 6/21/2017.
//

#include <stdlib.h>

struct point2D
{
    short x;
    short y;
};
typedef struct point2D point;

struct point2D_stack
{
    point* memory;
    point* next;
};
typedef struct point2D_stack stack;

void init(stack* s, int max_capacity)
{
    s->memory = (point*)malloc(max_capacity * sizeof(point));
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

void push(stack* s, short x, short y)
{
    s->next->x = x;
    s->next->y = y;
    s->next++;
}

point* pop(stack* s)
{
    point* tmp = s->next - 1;
    s->next--;
    return tmp;
}
