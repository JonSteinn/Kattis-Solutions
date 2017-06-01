#include <stdio.h>

void print(int* arr)
{
    printf("%d %d %d %d %d\n", *arr, *(arr + 1), *(arr + 2), *(arr + 3), *(arr + 4));
}

void swap(int* arr, int i, int j)
{
    *(arr + i)^=*(arr + j)^=*(arr + i)^=*(arr + j);
    print(arr);
}

int is_sorted(int* arr)
{
    return *arr == 1 && *(arr + 1) == 2 && *(arr + 2) == 3 && *(arr + 3) == 4 && *(arr + 4) == 5;
}

int main()
{
    int arr[5];
    scanf("%d %d %d %d %d", arr, arr+1, arr+2, arr+3, arr+4);
    while (!is_sorted(arr))
    {
        for (int i = 0; i < 4; i++)
        {
            if (*(arr + i) > *(arr + i + 1)) swap(arr, i, i + 1);
        }
    }
    return 0;
}