#include <stdio.h>
#include <string.h>

char get_oct(char a, char b, char c)
{
    return a == '0' ? (b == '0' ? (c == '0' ? '0' : '1') : (c == '0' ? '2' : '3'))
                    : (b == '0' ? (c == '0' ? '4' : '5') : (c == '0' ? '6' : '7'));
}

size_t start(size_t addition)
{
    return addition == 0 ? 2 : addition == 1 ? 0 : 1;
}

int main()
{
    char buffer[102];
    scanf("%s", buffer+2);
    buffer[0] = buffer[1] = '0';
    size_t len = strlen(buffer+2);
    size_t start_index = start(len % 3);
    len += 2;
    while (start_index < len)
    {
        printf("%c", get_oct(buffer[start_index], buffer[start_index + 1], buffer[start_index + 2]));
        start_index += 3;
    }
    printf("\n");
    return 0;
}