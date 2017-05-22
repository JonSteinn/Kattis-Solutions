#include <stdio.h>
#include <string.h>

#define INT_MAP(x) (x-'a')

int main()
{
    char letters[26];
    memset(letters, 0, 26);
    char c;
    while (scanf("%c", &c) != EOF && c != '\n') letters[INT_MAP(c)]++;
    int odds = 0;
    for (int i = 0; i < 26; i++) odds += letters[i] & 1;
    printf("%d\n", odds > 1 ? odds-1 : 0);
    return 0;
}