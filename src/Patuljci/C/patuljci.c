#include <stdio.h>

void find_two_excessive(int* arr, int sum)
{
    for (int i = 1; i < 9; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (sum - arr[i] - arr[j] == 100)
            {
                for (int k = 0; k < 9; k++)
                {
                    if (k != i && k != j) printf("%d\n", arr[k]);
                }
                return;
            }
        }
    }
}

int main()
{
    int sum = 0;
    int arr[9];
    for (int i = 0; i < 9; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    find_two_excessive(arr, sum);
    return 0;
}