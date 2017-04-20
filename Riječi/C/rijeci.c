#include "stdio.h"
#include "stdlib.h"

unsigned long long fibonacci(int n, unsigned long long* arr)
{
    if (n == 0) return arr[0];
    if (!arr[n]) arr[n] = fibonacci(n - 1, arr) + fibonacci(n -2, arr);
    return arr[n];
}

int main()
{
    unsigned long long* arr = (unsigned long long*)calloc(46, sizeof(unsigned long long));
    arr[0] = 0L;
    arr[1] = 1L;

    int n;
    scanf("%d", &n);
    printf("%llu %llu\n", fibonacci(n - 1, arr), fibonacci(n, arr));

    free(arr);
    return 0;
}