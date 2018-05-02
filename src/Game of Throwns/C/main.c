#include <stdio.h>
#include <stdlib.h>

int undo(int curr)
{
    int backtrack = 0;
    scanf("%d", &backtrack);
    while(backtrack--) curr--;
    return curr < 0 ? 0 : curr;
}

int throw(int amount, int* stack, int curr, int n)
{
    stack[curr + 1] = (stack[curr] + (10001 * n) + amount) % n;
    return curr + 1;
}

int game(int n, int k)
{
    int stack[k + 1];
    stack[0] = 0;
    int curr = 0;

    while(k--)
    {
        char str[7];
        scanf("%s", str);
        if (str[0] == 'u') curr = undo(curr);
        else curr = throw(atoi(str), stack, curr, n);
    }

    return stack[curr];
}

int main()
{
    int n = 0, k = 0;
    scanf("%d %d", &n, &k);
    printf("%d\n", game(n,k));
    return 0;
}