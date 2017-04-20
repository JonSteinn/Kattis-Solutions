#include <stdio.h>
#include <stdlib.h>

// Best scenario:
// x is lowest 2, y is largest 2 (or vv)
// than min(x)*min(y) is our rectangle (would not complete with the larger sides).

void swap(int* a, int *b)
{
    *a^=*b;
    *b^=*a;
    *a^=*b;
}
int main()
{
    int* n = (int*)malloc(128);
    scanf("%d %d %d %d",n,n+1,n+2,n+3);
    // Selection sort
    int i, j;
    for (i = 0; i < 3; i++)
    {
        int min = i;
        for (j=i+1;j<4;j++) if (*(n+min)>*(n+j)) min=j;
        if (i!=min) swap(n+i,n+min);
    }
    printf("%d \n", *n**(n+2));
    free(n);
    return 0;
}