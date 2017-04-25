#include <stdio.h>
#include <string.h>

void swap(char* a, char* b)
{
    if (a != b)
    {
        *a ^= *b;
        *b ^= *a;
        *a ^= *b;
    }
}

int perm(char* str, size_t len)
{
    size_t i = len - 1;
    while (i > 0 && str[i-1] >= str[i]) i--;
    if (i <= 0) return 0;
    size_t j = len - 1;
    while (str[j] <= str[i-1]) j--;
    swap(str + (i - 1), str + j);
    j = len - 1;
    while (i < j) swap(str + i++, str + j--);
    return 1;
}

int main()
{
    char buffer[7];
    scanf("%s", buffer);
    printf("%s\n", perm(buffer, strlen(buffer)) ? buffer : "0");
    return 0;
}