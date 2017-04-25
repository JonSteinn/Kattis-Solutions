#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N0 "**** ** ** ****"
#define N1 "  *  *  *  *  *"
#define N2 "***  *****  ***"
#define N3 "***  ****  ****"
#define N4 "* ** ****  *  *"
#define N5 "****  ***  ****"
#define N6 "****  **** ****"
#define N7 "***  *  *  *  *"
#define N8 "**** ***** ****"
#define N9 "**** ****  ****"

int main()
{
    char first_line[33];
    size_t n = 0;
    int skip = 0;
    for (size_t i = 0; i < 33; i++)
    {
        scanf("%c", &first_line[i]);
        if (first_line[i] == '\n')
        {
            first_line[i + 1] = '\0';
            break;
        }
        if (!skip)
        {
            n++;
            if (n % 3 == 0) skip = 1;
        }
        else
        {
            skip = 0;
        }
    }
    n /= 3;

    int first_index = 0;
    char numbers[n][16];
    for (int height = 0; height < 5; height++)
    {
        int letter = 0, offset = 0;
        char c;
        while(1)
        {
            if (height)
            {
                if (scanf("%c", &c) == EOF) break;
            }
            else
            {
                c = first_line[first_index++];
            }
            if (c == '\n') break;

            if (offset == 3)
            {
                letter++;
                offset = 0;
            }
            else
            {
                numbers[letter][height * 3 + offset] = c;
                offset++;
            }
        }
    }
    for (int i = 0; i < n; i++) numbers[i][15] = '\0';


    char number_string[9];
    int max_index = 0;
    int legit = 1;
    for (int i = 0; i < n; i++)
    {
        max_index = i;
        if (!strncmp(numbers[i], N0, 15))
        {
            number_string[i] = '0';
            continue;
        }
        if (!strncmp(numbers[i], N1, 15))
        {
            number_string[i] = '1';
            continue;
        }
        if (!strncmp(numbers[i], N2, 15))
        {
            number_string[i] = '2';
            continue;
        }
        if (!strncmp(numbers[i], N3, 15))
        {
            number_string[i] = '3';
            continue;
        }
        if (!strncmp(numbers[i], N4, 15))
        {
            number_string[i] = '4';
            continue;
        }
        if (!strncmp(numbers[i], N5, 15))
        {
            number_string[i] = '5';
            continue;
        }
        if (!strncmp(numbers[i], N6, 15))
        {
            number_string[i] = '6';
            continue;
        }
        if (!strncmp(numbers[i], N7, 15))
        {
            number_string[i] = '7';
            continue;
        }
        if (!strncmp(numbers[i], N8, 15))
        {
            number_string[i] = '8';
            continue;
        }
        if (!strncmp(numbers[i], N9, 15))
        {
            number_string[i] = '9';
            continue;
        }

        legit = 0;
        break;
    }
    if (legit)
    {
        number_string[max_index + 1] = '\0';
        printf(atoi(number_string) % 6 == 0 ? "BEER!!\n" : "BOOM!!\n");
    }
    else
    {
        printf("BOOM!!\n");
    }
    return 0;
}