#include <stdio.h>
#include <string.h>
#include "Stack.h"

#define STATE_SPACE 4096
#define TOTAL_CAVITIES 12

int pebbles_left(int state)
{
    state = state - ((state >> 1) & 0x55555555);
    state = (state & 0x33333333) + ((state >> 2) & 0x33333333);
    return (((state + (state >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

void set_bit(int* x, int b)
{
    *x |= (1 << b);
}

void unset_bit(int* x, int b)
{
    *x &= ~(1 << b);
}

int is_set(int x, int b)
{
    return x & (1 << b);
}

void add_neighbors(stack* open, char* closed, int state)
{
    for (int i = 0; i < 11; i++)
    {
        if (is_set(state, i) && is_set(state, i + 1))
        {
            if (i != 0 && !is_set(state, i - 1))
            {
                int n = state;
                unset_bit(&n, i);
                unset_bit(&n, i+1);
                set_bit(&n, i-1);
                if (!closed[n]) push(open, n);
            }
            if (i != 10 && !is_set(state, i + 2))
            {
                int n = state;
                unset_bit(&n, i);
                unset_bit(&n, i+1);
                set_bit(&n, i+2);
                if (!closed[n]) push(open, n);
            }
        }
    }
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int solve(stack* open, char* closed)
{
    int least = 12;
    while(!is_empty(open))
    {
        int current = pop(open);
        if (closed[current]) continue;
        closed[current] = 1;
        least = min(least, pebbles_left(current));
        if (least == 1) break;
        add_neighbors(open, closed, current);
    }
    return least;
}

int state_to_number(char* str)
{
    int x = 0;
    for (int i = 0; i < TOTAL_CAVITIES; i++)
    {
        if (str[i] == 'o') x |= (1 << i);
    }
    return x;
}

int main()
{
    int n;
    scanf("%d",&n);
    stack open;
    init(&open, STATE_SPACE << 4);
    char closed[STATE_SPACE];
    while(n--)
    {
        char buffer[13];
        scanf("%s",buffer);
        memset(closed, 0, STATE_SPACE * sizeof(char));
        clear(&open);
        push(&open, state_to_number(buffer));
        printf("%d\n", solve(&open, closed));
    }
    destroy(&open);
    return 0;
}