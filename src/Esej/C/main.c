#include <stdio.h>

void print(int word_number, char* letters, int space)
{
    if (word_number == 0) {
        printf("a");
    }
    else
    {
        while (word_number)
        {
            int mod = word_number % 15;
            word_number /= 15;
            printf("%c", letters[mod]);
        }
    }
    if (space) printf(" ");
}

int main()
{
    char letters[15];
    for (int i = 0; i < 15; i++) letters[i] = (char)('a' + i);
    int n,k;
    scanf("%d %d",&n,&k);
    k >>= 1;
    int upper = n < k ? k : n;
    for (int i = 0; i < upper - 1; i++) print(i, letters, 1);
    print(upper-1, letters, 0);
    printf("\n");
    return 0;
}