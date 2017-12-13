#include <stdio.h>
#include <string.h>

char rotate_by(char c, int x)
{
    return (char)('A' + (((c - 'A') + x) % 26));
}

int sum(char* str, size_t len)
{
    int _sum = 0;
    for (int i = 0; i < len; i++) _sum += str[i] - 'A';
    return _sum;
}

int main()
{
    char buffer[15001];
    scanf("%s", buffer);
    size_t len = strlen(buffer) >> 1;
    int a = sum(buffer, len), b = sum(buffer + len, len);
    for (int i = 0; i < len; i++)
    {
        buffer[i] = rotate_by(buffer[i], a);
        buffer[i + len] = rotate_by(buffer[i + len], b);
    }
    for (int i = 0; i < len; i++) buffer[i] = rotate_by(buffer[i], buffer[i + len] - 'A');
    buffer[len] = '\0';
    printf("%s\n", buffer);
    return 0;
}