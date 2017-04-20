#include <stdio.h>
#include <stdlib.h>

#define LEGAL "pangram"
#define MISSING "missing "
#define ALPHABET_SIZE 26

int is_lower_case(char c)
{
    return c <= 'z' && 'z' - c < ALPHABET_SIZE;
}

int is_upper_case(char c)
{
    return c <= 'Z' && 'Z' - c < ALPHABET_SIZE;
}

char to_upper(char c)
{
    return (char)(c - 32);
}

char to_lower(char c)
{
    return (char)(c + 32);
}

int array_shift(char c)
{
    return c - 'A';
}

void process(char* alphabet)
{
    int i, is_legal = 1;
    for (i = 0; i < ALPHABET_SIZE; i++)
    {
        if (!*(alphabet + i))
        {
            if (is_legal) printf(MISSING);
            is_legal = 0;
            printf("%c", to_lower((char)('A' + i)));
        }
    }
    if (is_legal) printf(LEGAL);
    printf("\n");
}

void experiment()
{
    char* alphabet = (char*)calloc(ALPHABET_SIZE, sizeof(char));
    char c;
    while (1)
    {
        scanf("%c", &c);
        if (c == '\n' || c == '\0')
        {
            process(alphabet);
            break;
        }

        if (is_lower_case(c)) c = to_upper(c);
        if (is_upper_case(c)) *(alphabet + array_shift(c)) = 1;
    }
    free(alphabet);
}

int main()
{
    int n;
    scanf("%d\n", &n);
    while(n-- > 0) experiment();
    return 0;
}