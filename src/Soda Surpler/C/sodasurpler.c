#include <stdio.h>

int main()
{
    int e, f, c;
    scanf("%d %d %d", &e, &f, &c);

    int sum = 0;
    e += f;
    while (e >= c)
    {
        int new_sodas = e / c, remaining_empty = e % c;
        sum += new_sodas;
        e = new_sodas + remaining_empty;
    }
    printf("%d\n", sum);
    return 0;
}