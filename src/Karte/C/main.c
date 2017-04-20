#include <stdio.h>
#include <stdlib.h>

int analyze(short* sets, short* counts)
{
    char buffer[1001];
    scanf("%s", buffer);

    int i;
    for (i = 0; i < 1001; i+=3)
    {
        if (buffer[i] == '\0') break;
        int bit = 1 << (buffer[i+1] == '0' ? (buffer[i+2] - '0') : (10 + buffer[i+2] - '0'));
        if (buffer[i] == 'P')
        {   
            if (!(*sets & bit))
            {
                (*counts)++;
                *sets |= bit;
            }
            else
            {
                return 0;
            }
        }

        if (buffer[i] == 'K')
        {
            if (!(*(sets+1) & bit))
            {
                (*(counts+1))++;
                *(sets+1) |= bit;
            }
            else
            {
                return 0;               
            }
        }

        if (buffer[i] == 'H')
        {
            if (!(*(sets+2) & bit))
            {
                (*(counts+2))++;
                *(sets+2) |= bit;
            }
            else
            {
                return 0;
            }
        }

        if (buffer[i] == 'T')
        {
            if (!(*(sets+3) & bit))
            {
                (*(counts+3))++;
                *(sets+3) |= bit;
            }
            else
            {
                return 0;               
            }
        }
    }
    return 1;
}

int main()
{
    short* sets = (short*)calloc(4,16);
    short* counts = (short*)calloc(4,16);
    if (analyze(sets, counts)) printf("%d %d %d %d\n",13-*counts,13-*(counts+1),13-*(counts+2),13-*(counts+3));
    else printf("GRESKA\n");
    free(sets);
    free(counts);
    return 0;
}