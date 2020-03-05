
#include <stdio.h>

#define ToChar(x) (char)(((26 + (x)) % 26)+'a')
#define ToNum(x) ((x)-'a')

int main() {
    int n,m;
    scanf("%d %d", &n, &m);

    char last[n+1], encrypted[m+1], plain[m+1];
    plain[m] = 0;
    scanf("%s", last);
    scanf("%s", encrypted);

    for (int i = 0; i < n; i++) plain[m-1-i] = last[n-1-i];
    for (int i = m-n-1; i >= 0; i--) plain[i] = ToChar(ToNum(encrypted[i+n])-ToNum(plain[n+i]));

    printf("%s\n", plain);
    return 0;
}