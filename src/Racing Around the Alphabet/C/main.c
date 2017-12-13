#include <stdio.h>

#define STEP_LENGTH 6.731984257692413

int to_int(char x)
{
    return x == ' ' ? 26 : x == '\'' ? 27 : x - 'A';
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int shortest_route(char a, char b)
{
    if (a == b) return 0;
    int _a = to_int(a), _b = to_int(b);
    if (_b < _a)
    {
        _a ^= _b;
        _b ^= _a;
        _a ^= _b;
    }
    return min(_b - _a, (28 - _b) + _a);
}

int run(char* str, int len)
{
    len--;
    int counter = 0;
    for (int i = 0; i < len; i++) counter += shortest_route(str[i], str[i+1]);
    return counter;
}

int read_line(char* buffer)
{
    char c = 0;
    int counter = 0;
    while(1)
    {
        scanf("%c", &c);
        if (c == '\n') break;
        buffer[counter++] = c;
    }
    return counter;
}

int main()
{
    char buffer[121];
    int n = 0;
    scanf("%d\n",&n);
    while(n--)
    {
        int len = read_line(buffer);
        printf("%.8f\n", run(buffer, len) * STEP_LENGTH / 15 + len);
    }
    return 0;
}