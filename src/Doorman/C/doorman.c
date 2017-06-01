#include <stdio.h>
#include <string.h>

#define INDEX(x) ((x) != 'M')
#define ABS(x) ((x) < 0 ? -(x) : (x))


int people_in(char* str, size_t size, int max)
{
    char waiting = 0;
    int index = 0;
    int counts[2] = {0,0};

    while(1)
    {
        if (index >= size)
        {
            if (waiting != 0 && ABS(counts[INDEX(waiting)] + 1 - counts[!INDEX(waiting)]) <= max) counts[INDEX(waiting)]++;
            break;
        }
        char next = str[index++];
        if (ABS(counts[INDEX(next)] + 1 - counts[!INDEX(next)]) <= max) {
            counts[INDEX(next)]++;
        } else if(waiting == 0) {
            waiting = next;
        } else if (ABS(counts[INDEX(waiting)] + 1 - counts[!INDEX(waiting)]) <= max) {
            counts[INDEX(waiting)]++;
            index--;
        } else {
            break;
        }
    }

    return counts[0] + counts[1];
}

int main()
{
    int max;
    scanf("%d", &max);
    char buffer[101];
    scanf("%s", buffer);
    printf("%d\n", people_in(buffer, strlen(buffer), max));
    return 0;
}