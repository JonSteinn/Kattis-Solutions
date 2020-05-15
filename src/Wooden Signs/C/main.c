#include <stdio.h>
#include <stdlib.h>

#define MAX_PERM 2001

typedef unsigned long long ull;

typedef struct {
    int MOD;
    int n;
    int perm[MAX_PERM];
    ull *memory;
} RecData;

ull count(int a, int b, int i, RecData *data) {
    int x = data->perm[i];
    
    if (i == data->n) {
        return a < x && x < b ? 2 : 1;
    }

    ull total = 0;
    if (x > a) {
        if (!(data->memory+MAX_PERM*a)[i]) (data->memory+MAX_PERM*a)[i] = count(a, x, i+1, data);
        total += (data->memory+MAX_PERM*a)[i];
    }
    if (x < b) {
        if (!(data->memory+MAX_PERM*b)[i]) (data->memory+MAX_PERM*b)[i] = count(x, b, i+1, data);
        total += (data->memory+MAX_PERM*b)[i];
    }

    return total % data->MOD;
}

void init_rec_data(RecData *data, int *a, int *b) {
    data->MOD = 2147483647;
    data->memory = (ull*)calloc(MAX_PERM*MAX_PERM, sizeof(ull));
    scanf("%d",&data->n);
    scanf("%d %d", a, b);
    data->n--;
    if (*a>*b) (*a)^=(*b)^=(*a)^=(*b);
    for (int i = 0; i < data->n; i++) scanf("%d", data->perm+i);
}

int main() {
    int a,b;
    RecData data;
    init_rec_data(&data,&a,&b);

    if (data.n == 0) {
        printf("1\n");
    } else {
        printf("%llu\n", count(a,b,0,&data));
    }
    
    return 0;
}