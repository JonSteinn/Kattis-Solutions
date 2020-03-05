#include <stdio.h>

int array_pos(char rank) {
    if (rank == 'A') return 0;
    if (rank == 'T') return 9;
    if (rank == 'J') return 10;
    if (rank == 'Q') return 11;
    if (rank == 'K') return 12;
    return (int)(rank - '1');
}

int main() {
    int counter[13] = {0,0,0,0,0,0,0,0,0,0,0,0,0};
    int curr_max = 0;
    for (int i = 0; i < 5; i++) {
        char card[3];
        scanf("%s", card);
        int rank = array_pos(card[0]);
        counter[rank] += 1;
        if (counter[rank] > curr_max) curr_max = counter[rank];
    }
    printf("%d\n", curr_max);
    return 0;
}