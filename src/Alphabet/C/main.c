#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int longest_increasing_subsequence(char* arr, int n) {
    int lis[n];
    lis[0] = 1;
    int longest = 1;
    for (int i = 1; i < n; i++ ) {
        lis[i] = 1;
        for (int j = 0; j < i; j++ ) {
            if (arr[i] > arr[j] && lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
                longest = lis[i] > longest ? lis[i] : longest;
            }
        }
    }
    return longest;
}

int main() {
    char buffer[51];
    scanf("%s", buffer);
    printf("%d\n", 26 - longest_increasing_subsequence(buffer, (int)strlen(buffer)));
    return 0;
}