#include <stdio.h>

int root(int *arr, int x) {
    if (arr[x] < 0) return x;
    arr[x] = root(arr, arr[x]);
    return arr[x];
}

void connect(int* arr, int a, int b) {
    int ra = root(arr, a), rb = root(arr, b);
    if (ra - rb) {
        if (arr[ra] > arr[rb]) ra ^= rb ^= ra ^= rb;
        arr[ra] += arr[rb];
        arr[rb] = ra;
    }
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int uf[1000000] = {[0 ... 999999] = -1};
    for (int i = 0; i < k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        connect(uf, a-1, b-1);
    }

    int cap = n>>1, valid = 1;
    for (int i = 0; i < cap; i++) {
        if (root(uf, i) != root(uf, n-1-i)) {
            valid = 0;
            break;
        }
    }
    printf(valid ? "Yes\n" : "No\n");

    return 0;
}