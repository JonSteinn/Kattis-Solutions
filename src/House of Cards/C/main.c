#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// 1. For height n, there are f(n) = n*(3*n+1)/2 cards in the pyramid.
// 2. The sequence {f(n) mod 8, n >= 0} is [0, 2, 3, 3, 2, 0, 1, 1] repeated.
// n % 8 == 0 if last 3 digits of n is divisible by 8
// n % 8 == 5 if binary(n) ends with 101

void increment(char* str, size_t len)
{
    size_t index = len - 1;
    while(str[index] == '9') str[index--] = '0';
    str[index] = str[index] == 'X' ? '1' : (char)(str[index] + 1);
}

int ends_with_101(char* str, size_t len)
{
    int n = atoi(str + len - 3);
    if (!((n%2)&1)) return 0;
    n >>= 1;
    if ((n%2)&1) return 0;
    n >>= 1;
    return (n%2)&1;
}

void update_buffer(char* str, size_t l)
{
    while (atoi(str + (l - 3)) % 8 != 0 && !ends_with_101(str, l)) increment(str, l);
}

int numeric_find(int n)
{
    while(1)
    {
        int rem = n % 8;
        if (rem == 0 || rem == 5) return n;
        n++;
    }
}

int main()
{
    char buffer[10003];
    scanf("%s", buffer + 1);
    size_t len = strlen(buffer + 1);
    if (len < 10) printf("%d\n", numeric_find(atoi(buffer + 1)));
    else
    {
        buffer[0] = 'X';
        update_buffer(buffer, len + 1);
        printf("%s\n", buffer[0] == 'X' ? buffer + 1 : buffer);
    }
    return 0;
}
