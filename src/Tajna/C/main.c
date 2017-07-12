#include <stdio.h>
#include <string.h>
#include <math.h>

int find_r(int n)
{
    for (int r = (int)(sqrt(n)+.1); r > 1; r--) {
        if (n % r == 0) return r;
    }
    return 1;
}

int main()
{
    char buffer[101];
    scanf("%s", buffer);
    int n = (int)strlen(buffer), r = find_r(n), c = n / r;

    char out[n + 1];
    out[n] = '\0';
    int index = 0;
    for (int _c = 0; _c < c; _c++) {
        for (int _r = 0; _r < r; _r++) {
            out[_r * c + _c] = buffer[index++];
        }
    }
    printf("%s\n", out);
    return 0;
}