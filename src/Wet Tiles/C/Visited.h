//
// Created by Jonni on 7/16/2017.
//

#include <stdlib.h>
#include <string.h>

#ifndef VISITED_H
#define VISITED_H

typedef struct int_set visited;
struct int_set
{
    int* arr;
    int arr_size;
};

void visited_init(visited* v, int max_elements)
{
    v->arr_size = max_elements % 32 ? max_elements / 32 + 1 : max_elements / 32;
    v->arr = (int*)malloc(sizeof(int) * v->arr_size);
}

void visited_destroy(visited* v)
{
    free(v->arr);
}

void visited_unset_all(visited* v)
{
    memset(v->arr, 0, v->arr_size * sizeof(int));
}

void visited_set(visited* v, int n)
{
    v->arr[n / 32] |= (1 << (n % 32));
}

int visited_is_set(visited* v, int n)
{
    return v->arr[n / 32] & (1 << (n % 32));
}

#endif VISITED_H
