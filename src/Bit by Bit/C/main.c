#include <stdio.h>

#define CMD_LEN 6
#define BIT_LEN 32

void set_bit(int* n, int b)
{
    *n |= (1<<b);
}
void unset_bit(int* n, int b)
{
    *n &= ~(1<<b);
}
int get_bit(int* n, int b)
{
    return *n & (1<<b);
}

int true(int* bits, int* known, int b)
{
    return get_bit(bits, b) && get_bit(known, b);
}

int false(int* bits, int* known, int b)
{
    return !get_bit(bits, b) && get_bit(known, b);
}

void clear(int* bits, int* known)
{
    int i;
    scanf("%d",&i);
    unset_bit(bits, i);
    set_bit(known, i);
}

void set(int* bits, int* known)
{
    int i;
    scanf("%d",&i);
    set_bit(bits, i);
    set_bit(known, i);
}

void or(int* bits, int* known)
{
    int i,j;
    scanf("%d %d",&i,&j);
    if (true(bits, known, i) || true(bits, known, j))
    {
        set_bit(bits, i);
        set_bit(known, i);
    }
    else if (false(bits, known, i) && false(bits, known, j))
    {
        unset_bit(bits, i);
        set_bit(known, i);
    }
    else
    {
        unset_bit(known, i);
    }
}

void and(int* bits, int* known)
{
    int i,j;
    scanf("%d %d",&i,&j);
    if (true(bits, known, i) && true(bits, known, j))
    {
        set_bit(bits, i);
        set_bit(known, i);
    }
    else if (false(bits, known, i) || false(bits, known, j))
    {
        unset_bit(bits, i);
        set_bit(known, i);
    }
    else
    {
        unset_bit(known, i);
    }
}

void print(int* bits, int* known)
{
    char buffer[BIT_LEN+1];
    buffer[BIT_LEN] = '\0';
    for (int i = 0; i < BIT_LEN; i++)
    {
        if (true(bits, known, i)) buffer[BIT_LEN-1-i] = '1';
        else if (false(bits, known, i)) buffer[BIT_LEN-1-i] = '0';
        else buffer[BIT_LEN-1-i] = '?';
    }
    printf("%s\n", buffer);
}

int main()
{
    while(1)
    {
        int n;
        scanf("%d",&n);
        if (!n) break;
        int bits = 0;
        int known = 0;
        while(n--)
        {
            char buffer[CMD_LEN];
            scanf("%s",buffer);
            if (buffer[0] == 'C') clear(&bits, &known);
            else if (buffer[0] == 'S') set(&bits, &known);
            else if (buffer[0] == 'O') or(&bits, &known);
            else and(&bits, &known);
        }
        print(&bits, &known);
    }
    return 0;
}