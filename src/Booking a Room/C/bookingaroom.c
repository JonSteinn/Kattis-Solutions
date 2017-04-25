#include <stdio.h>
#include <stdlib.h>

int main()
{
    int r, n;
    scanf("%d %d", &r, &n);
    int* rooms = (int*)calloc(100, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        int room;
        scanf("%d", &room);
        *(rooms + (room-1)) = 1;
    }
    int late = 1;
    for (int i = 0; i < r; i++)
    {
        if (!*(rooms + i))
        {
            printf("%d\n", i + 1);
            late = 0;
            break;
        }
    }
    if (late) printf("too late\n");
}