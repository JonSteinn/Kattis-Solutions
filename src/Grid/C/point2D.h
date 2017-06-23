//
// Created by Jonni on 6/21/2017.
//

#include <stdlib.h>

struct point2D
{
    short x;
    short y;
    int cost;
};
typedef struct point2D point;

struct point2D_queue
{
    point* memory;
    point* tail;
    point* head;
};
typedef struct point2D_queue queue;

void init(queue* s, int max_capacity)
{
    s->memory = (point*)malloc(max_capacity * sizeof(point));
    s->tail = s->memory;
    s->head = s->memory;
}

void destroy(queue* s)
{
    free(s->memory);
}

int is_empty(queue* s)
{
    return s->tail == s->head;
}

void add(queue* s, short x, short y, int cost)
{
    s->tail->x = x;
    s->tail->y = y;
    s->tail->cost = cost;
    s->tail++;
}

point* poll(queue* s)
{
    point* tmp = s->head;
    s->head++;
    return tmp;
}
