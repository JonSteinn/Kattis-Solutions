#include <stdio.h>
#include <string.h>

#define LEGEND 0

struct game_status
{
    int rank;
    int stars;
    int consecutive;
};

int stars_cap(int rank)
{
    return rank > 20 ? 2 : rank > 15 ? 3 : rank > 10 ? 4 : 5;
}

void lose(struct game_status* s)
{
    s->consecutive = 0;
    if (s->rank > 20 || (s->rank == 20 && s->stars == 0)) return;
    if (s->stars == 0)
    {
        s->rank++;
        s->stars = stars_cap(s->rank) - 1;
    }
    else
    {
        s->stars--;
    }
}

void win(struct game_status* s)
{
    s->consecutive++;
    s->stars += (1 + ((s->rank > 5 && s->consecutive >= 3) ? 1 : 0));
    int cap = 0;
    while (s->rank != 0 && s->stars > (cap = stars_cap(s->rank)))
    {
        s->stars -= cap;
        s->rank--;
    }
}

void update(struct game_status* s, char result)
{
    if (s->rank > 0)
    {
        if (result == 'W') win(s);
        else lose(s);
    }
}

void init(struct game_status* status)
{
    status->rank = 25;
    status->stars = 0;
    status->consecutive = 0;
}

int game(char* seq, size_t len)
{
    struct game_status status;
    init(&status);
    for (int i = 0; i < len; i++)
    {
        update(&status, seq[i]);
        if (status.rank == LEGEND) break;
    }
    return status.rank;
}

int main()
{
    char buffer[10001];
    scanf("%s", buffer);
    int rank = game(buffer, strlen(buffer));
    if (rank == LEGEND) printf("Legend\n");
    else printf("%d\n", rank);
    return 0;
}