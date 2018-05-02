#include <stdio.h>

int main()
{
    int n = 0, count = 0;
    scanf("%d", &n);
    int arr[n];
    while(n--)
    {
        int next = 0;
        scanf("%d", &next);

        if (count == 0 || arr[count - 1] < next) arr[count++] = next;
    }
    printf("%d\n%d", count, arr[0]);
    for (int i = 1; i < count; i++) printf(" %d", arr[i]);
    putchar('\n');
    return 0;
}