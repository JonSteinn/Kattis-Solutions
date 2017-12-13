#include <stdio.h>

int main()
{
    char buffer[6];
    int limit = 0, events = 0, current = 0, next = 0, rejects = 0;
    scanf("%d %d", &limit, &events);
    while(events--)
    {
        scanf("%s %d", buffer, &next);
        if (buffer[0] == 'e')
        {
            if (current + next > limit) rejects++;
            else current += next;
        }
        else
        {
            current -= next;
        }
    }
    printf("%d\n", rejects);
    return 0;
}