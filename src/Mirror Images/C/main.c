#include <stdio.h>

void char_swap(char* a, char *b)
{
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

void reverse(char* arr, int lo, int hi)
{
    while (lo < hi)
    {
        char_swap(arr+lo,arr+hi);
        hi--;
        lo++;
    }
}

void experiment(int x) 
{
    int r, c, i;
    scanf("%d %d", &r, &c);
    char arr[r][c+1];
    for (i = 0; i < r; i++) scanf("%s", arr[i]);
    printf("Test %d\n", x);
    for (i = r-1; i >= 0; i--)
    {
        reverse(arr[i], 0, c-1);
        printf("%s\n", arr[i]);
    }

}

int main()
{
    int n;
    scanf("%d",&n);
    int i;
    for (i = 1; i <= n; i++) experiment(i);
    return 0;
}