#include <stdio.h>
#include <string.h>

#define U 'U'
#define D 'D'

struct counters
{
    int first;
    int second;
    int third;
};

struct status
{
    char first;
    char second;
    char third;
};

void third(char* status, int* counter, char pref)
{
    if (*status == U)
    {
        if (pref == D)
        {
            *counter += 1;
            *status = D;
        }
    }
    else
    {
        if (pref == U)
        {
            *counter += 1;
            *status = U;
        }
    }

}

void second(char* status, int* counter, char pref)
{
    if (*status == D)
    {
        if (pref == U) *counter += 2;
    }
    else
    {
        *counter += 1;
    }
    *status = D;
}

void first(char* status, int* counter, char pref)
{
    if (*status == U)
    {
        if (pref == D) *counter += 2;
    }
    else
    {
        *counter += 1;
    }
    *status = U;
}

void seat_adjustments(struct counters* c, char* seq, size_t len)
{
    struct status s;
    c->first = 0; c->second = 0; c->third = 0;
    s.first = seq[0]; s.second = seq[0]; s.third = seq[0];
    for (int i = 1; i < len; i++)
    {
        first(&s.first, &c->first, seq[i]);
        second(&s.second, &c->second, seq[i]);
        third(&s.third, &c->third, seq[i]);
    }
}


size_t read(char* buffer)
{
    scanf("%s", buffer);
    return strlen(buffer);
}

int main()
{
    char buffer[1001];
    size_t len = read(buffer);
    struct counters c;
    seat_adjustments(&c, buffer, len);
    printf("%d\n%d\n%d\n", c.first, c.second, c.third);
    return 0;
}