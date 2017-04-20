#include <stdio.h>

#define TIME_LIMIT 210

int main()
{
    int current, questions, total_time = 0, explode = -1;
    scanf("%d", &current);
    scanf("%d", &questions);
    while (questions-- > 0)
    {
        int time;
        char result;
        scanf("%d %c", &time, &result);
        total_time += time;
        if (total_time >= TIME_LIMIT && explode < 0) explode = current;
        if (result == 'T') current = current == 8 ? 1 : current + 1;
    }
    printf("%d\n", explode);
}