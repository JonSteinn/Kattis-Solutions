#include <stdio.h>

struct time
{
    int h, m, s;
};

void seconds_to_clock(int seconds)
{
    int hours = seconds / 3600;
    seconds -= hours * 3600;
    int minutes = seconds / 60;
    seconds -= minutes * 60;

    printf(hours < 10 ? "0%d:" : "%d:", hours);
    printf(minutes < 10 ? "0%d:" : "%d:", minutes);
    printf(seconds < 10 ? "0%d\n" : "%d\n", seconds);
}

int seconds_between(struct time* t1, struct time* t2)
{
    return (t2->h - t1->h) * 3600 + (t2->m - t1->m) * 60 + t2->s - t1->s;
}

int seconds(struct time* t)
{
    return t->h * 3600 + t->m * 60 + t->s;
}

int main()
{
    struct time first, second;
    scanf("%d:%d:%d", &first.h, &first.m, &first.s);
    scanf("%d:%d:%d", &second.h, &second.m, &second.s);

    if (first.h > second.h)
    {
        struct time midnight;
        midnight.h = 24;
        midnight.m = 0;
        midnight.s = 0;

        seconds_to_clock(seconds_between(&first, &midnight) + seconds(&second));
    }
    else if (first.h == second.h && first.m == second.m && first.s == second.s)
    {
        printf("24:00:00\n");
    }
    else
    {
        seconds_to_clock(seconds_between(&first, &second));
    }

    return 0;
}