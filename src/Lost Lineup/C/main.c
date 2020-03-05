#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    arr[0] = 1;
    for (int i = 1; i < n; i++) {
        int next;
        scanf("%d", &next);
        arr[next+1] = i + 1;
    }

    putchar('1');
    for (int i = 1; i < n; i++) printf(" %d", arr[i]);
    putchar('\n');

    return 0;
}