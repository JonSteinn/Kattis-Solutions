#include <stdio.h>
#include <string.h>

void third(char* str, size_t len)
{
    printf("#.%c.#", str[0]);
    for (int i = 1; i < len; i++)
    {
        switch (i % 3)
        {
            case 0:
                printf(".%c.#",str[i]);
                break;
            case 1:
                printf(i == len - 1 ? ".%c.#" : ".%c.*",str[i]);
                break;
            default:
                printf(".%c.*",str[i]);

        }
    }
    putchar('\n');
}

void second(size_t len)
{
    printf(".#.#.");
    for (int i = 1; i < len; i++) printf(i % 3 == 2 ? "*.*." : "#.#.");
    putchar('\n');
}

void first(size_t len)
{
    printf("..#..");
    for (int i = 1; i < len; i++) printf(i % 3 == 2 ? ".*.." : ".#..");
    putchar('\n');
}

void decorate(char* str, size_t len)
{
    first(len);
    second(len);
    third(str, len);
    second(len);
    first(len);
}

int main()
{
    char buffer[16];
    scanf("%s",buffer);
    decorate(buffer, strlen(buffer));
    return 0;
}