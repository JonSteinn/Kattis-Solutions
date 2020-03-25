#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int y,m,d,h,mi;
    int type;
} time;

int days_in_month[] = {31,28,31,30,31,30,31,31,30,31,30,31};

int comparator (const void * a, const void * b) {
    time t1 = *(time*)a, t2 = *(time*)b;
    if (t1.y != t2.y) return t1.y - t2.y;
    if (t1.m != t2.m) return t1.m - t2.m;
    if (t1.d != t2.d) return t1.d - t2.d;
    if (t1.h != t2.h) return t1.h - t2.h;
    if (t1.mi != t2.mi) return t1.mi - t2.mi;
    return t1.type - t2.type;
}

int rooms_needed(time* times, int size) {
    int c = 0, most = 0;
    for (int i = 0; i < size; i++) {
        c += times[i].type;
        if (c > most) most = c;
    }
    return most;
}

void next_day(time*t) {
    // New year
    if (t->d == 31 && t->m == 12) {
        t->y++;
        t->m = 1;
        t->d = 1;
        return;
    }

    // Leap year exception
    if (t->y == 2016 && t->m == 2 && t->d >= 28) {
        if (t->d == 28) {
            t->d = 29;
        } else {
            t->d = 1;
            t->m++;
        }
        return;
    }

    // End of month
    if (t->d == days_in_month[t->m -1]) {
        t->d = 1;
        t->m++;
        return;
    }

    // Any other day
    t->d++;
}

void add_cleaning(time* t, int c) {
    if (!c) return;

    t->mi += c;
    t->h += t->mi / 60;
    t->mi %= 60;

    if (t->h >= 24) {
        t->h %= 24;
        next_day(t);
    }
}

int main(void) {
    int t,b,c;
    char buffer[21];
    time times[10000];
    scanf("%d",&t);
    while(t--) {
        scanf("%d %d", &b, &c);
        b <<= 1;
        for (int i = 0; i < b; i += 2) {
            times[i].type = 1;
            times[i+1].type = -1;
            scanf("%s %d-%d-%d %d:%d %d-%d-%d %d:%d", buffer,
                &times[i].y,&times[i].m,&times[i].d,&times[i].h,&times[i].mi,
                &times[i+1].y,&times[i+1].m,&times[i+1].d,&times[i+1].h,&times[i+1].mi);
            add_cleaning(&times[i+1], c);
        }
        qsort(times, b, sizeof(time), comparator);
        printf("%d\n", rooms_needed(times, b));
    }
    return 0;
}