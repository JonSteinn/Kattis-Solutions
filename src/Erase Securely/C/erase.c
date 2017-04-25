#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int flips;
    scanf("%d", &flips);

    char buffer[1001];
    scanf("%s", buffer);
    size_t len = strlen(buffer);

    size_t padding = 32 - len%32;
    if (padding == 32)
    {
        size_t arr_size = len/32;
        int* number = (int*)calloc(arr_size, sizeof(int));
        for (size_t i = 0; i < arr_size; i++)
        {
            for (int j = 0; j < 32; j++)
            {
                if (buffer[i * 32 + j] == '1') *(number+i) |= (1 << j);
            }
            if (flips & 1) *(number+i) = ~*(number+i);
        }
        int successful = 1;
        scanf("%s", buffer);
        int* second = (int*)calloc(arr_size, sizeof(int));
        for (size_t i = 0; i < arr_size; i++)
        {
            for (int j = 0; j < 32; j++)
            {
                if (buffer[i * 32 + j] == '1') *(second+i) |= (1 << j);
            }
            if (*(second + i) != *(number + i))
            {
                successful = 0;
                break;
            }
        }
        printf(successful ? "Deletion succeeded\n" : "Deletion failed\n");
    }
    else
    {
        size_t arr_size = len/32 + 1;
        int* number = (int*)calloc(arr_size, sizeof(int));
        for (size_t i = 0; i < arr_size; i++)
        {
            if (i == arr_size - 1)
            {
                for (int j = 0; j < 32 - padding; j++)
                {
                    if (buffer[i * 32 + j] == '1') *(number + i) |= (1 << j);
                }
            }
            else
            {
                for (int j = 0; j < 32; j++)
                {
                    if (buffer[i * 32 + j] == '1') *(number + i) |= (1 << j);
                }
            }
            if (flips & 1) *(number + i) = ~*(number + i);
        }
        int successful = 1;
        scanf("%s", buffer);
        int* second = (int*)calloc(arr_size, sizeof(int));
        for (size_t i = 0; i < arr_size; i++)
        {
            if (i == arr_size - 1)
            {
                for (int j = 0; j < 32 - padding; j++)
                {
                    if (buffer[i * 32 + j] == '1') *(second + i) |= (1 << j);
                }
                if (flips & 1)
                {
                    for (size_t j = 32 - padding; j < 32; j++)
                    {
                        *(second + i) |= (1 << j);
                    }
                }
            }
            else
            {
                for (int j = 0; j < 32; j++)
                {
                    if (buffer[i * 32 + j] == '1') *(second+i) |= (1 << j);
                }
            }
            if (*(second + i) != *(number + i))
            {
                successful = 0;
                break;
            }
        }
        printf(successful ? "Deletion succeeded\n" : "Deletion failed\n");
    }

    return 0;
}