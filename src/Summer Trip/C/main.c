#include <stdio.h>
#include <stddef.h>
//#include <stdlib.h>

int ones(int i) {
     i = i - ((i >> 1) & 0x55555555);
     i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
     return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

int count(char* word, int len) {
    int counter = 0;
    int since_last[26];
    for (int i = 0; i < 26; i++) since_last[i] = 1 << (word[0]-'a');
    since_last[word[0]-'a'] = 0;
    for (int i = 1; i < len; i++) {
        counter += ones(since_last[word[i]-'a']);
        for (int j = 0; j < 26; j++) {
            since_last[j] |= 1 << (word[i]-'a');
        }
        since_last[word[i]-'a'] = 0;
    }
    return counter;
}

int main() {
    char* line = NULL;
    size_t t = 0;
    int size = getline(&line, &t, stdin);
    printf("%d\n", count(line, size-1));
    // free(line);
    return 0;
}