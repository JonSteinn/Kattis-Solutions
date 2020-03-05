#include <stdio.h>

int cap(int* j, int* r) {
    // Will 0 finish before 1?
    if (j[0]/(double)j[1] < r[0]/(double)r[1]) {
        // Will 0 finish before 2?
        return j[0]/(double)j[2] < r[0]/(double)r[2] ? 0 : 2;
    } else {
        // Will 1 finish before 2?
        return j[1]/(double)j[2] < r[1]/(double)r[2] ? 1 : 2;
    }
}

int print(int* j, int* r, int index) {
    for (int i = 0; i < 3; i++) {
        if (i == index) {
            printf("%.4f", 0.0f);
        } else {
            printf("%.4f", j[i]-j[index]*(r[i]/(double)r[index]));
        }
        putchar(i == 2 ? '\n': ' ');
    }
}

int main() {
    int j[3], r[3];
    scanf("%d %d %d", j, j+1, j+2);
    scanf("%d %d %d", r, r+1, r+2);
    print(j, r, cap(j,r));
    return 0;
