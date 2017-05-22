#include <stdio.h>

char next(char c)
{
    return c == 'G' ? 'A' : (char)(c+1);
}

char prev(char c)
{
    return c == 'A' ? 'G' : (char)(c-1);
}

int main()
{
    char note[3], tonality[6];
    int case_number = 1;
    while (scanf("%s %s", note, tonality) == 2)
    {
        printf("Case %d: ", case_number++);
        if (note[1] == '#')
        {
            printf("%cb %s\n", next(note[0]), tonality);
        }
        else if (note[1] == 'b')
        {
            printf("%c# %s\n", prev(note[0]), tonality);
        }
        else
        {
            printf("UNIQUE\n");
        }
    }
    return 0;
}