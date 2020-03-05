#include <stdio.h>
#include <stdlib.h>

int tenten(char* game, int index) {
    int p[2] = {10,10};
    for (int i = index; game[i] && abs(p[0]-p[1]) < 2; i += 2) {
        p[game[i] - 'A'] += (int)(game[i+1] - '0');
    }
    printf(p[0] > p[1] ? "A\n" : "B\n");
}

int main() {
    int p[2] = {0,0};
    char game[201];
    scanf("%s", game);
    for (int i = 0; game[i]; i += 2) {
        p[game[i] - 'A'] += (int)(game[i+1] - '0');
        if (p[0] == 10 && p[1] == 10) {
            tenten(game, i+2);
            break;
        }
        if (p[0] > 10) {
            printf("A\n");
            break;
        }
        if (p[1] > 10) {
            printf("B\n");
            break;
        }
    }
    return 0;
}