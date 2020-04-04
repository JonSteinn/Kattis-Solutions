#include <stdio.h>
#include <stdlib.h>

int* primes_less_than_500(int* n) {
    *n = 0;
    int prime[500] = {[0 ... 499] = 1};
    for (int i = 2; i < 500; i++) {
        if (prime[i]) {
            (*n)++;
            for (int j=i*i; j<500; j += i) prime[j] = 0;
        }
    }
    int* arr = (int*)malloc(sizeof(int)*(*n));
    int next = 0;
    for (int i = 2; i < 500; i++) {
        if (prime[i]) arr[next++] = i;
    }
    return arr;
}

int least_not_smaller(int arr[], int size, int x) {
    int l = 0, r = size - 1;
    while (l <= r) { 
        int m = l + (r - l) / 2;
        if (arr[m] == x) return m;
        if (arr[m] < x) l = m + 1;
        else r = m - 1;
    } 
    return l;
} 

int root(int* p, int a) {
    while (p[a] >= 0) a = p[a];
    return a;
}

void connect(int* p, int rA, int rB) {
    if (p[rA] > p[rB]) rA ^= rB ^= rA ^= rB;
    p[rA] += p[rB];
    p[rB] = rA;
}

int sets(int a, int b, int p, int* arr, int* primes, int prime_cnt) {
    int s = b-a+1;
    int top = s;
    for (int i = least_not_smaller(primes, prime_cnt, p); i < prime_cnt; i++) {
        int prime = primes[i];
        if (prime > top) break;
        
        int first_found = -1;
        for (int j = a; j <= b; j++) {
            if (j % prime == 0) {
                if (first_found < 0) {
                    first_found = j;
                } else {
                    int r_i = root(arr,first_found), r_j = root(arr,j);
                    if (r_i != r_j) {
                       connect(arr, r_i, r_j);
                       s--;
                    }
                }
            }
        }
    }
    return s;
}

int main() {
    int tc, a, b, p, prime_cnt = 0;
    int* primes = primes_less_than_500(&prime_cnt);
    scanf("%d", &tc);
    for (int i = 1; i <= tc; i++) {
        int arr[1001] = {[0 ... 1000] = -1};
        scanf("%d %d %d", &a, &b, &p);
        printf("Case #%d: %d\n", i, sets(a,b,p,arr,primes,prime_cnt));
    }
    free(primes);
    return 0;
}