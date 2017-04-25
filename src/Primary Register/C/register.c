#include <stdio.h>

int main()
{
    int mods[8] = {2, 3, 5, 7, 11, 13, 17, 19};
    int lesser_needed[8] = {1,2,1,1,1,1,1,1};
    for (int i = 2; i < 8; i++) for (int j = 0; j < i; j++) lesser_needed[i] *= mods[j];
    int values[8];
    scanf("%d %d %d %d %d %d %d %d", values, values+1, values+2, values+3, values+4, values+5, values+6, values+7);
    int sum = 0;
    for (int i = 0; i < 8; i++) sum += (mods[i] - 1 - values[i]) * lesser_needed[i];
    printf("%d\n", sum);
    return 0;
}