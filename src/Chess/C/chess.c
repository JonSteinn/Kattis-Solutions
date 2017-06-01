#include <stdio.h>

typedef struct position pos;

struct position {
    char file; // column
    int rank;  // row
};

int abs(int x)
{
    return x < 0 ? -x : x;
}

int xor(int p, int q)
{
    return (p || q) && !(p && q);
}

int diagonals(pos* p1, pos* p2)
{
    return abs(p1->file - p2->file) == abs(p1->rank - p2->rank);
}

int black(pos* p)
{
    return ((p->file - 'A') + p->rank) % 2;
}

int nw(pos* from, pos* to, pos* mid, int steps)
{
    mid->rank = from->rank;
    mid->file = from->file;
    while(steps--)
    {
        mid->file = (char)(mid->file + 1);
        mid->rank++;
        if (diagonals(mid, to)) {
            return 1;
        }
    }
    return 0;
}

int ne(pos* from, pos* to, pos* mid, int steps)
{
    mid->rank = from->rank;
    mid->file = from->file;
    while(steps--)
    {
        mid->file = (char)(mid->file - 1);
        mid->rank++;
        if (diagonals(mid, to)) return 1;
    }
    return 0;
}

int sw(pos* from, pos* to, pos* mid, int steps)
{
    mid->rank = from->rank;
    mid->file = from->file;
    while(steps--)
    {
        mid->file = (char)(mid->file + 1);
        mid->rank--;
        if (diagonals(mid, to)) return 1;
    }
    return 0;
}

void se(pos* from, pos* to, pos* mid, int steps)
{
    mid->rank = from->rank;
    mid->file = from->file;
    while(steps--)
    {
        mid->file = (char)(mid->file - 1);
        mid->rank--;
        if (diagonals(mid, to)) return;
    }
}

void step(pos* from, pos* to, pos* mid)
{
    int left = (from->file - 'A');
    int right = 7 - (from->file - 'A');
    int down = from->rank - 1;
    int up = 8 - from->rank;
    if (!nw(from, to, mid, right < up ? right : up))
    {
        if (!ne(from, to, mid, left < up ? left : up))
        {
            if (!sw(from, to, mid, right < down ? right : down))
            {
                se(from, to, mid, left < down ? left : down);
            }
        }
    }
}

void move(pos* from, pos* to)
{
    if (xor(black(from), black(to))) printf("Impossible\n");
    else if (from->file == to->file && from->rank == to->rank) printf("0 %c %d\n", from->file, from->rank);
    else if (diagonals(from, to)) printf("1 %c %d %c %d\n", from->file, from->rank, to->file, to->rank);
    else
    {
        pos mid;
        step(from, to, &mid);
        printf("2 %c %d %c %d %c %d\n", from->file, from->rank, mid.file, mid.rank, to->file, to->rank);
    }
}

void test_case()
{
    pos from, to;
    char b1[2], b2[2]; // lazy avoidance of single-char input formatting...
    scanf("%s %d %s %d", b1, &from.rank, b2, &to.rank);
    from.file = b1[0];
    to.file = b2[0];
    move(&from, &to);
}

int main()
{
    int n;
    scanf("%d", &n);
    while(n--) test_case();
    return 0;
}