#include <stdio.h>
#include <stdlib.h>

#define STUDENT_COUNT 20

void read(int* array)
{
    int i;
    for (i = 0; i < STUDENT_COUNT; i++) scanf("%d", array + i);
}

int inversions(int* array)
{
    int count = 0;
    int i, j;
    for (i = 0; i < STUDENT_COUNT - 1; i++)
    {
        for (j = i + 1; j < STUDENT_COUNT; j++)
        {
            if (*(array + i) > *(array + j)) count++;
        }
    }
    return count;
}

int steps(int* array)
{
    read(array);
    return inversions(array);
}

int main()
{
    int n, line;
    scanf("%d", &n);
    int* array = (int*)malloc(STUDENT_COUNT * sizeof(int));
    while (n-- > 0)
    {
        scanf("%d", &line);
        printf("%d %d\n", line, steps(array));
    }
    free(array);
    return 0;
}