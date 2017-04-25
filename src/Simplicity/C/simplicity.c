#include <stdio.h>
#include <stdlib.h>

int main()
{
    int* arr = (int*)calloc(26, sizeof(int));
    char c;
    while (scanf("%c", &c) != EOF && c != '\n') arr[c - 'a']++;
    int large1 = 0, large2 = 0, sum = 0;
    for (int i = 0; i < 26; i++)
    {
        if (arr[i] > large2)
        {
            large2 = arr[i];
            if (large2 > large1)
            {
                large1^=large2;
                large2^=large1;
                large1^=large2;
            }
        }
        sum += arr[i];
    }
    printf("%d\n", sum - large1 - large2);
    return 0;
}