#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void reverse(char* str, int lo, int hi)
{
    while (lo < hi)
    {
        if (str[lo] - str[hi]) str[lo] ^= str[hi] ^= str[lo] ^= str[hi];
        lo++;
        hi--;
    }
}

void split_reverse(char* str, int start2, int start3, int len)
{
    reverse(str, 0, start2 - 1);
    reverse(str, start2, start3 - 1);
    reverse(str, start3, len - 1);
}


int main()
{
    char buffer[51];
    scanf("%s",buffer);
    size_t len = strlen(buffer);

    // positive infinity for a-z strings of length len
    char inf[len+1];
    for (int i = 0; i < len; i++) inf[0] = 'z';
    inf[len] = '\0';

	// len+1 for chars, binom(len-1,2) for number of different splits
    char* mem = (char*)malloc(sizeof(char) * (len*len-1) * (len-2));
    char* curr = mem;
    char* least = inf;

    for (int i = 1; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            strcpy(curr, buffer);
            split_reverse(curr, i, j, (int)len);
            if (strncmp(least, curr, len) > 0) least = curr;
            curr += (len+1);
        }
    }

    printf("%s\n", least);

    free(mem);
    
    return 0;
}