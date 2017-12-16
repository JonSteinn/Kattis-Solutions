
#include <stdio.h>

int tetris1(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 3; i++)
    {
        if (arr[i+3] == arr[i+2])
        {
            if (arr[i+2] == arr[i+1])
            {
                if (arr[i+1] == arr[i]) counter++;
            }
            else
            {
                i += 1;
            }
        }
        else
        {
            i += 2;
        }
    }
    return counter + c;
}

int tetris2(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 1; i++)
    {
        if (arr[i] == arr[i+1]) counter++;
    }
    return counter;
}

int tetris3(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 2; i++)
    {
        if (arr[i] == arr[i + 1] && arr[i] == arr[i + 2] - 1) counter++;
        if (arr[i] == arr[i + 1] + 1) counter++;
    }
    if (arr[c - 2] == arr[c - 1] + 1) counter++;
    return counter;
}

int tetris4(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 2; i++)
    {
        if (arr[i] - 1 == arr[i + 1] && arr[i + 1] == arr[i + 2]) counter++;
        if (arr[i + 1] - 1 == arr[i]) counter++;
    }
    if (arr[c - 1] - 1 == arr[c - 2]) counter++;
    return counter;
}

int tetris5(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 2; i++)
    {
        if (arr[i] == arr[i + 1] && arr[i] == arr[i + 2]) counter++;
        if (arr[i] - 1 == arr[i + 1] && arr[i] == arr[i + 2]) counter++;
        if (arr[i] - 1 == arr[i + 1]) counter++;
        if (arr[i + 1] - 1 == arr[i]) counter++;
    }
    if (arr[c - 2] - 1 == arr[c - 1]) counter++;
    if (arr[c - 1] - 1 == arr[c - 2]) counter++;
    return counter;
}

int tetris6(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 2; i++)
    {
        if (arr[i] == arr[i + 1] && arr[i] == arr[i + 2]) counter++;
        if (arr[i] == arr[i + 1] - 1 && arr[i + 1] == arr[i + 2]) counter++;
        if (arr[i] - 2 == arr[i + 1]) counter++;
        if (arr[i] == arr[i + 1]) counter++;
    }
    if (arr[c - 2] - 2 == arr[c - 1]) counter++;
    if (arr[c - 2] == arr[c - 1]) counter++;
    return counter;
}

int tetris7(int c, int *arr)
{
    int counter = 0;
    for (int i = 0; i < c - 2; i++)
    {
        if (arr[i] == arr[i + 1] && arr[i] == arr[i + 2]) counter++;
        if (arr[i + 2] == arr[i + 1] - 1 && arr[i + 1] == arr[i]) counter++;
        if (arr[i + 1] - 2 == arr[i]) counter++;
        if (arr[i] == arr[i + 1]) counter++;
    }
    if (arr[c - 1] - 2 == arr[c - 2]) counter++;
    if (arr[c - 2] == arr[c - 1]) counter++;
    return counter;
}


int tetris(int c, int p, int* arr)
{
    return p == 1 ? 
               tetris1(c, arr) : 
               (p == 2 ? 
                    tetris2(c, arr) : 
                    (p == 3 ? 
                        tetris3(c, arr) : 
                        (p == 4 ? 
                            tetris4(c, arr) : 
                            (p == 5 ? 
                                tetris5(c, arr) : 
                                (p == 6 ? 
                                    tetris6(c, arr) : 
                                    tetris7(c, arr))))));
}

int main()
{
    int c = 0, p = 0;
    scanf("%d %d", &c, &p);
    int heights[c];
    for (int i = 0; i < c; i++) scanf("%d", heights + i);
    printf("%d\n", tetris(c, p, heights));
    return 0;
}