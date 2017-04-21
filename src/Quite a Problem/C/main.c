#include <stdio.h>

#define WORD_LENGTH 7

int check_letter(char c, int index)
{
    switch (index)
    {
        case 0:
            return c == 'p' || c == 'P';
        case 1:
            return c == 'r' || c == 'R';
        case 2:
            return c == 'o' || c == 'O';
        case 3:
            return c == 'b' || c == 'B';
        case 4:
            return c == 'l' || c == 'L';
        case 5:
            return c == 'e' || c == 'E';
        case 6:
            return c == 'm' || c == 'M';
        default:
            return 0;
    }
}

int read_line()
{
    char next;
    int index = 0, found = 0;
    while(1)
    {
        if (scanf("%c", &next) == EOF) return 0;
        if (next == '\n')
        {
            printf(found ? "yes\n" : "no\n");
            return 1;
        }
        if (!found)
        {
            if (check_letter(next, index++)) found = (index == WORD_LENGTH);
            else index = (next == 'p' || next == 'P');
        }
    }
}

int main()
{
    while(read_line()){};
    return 0;
}