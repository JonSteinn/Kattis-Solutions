#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int* code = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int next;
            scanf("%d",&next);
            if (i == j) continue;
            code[i] |= next;
            code[j] |= next;
        }
    }
    for (int i = 0; i < n - 1; i++) printf("%d ", code[i]);
    printf("%d\n", code[n-1]);
    return 0;
}