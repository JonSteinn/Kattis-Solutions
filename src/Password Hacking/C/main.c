#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    double x = *((double*)b) - *((double*)a);
    return x < 0 ? -1 : x > 0 ? 1 : 0;
}

int main()
{
    int n = 0;
    scanf("%d", &n);
    char buffer[13];
    double arr[n];
    for (int i = 0; i < n; i++) scanf("%s %lf", buffer, arr + i);
    qsort((void*)arr, (size_t)n, sizeof(arr[0]), comparator);
    double expected = 0.0;
    for (int i = 0; i < n; i++) expected += arr[i] * (i+1);
    printf("%.6f\n", expected);
    return 0;
}