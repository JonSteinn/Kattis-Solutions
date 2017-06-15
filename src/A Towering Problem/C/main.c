#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return (*(int*)b - *(int*)a);
}

void find_towers(int* arr, int h1, int h2)
{
    // O(n^3) is fine for n = 6
    int found = 0;
    int indices[6];
    for (int i = 0; i < 6; i++)
    {
        for (int j = i + 1; j < 6; j++)
        {
            for (int k = j + 1; k < 6; k++)
            {
                if (arr[i] + arr[j] + arr[k] == h1)
                {
                    found++;
                    indices[0] = i;
                    indices[1] = j;
                    indices[2] = k;
                }
                else if (arr[i] + arr[j] + arr[k] == h2)
                {
                    found++;
                    indices[3] = i;
                    indices[4] = j;
                    indices[5] = k;
                }
                if (found == 2)
                {
                    printf("%d %d %d %d %d %d\n",
                           arr[indices[0]], arr[indices[1]], arr[indices[2]],
                           arr[indices[3]], arr[indices[4]], arr[indices[5]]);
                    return;
                }
            }
        }
    }
}

int main()
{
    int arr[6];
    for (int i = 0; i < 6; i++) scanf("%d", arr+i);
    int h1, h2;
    scanf("%d %d", &h1, &h2);
    qsort(arr, 6, sizeof(int), comparator);
    find_towers(arr, h1, h2);
    return 0;
}