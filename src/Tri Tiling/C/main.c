#include <stdio.h>
#include <stdlib.h>

int fills(int n, int* array)
{
    if (!array[n]) array[n] = (fills(n-1, array) << 2) - fills(n-2, array);
    return array[n];
}

int main()
{
    int* array = (int*)calloc(16, sizeof(int));
    array[0] = 1;
    array[1] = 1;
    int n;
    while (1)
    {
        scanf("%d", &n);
        if (n < 0) break;
        else if (n & 1) printf("0\n");
        else printf("%d\n", fills((n >> 1) + 1, array));
    }
    free(array);
    return 0;
}
