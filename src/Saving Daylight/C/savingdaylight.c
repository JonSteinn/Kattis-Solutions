#include <stdio.h>
#include <stdlib.h>

struct clock_time
{
    int hours;
    int minutes;
};

void sun_time(struct clock_time* c1, struct clock_time* c2, struct clock_time* r)
{
    int minutes = (c2->hours - c1->hours) * 60 + c2->minutes - c1->minutes;
    r->hours = minutes / 60;
    r->minutes = minutes % 60;
}

int main()
{
    struct clock_time clock1, clock2;
    struct clock_time* results = (struct clock_time*)malloc(sizeof(struct clock_time));
    char month[10], day[3], year[5];
    while (scanf("%s %s %s %d:%d %d:%d", month, day, year, &clock1.hours, &clock1.minutes, &clock2.hours, &clock2.minutes) == 7)
    {
        sun_time(&clock1, &clock2, results);
        printf("%s %s %s %d hours %d minutes\n", month, day, year, results->hours, results->minutes);
    }
    free(results);
    return 0;
}