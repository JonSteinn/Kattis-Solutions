//
// Created by Jonni on 7/16/2017.
//

#include <stdlib.h>

#ifndef BFS_QUEUE_H
#define BFS_QUEUE_H

typedef struct position pos;
struct position
{
    short x, y;
};

typedef struct fast_queue queue;
struct fast_queue
{
    pos* arr;
    pos* last;
    pos* head;
    pos* tail;
};

void queue_init(queue* q, int max_cap)
{
    q->arr = (pos*)malloc(max_cap * sizeof(pos));
    q->last = q->arr + (max_cap - 1);
    q->head = q->arr;
    q->tail = q->arr;
}

void queue_reset(queue* q)
{
    q->head = q->arr;
    q->tail = q->arr;
}

void queue_destroy(queue* q)
{
    free(q->arr);
}

int queue_is_empty(queue* q)
{
    return q->head == q->tail;
}

void queue_add(queue* q, short x, short y)
{
    q->tail->x = x;
    q->tail->y = y;

    if (q->tail == q->last) q->tail = q->arr;
    else q->tail++;
}

pos* queue_poll(queue* q)
{
    pos* tmp = q->head;
    if (q->head == q->last) q->head = q->arr;
    else q->head++;
    return tmp;
}

#endif
