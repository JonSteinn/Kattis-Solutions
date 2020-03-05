#include <stdio.h>
#include <math.h>

void best(int s) {
    if (s >= 8) {
        printf("Province or Gold\n");
    } else if (s >= 6) {
        printf("Duchy or Gold\n");
    } else if (s >= 5) {
        printf("Duchy or Silver\n");
    } else if (s >= 3) {
        printf("Estate or Silver\n");
    } else if (s >= 2) {
        printf("Estate or Copper\n");
    } else {
        printf("Copper\n");
    }
}

int main() {
    int g,s,c;
    scanf("%d %d %d", &g, &s, &c);
    best(3*g+2*s+c);
    return 0;
}